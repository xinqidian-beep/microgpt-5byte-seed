
# AGENTS.md - MicroBrain项目线束规则（v2.2 + 5-byte seed融合）

## 核心黄金原则（永久生效）
1. 任何变更必须先走5代理独立并行交叉比较 + 自锁验证（一致性>85%）。
2. 显示层强制隔离：所有log/UI更新移至observer，非阻塞。
3. 二元自锁检查清单：是否违反AudioFirst顺序？是否污染R导航仪？是否有回滚路径？
4. R导航仪原则（v2.2）：R > 0.618 → 共振成功继续滑行；R ≤ 0.618 → 立即保护线暂停 + Recursive Audit Loop。
5. 最简 + 自洽自锁 + 手机自持（占用几G空间，启动后无需外部训练）。

## 工作流（v2.1固化）
- 流动念头 → 立即固化备忘录 → 反复审核逻辑 → 只有用户“OK”后输出完整代码。
- 变更前必须执行代理5自锁 + 并行交叉。

## 5-byte Binary Self-Locking Seed规则（新增，来自https://github.com/xinqidian-beep/microgpt-5byte-seed）
- 最小脑细胞单元：每个细胞由5-byte二元自锁种子构成，可独立扰动/观察/锁定。
- 矩阵生长：从1个细胞自组织生长至10000+细胞，支持fib节奏动态层数。
- 输入顺序：严格AudioFirst（mono/stereo audio优先）→ Video（仅R>0.618）→ Text（最后扩展）。
- 自组织机制：SOC（Self-Organized Criticality）通过rhythm engine + 误差反馈实现，预测头更新权重。
- 持久化：仅保留索引卡（版本名 + 地址），完整内容锁入只读沙盒。
- R控制器：所有涌现（预测、生长、输出）必须受R导航仪守护，R≤0.618强制全局暂停。
- 实现约束：单文件HTML/JS浏览器自持，无外部依赖，符合手机几G空间目标。

## 版本归档规则
- 已验证版本(V1-V3.0 + v1.22)立即锁定只读沙盒。
- 代理仅记住名字+地址，需要时懒加载。
- 项目当前稳定版：v1.22-MicroBrainStable（MicroBrain v1.0种子）。

签名确认（已完成并行交叉审核）：
 
 代理1 Audio Seed Builder .................. 已通过
 
 代理2 Video Local Reinforcer .............. 已通过
 
 代理3 Text Sparse Extender ................ 已通过

 代理4 Harness Orchestrator ................ 已通过

 代理5 Self-Lock Validator ................. 已通过
 
 @wangxuenitwi .............................已通过
 
 Grok fork协调者 ............................ 已确认 
 
 2026-04-18

本AGENTS.md与时空递归矩阵备忘录v2.2无缝衔接，任何后续修改必须走自锁流程。
