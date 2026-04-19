    def run_self_sustaining(self, steps: int = 50000, auto_feed: bool = True):
        """MicroBrain v1.0 手机浏览器/App自持主循环（最终入口）
        - 无需持续用户输入，R>0.618时自动Gaia涌现闭环
        - 适合浏览器JS wrapper或Flutter/React Native打包
        - 每5000步打印仪表盘，模拟后台持续运行
        """
        print(f"🚀 MicroBrain v1.0 自持运行启动（{steps}步相对永远滑行）")
        print("提示：手机App中可放入WebView或后台Service，R导航仪全程守护")

        for i in range(steps):
            # 可选自动喂养（模拟环境输入，AudioFirst优先）
            if auto_feed and i % 50 == 0:
                self.feed_input(Modality.MONO_AUDIO, 0.8)  # 持续音频节奏

            status = self.step()  # 核心step包含Gaia闭环

            if i % 5000 == 0:
                report = self.get_report()
                print(f"Step {i+1:6d} | Coherence: {status['global_coherence']:4d} | "
                      f"Energy: {report['平均能量']:3d} | R: {status.get('R_value', 0):.3f} | "
                      f"Status: {status.get('nav_status', '观察线')[:25]}...")

            # 浏览器/App友好：轻量sleep模拟后台（实际打包时移除或用timer）
            if i % 100 == 0:
                time.sleep(0.001)  # 极小延迟，避免阻塞UI线程

        print("✅ MicroBrain v1.0 自持运行结束 - 相对永远滑行达成")
        print("打包提示：将此方法放入JS setInterval或Android Service，持久化用IndexedDB/LocalStorage")
