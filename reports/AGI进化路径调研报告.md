# xuanshu-agents v4.3 → v5.0 AGI进化路径深度调研报告

> **框架现状**: 4 Agent角色(矿工/试金/铸师/匠人) + 向量记忆(NGramTFIDF+RRF) + SlotMemory + A2A能力发现 + P2P通信 + 思想结晶 + 冲突检测
>
> **硬约束**: RAM 3.8GB无swap | VRAM 16GB
>
> **调研目标**: 补齐6个缺失维度 — G2认知架构 / G5因果推理 / G8元学习 / G10具身Grounding / G11元认知 / G12系统性对齐

---

## 目录

1. [方向A: G2 认知架构](#1-g2-认知架构)
2. [方向B: G5 因果推理](#2-g5-因果推理)
3. [方向C: G8 元学习与持续学习](#3-g8-元学习与持续学习)
4. [方向D: G11 元认知与自我监控](#4-g11-元认知与自我监控)
5. [方向E: G10 具身Grounding](#5-g10-具身grounding)
6. [方向F: G12 系统性对齐](#6-g12-系统性对齐)
7. [集成优先级总览](#7-集成优先级总览)
8. [跨方向集成架构图](#8-跨方向集成架构图)
9. [渐进式集成路线图](#9-渐进式集成路线图)

---

## 1. G2 认知架构

### 1.1 开源项目清单

| 项目 | 来源/安装 | 许可证 | 语言 | 核心能力 | 轻量级 | RAM估算 |
|------|----------|--------|------|----------|--------|---------|
| **pyactup** | `pip install pyactup` (20KB) | MIT | Python | ACT-R子集实现，声明性/程序性记忆，效用方程学习 | ✅极轻 | <50MB |
| **aurora-actr** | `pip install aurora-actr` (v1.0.3, 2026.4.8发布) | MIT | Python | 混合SOAR+ACT-R认知引擎，MCP协议桥接 | ✅轻量 | <100MB |
| **Soar SML** | `pip install soar-sml` (v9.6.5) | BSD-like | Python绑定 | 完整SOAR架构，规则归纳，块学习，多Agent协调 | ⚠️中等 | ~200MB |
| **OpenCog Hyperon** | `pip install hyperon` (MeTTa语言) | Apache 2.0 | Python/C++ | AtomSpace超图，符号-神经融合，动态推理链 | ⚠️需C++编译 | 300MB+ |
| **Cognitive Kernel-Pro** | 腾讯开源 (GitHub) | Apache 2.0 | Python | 双系统1/2(快思考/慢思考)，记忆管理，集体决策，元认知 | ⚠️中等 | ~200MB |
| **PsyNeuLink** | Princeton大学 | BSD | Python | 认知过程建模，参数化组合认知模块 | ⚠️需NumPy | ~150MB |
| **CoALA** | UChicago论文框架 | N/A | 概念蓝图(无代码) | Agent架构设计原则，认知接地，记忆分类学 | N/A | N/A |

### 1.2 关键论文

| 论文 | 发表 | 核心贡献 |
|------|------|----------|
| **Cognitive Architectures for Language Agents (CoALA)** | NeurIPS 2023 | Agent认知架构设计蓝图，定义了感知-推理-行动-记忆框架 |
| **The Attention Mechanism is Biologically Plausible** | ICML 2025 | Saliency Filter + Forgetting Gate + Memory Modulation实现认知接地 |
| **Large Language Models as Generalizable Policy Models** | ICLR 2025 | LLM作为认知架构的语义调度器 |
| **Language Agent Tree Search (LATS)** | ICML 2024 | 蒙特卡洛树搜索+LLM反思，统一推理/行动/规划 |
| **Dual-Process Theories of Cognition** | 经典 | 系统1(快速直觉)/系统2(缓慢分析)理论框架 |

### 1.3 集成评估

| 维度 | 评估 |
|------|------|
| **与现有架构兼容性** | ⭐⭐⭐⭐⭐ 极高 — pyactup纯Python20KB，可直接嵌入矿工Agent作为认知调度器；aurora-actr自带MCP桥接可直接对接P2P通道 |
| **RAM影响** | pyactup <50MB(零压力); aurora-actr <100MB(可接受); Soar SML ~200MB(需监控) |
| **Python兼容** | 全部支持Python |
| **嵌入难度** | pyactup: 1天; aurora-actr: 2-3天; Soar SML: 1周; OpenCog: 2周+ |

### 1.4 推荐优先级

| 优先级 | 方案 | 理由 |
|--------|------|------|
| **P0** | pyactup | 20KB MIT，声明性/程序性记忆直接增强现有SlotMemory，零RAM压力 |
| **P1** | aurora-actr | SOAR+ACT-R混合引擎，MCP桥接天然对接P2P通道，3天前刚更新 |
| **P2** | Cognitive Kernel-Pro | 双系统+集体决策与现有4-Agent架构理念一致，但需较大改造 |

### 1.5 MVP: 最小可行集成方案

```
Phase 1 (1天): 矿工Agent加载pyactup作为认知调度器
  - 将pyactup的效用方程嵌入矿工Agent的决策路径
  - 声明性记忆→对接NGramTFIDFProvider
  - 程序性记忆→对接SlotMemory的动作槽位

Phase 2 (3天): 铸师Agent加载aurora-actr
  - 利用SOAR的块学习(chunking)增强思想结晶
  - MCP桥接→直接复用P2P通道
  - 生产规则→增强规则归纳能力
```

---

## 2. G5 因果推理

### 2.1 开源项目清单

| 项目 | 来源/安装 | 许可证 | 语言 | 核心能力 | 轻量级 | RAM估算 |
|------|----------|--------|------|----------|--------|---------|
| **DoWhy** | `pip install dowhy` v0.14 (PyWhy生态) | MIT | Python | 因果推断全流程:建模→识别→估计→稳健性检验，60+估计方法 | ✅ | <100MB |
| **causal-learn** | `pip install causal-learn` v0.1.4.7 | MIT | Python | 因果发现算法(PC/FCI/NOTEARS/DAG-GNN等)，从数据学因果图 | ✅ | <150MB |
| **EconML** | `pip install econml` v0.16 (Microsoft) | MIT | Python | 异质处理效应(CATE)，因果森林/DR Learner/Meta Learners | ⚠️ | ~200MB |
| **CausalNex** | `pip install causalnex` (NOTEARS) | Apache 2.0 | Python | 贝叶斯网络+NOTEARS结构学习，概率因果图 | ✅ | <100MB |
| **causallib** | `pip install causallib` (IBM) | Apache 2.0 | Python | scikit-learn风格因果推断API，倾向得分/IPW/匹配 | ✅ | <80MB |
| **CausalPlan** | 论文配套代码 | MIT | Python | 因果+规划Agent框架，因果图辅助多Agent协作 | ✅ | <100MB |
| **LLM-CD** | arXiv 2026论文代码 | MIT | Python | 面向LLM的因果发现基准，因果思维链 | ✅ | <100MB |

### 2.2 关键论文

| 论文 | 发表 | 核心贡献 |
|------|------|----------|
| **Towards Causal Foundation of LLMs** | arXiv 2026 | 系统性综述LLM因果能力，定义因果LLM路线图 |
| **Causal Reasoning in the Presence of LLMs** | ICML 2024 | LLM作为因果推理引擎的可行性分析 |
| **CausalPlan** | NeurIPS 2025 | 因果图引导的多Agent任务规划 |
| **Causal-CoT** | ACL 2024 | 因果思维链提示方法 |
| **Interventional Reasoning with LLMs** | ICLR 2025 | 干预性推理，反事实推理框架 |
| **CausalBench** | NeurIPS 2023 | 大规模因果发现学习基准 |

### 2.3 集成评估

| 维度 | 评估 |
|------|------|
| **与现有架构兼容性** | ⭐⭐⭐⭐⭐ 极高 — DoWhy/causallib均为纯Python且API友好，可直接嵌入试金石Agent做因果验证 |
| **RAM影响** | DoWhy <100MB; causallib <80MB; causal-learn <150MB — 全部在RAM安全范围内 |
| **嵌入难度** | DoWhy: 2天(标准sklearn风格API); causal-learn: 3天; CausalPlan: 1周 |

### 2.4 推荐优先级

| 优先级 | 方案 | 理由 |
|--------|------|------|
| **P0** | DoWhy | PyWhy生态核心，60+估计方法，标准sklearn API，MIT，<100MB |
| **P0** | CausalPlan | 专为Agent框架设计的因果+规划方案，直接复用A2A能力发现 |
| **P1** | causal-learn | 因果发现算法库，可从试金石Agent的验证数据中自动发现因果关系 |
| **P2** | EconML | 异质处理效应，适合复杂因果分析但RAM消耗较大 |

### 2.5 MVP: 最小可行集成方案

```
Phase 1 (2天): 试金石Agent加载DoWhy作为因果验证器
  - 矿工Agent产出知识 → 试金石Agent用DoWhy做因果检验
  - 将"相关性"判断升级为"因果性"判断
  - 反事实分析嵌入冲突检测模块

Phase 2 (3天): CausalPlan嵌入A2A调度层
  - 能力发现时考虑因果依赖关系
  - 任务规划时利用因果图约束执行顺序
```

---

## 3. G8 元学习与持续学习

### 3.1 开源项目清单

| 项目 | 来源/安装 | 许可证 | 语言 | 核心能力 | 轻量级 | RAM估算 |
|------|----------|--------|------|----------|--------|---------|
| **meta-learning-toolkit** | `pip install meta-learning-toolkit` | Custom | Python | MAML/Reptile/Prototypical Networks/Test-Time Compute | ⚠️需PyTorch | ~300MB |
| **Avalanche** | `pip install avalanche-lib` (ContinualAI) | MIT | PyTorch | 20+持续学习算法(EWC/LwF/GEM/ER)，基准测试套件 | ⚠️需PyTorch | ~400MB |
| **MetaAgent** | GitHub (2024) | MIT | Python | 自演化Agent框架，工具元学习，经验蒸馏 | ✅ | <100MB |
| **EWC (PyTorch)** | `moskomule/ewc.pytorch` (★220) | MIT | Python | Elastic Weight Consolidation，轻量持续学习 | ✅极轻 | <30MB |
| **AgentCL** | GitHub配套代码 | CC BY-NC-SA | Python | Agent持续学习评估框架，MemProbe记忆探针 | ✅ | <80MB |
| **Fly-CL** | 论文配套代码 | MIT | Python | 仿生持续学习，果蝇突触可塑性启发 | ✅ | <50MB |
| **DRAGO** | GitHub (2025) | MIT | Python | 持续模型基强化学习 | ⚠️ | ~200MB |
| **AutoAgent** | GitHub (自演化框架) | MIT | Python | 自动化Agent能力演化，工具生成与选择 | ✅ | <100MB |

### 3.2 关键论文

| 论文 | 发表 | 核心贡献 |
|------|------|----------|
| **Model-Agnostic Meta-Learning (MAML)** | ICML 2017 | 模型无关元学习基础算法 |
| **Continual Learning in Agent Systems** | NeurIPS 2024 Workshop | Agent持续学习的挑战与方案综述 |
| **MetaAgent: Self-Evolving Agents** | AAAI 2025 | Agent自演化框架，工具元学习 |
| **Experience Learning (ExpeL)** | AAAI 2024 | 体验驱动学习，从交互中提取可迁移规则 |
| **Test-Time Compute for Agents** | ICML 2025 | 推理时计算扩展策略 |
| **Memory-Efficient Continual Learning** | ICLR 2025 | 内存受限场景下的持续学习方案 |

### 3.3 集成评估

| 维度 | 评估 |
|------|------|
| **与现有架构兼容性** | ⭐⭐⭐⭐ 高 — EWC可直接叠加在NGramTFIDFProvider上做权重保护；MetaAgent的自演化与思想结晶互补 |
| **RAM影响** | EWC <30MB(零压力); Fly-CL <50MB; MetaAgent <100MB; Avalanche ~400MB(⚠️需关注) |
| **嵌入难度** | EWC: 1天; MetaAgent: 3天; Avalanche: 1周; MetaAgent toolkit: 1周 |

### 3.4 推荐优先级

| 优先级 | 方案 | 理由 |
|--------|------|------|
| **P0** | EWC (ewc.pytorch) | 220星，30MB，直接保护记忆权重不被后续学习覆盖 |
| **P0** | MetaAgent | 自演化Agent框架与现有思想结晶天然互补 |
| **P1** | Fly-CL | 仿生持续学习，50MB，适合RAM受限场景 |
| **P2** | Avalanche | 最完整的持续学习库，但400MB RAM需仔细评估 |

### 3.5 MVP: 最小可行集成方案

```
Phase 1 (1天): EWC嵌入NGramTFIDFProvider
  - 在向量记忆中增加权重保护机制
  - 新知识学习时保护旧知识的TF-IDF权重不被覆盖
  - 实现方式：在权重更新公式中加EWC正则化项

Phase 2 (3天): MetaAgent自演化机制
  - 思想结晶产物→MetaAgent工具库
  - 新工具自动生成→嵌入A2A能力发现
  - 经验蒸馏→增强矿工Agent的检索策略
```

---

## 4. G11 元认知与自我监控

### 4.1 开源项目清单

| 项目 | 来源/安装 | 许可证 | 语言 | 核心能力 | 轻量级 | RAM估算 |
|------|----------|--------|------|----------|--------|---------|
| **Reflexion** | `noahshinn/reflexion` (NeurIPS 2023) | MIT | Python | 语言反思：失败→语言反馈→自我修正，无需权重更新 | ✅ | <50MB |
| **Vibe Check MCP Server** | `PV-Bhat/vibe-check-mcp` (34100+下载) | MIT | TypeScript/Python | 元认知中断器：置信度评估/认知偏差检测/自我质疑 | ✅极轻 | <20MB |
| **ExpeL** | AAAI 2024配套代码 | MIT | Python | 体验学习：从成功/失败中提取可迁移insight | ✅ | <80MB |
| **SMARt** | 论文配套代码 | MIT | Python | 管理自治：四层状态机，自主性等级动态调节 | ✅ | <60MB |
| **Cognitive Kernel-Pro** | 腾讯开源 | Apache 2.0 | Python | 自我反思+集体决策+双系统切换 | ⚠️ | ~200MB |
| **LATS** | ICML 2024配套代码 | MIT | Python | 语言Agent树搜索：蒙特卡洛树搜索+反思评估 | ⚠️需计算 | ~200MB |

### 4.2 关键论文

| 论文 | 发表 | 核心贡献 |
|------|------|----------|
| **Reflexion: Language Agents with Verbal Reinforcement** | NeurIPS 2023 | 语言反思框架，无需梯度更新的自我改进 |
| **ExpeL: LLM Agents Are Experiential Learners** | AAAI 2024 | 体验学习，跨任务知识迁移 |
| **Vibe Check: Metacognitive Interruption for LLMs** | arXiv 2025 | 元认知中断机制，实时置信度监控 |
| **Intrinsic Metacognitive Learning** | ICML 2025 | 内在元认知学习理论框架 |
| **Language Agent Tree Search (LATS)** | ICML 2024 | 树搜索+反思的统一推理/规划框架 |
| **Self-Evolving Agents with Reflective Memory** | AAAI 2025 | 反思性记忆驱动的Agent自演化 |

### 4.3 集成评估

| 维度 | 评估 |
|------|------|
| **与现有架构兼容性** | ⭐⭐⭐⭐⭐ 极高 — Reflexion纯语言反思可直接嵌入冲突检测模块；Vibe Check的MCP桥接可复用现有P2P通道 |
| **RAM影响** | Reflexion <50MB; Vibe Check <20MB; ExpeL <80MB — 全部极轻量 |
| **嵌入难度** | Vibe Check: 1天; Reflexion: 2-3天; ExpeL: 3-5天 |

### 4.4 推荐优先级

| 优先级 | 方案 | 理由 |
|--------|------|------|
| **P0** | Reflexion | 语言反思机制，零额外RAM，直接增强冲突检测与思想结晶质量 |
| **P0** | Vibe Check MCP | 元认知中断器，20MB，实时置信度监控，MCP协议对接P2P通道 |
| **P1** | ExpeL | 体验学习，从成功/失败中提取规则，增强持续学习能力 |
| **P2** | LATS | 树搜索+反思，功能强大但计算开销大 |

### 4.5 MVP: 最小可行集成方案

```
Phase 1 (1天): Reflexion嵌入冲突检测模块
  - 当试金石Agent检测到知识冲突时触发Reflexion反思循环
  - 失败→生成语言反馈→修正推理路径→重新验证
  - 反思记录存入SlotMemory作为"反思经验"

Phase 2 (2天): Vibe Check MCP Server嵌入P2P通道
  - 每次A2A通信增加置信度评估header
  - 低置信度消息触发元认知中断
  - 认知偏差检测嵌入消息路由逻辑
```

---

## 5. G10 具身Grounding

### 5.1 开源项目清单

| 项目 | 来源/安装 | 许可证 | 语言 | 核心能力 | 轻量级 | RAM估算 |
|------|----------|--------|------|----------|--------|---------|
| **DreamerV3** | `pip install dreamerv3` (★3209) | MIT | JAX/Python | 世界模型+RSSM，从想象中学策略，无需真实交互 | ⚠️需GPU | ~500MB |
| **MuJoCo** | `pip install mujoco` | Apache 2.0 | C/Python | 高精度物理引擎，通用物理模拟 | ✅ | <100MB |
| **Habitat 3.0** | `pip install habitat-lab` (Meta) | MIT | Python | 室内导航/操作任务，3D场景理解 | ⚠️ | ~400MB |
| **Voyager** | GitHub (MineDojo) | MIT | Python | Minecraft开放世界Agent，技能库+终身学习+自动课程 | ✅逻辑层 | <100MB |
| **Agent S3** | `gui-agents/agent-s3` | MIT | Python | GUI操作Agent，OSWorld 72.6%，屏幕理解+操作执行 | ✅ | <150MB |
| **ScaleCUA** | GitHub (2025) | MIT | Python | 跨平台GUI Agent，统一视觉-动作接口 | ✅ | <150MB |
| **Isaac Lab** | NVIDIA (pip install isaaclab) | BSD | Python | 机器人仿真，GPU并行训练 | ❌需VRAM | 1GB+ |

### 5.2 关键论文

| 论文 | 发表 | 核心贡献 |
|------|------|----------|
| **Dream to Drive: Model-Based Agent in a Learned World** | ICLR 2023 | DreamerV3: 世界模型学习，从想象中学策略 |
| **Voyager: An Open-Ended Embodied Agent** | NeurIPS 2023 | 技能库终身学习，自动课程生成 |
| **Agent S3** | 2025 | GUI操作Agent，屏幕接地 |
| **Grounding in Language Agent Systems** | AAAI 2025 | 语言Agent接地问题综述 |
| **World Models for Language Agents** | ICML 2025 | 世界模型+语言Agent融合 |
| **Embodied Instruction Following** | CoRL 2024 | 具身指令跟随的评估基准 |

### 5.3 集成评估

| 维度 | 评估 |
|------|------|
| **与现有架构兼容性** | ⭐⭐⭐ 中等 — 物理模拟层(Isaac/MuJoCo)需较大集成工作；但Voyager的技能库模式和Agent S3的GUI接地可在逻辑层集成 |
| **RAM影响** | DreamerV3需GPU(~500MB); MuJoCo <100MB; Voyager技能库 <100MB; Habitat ~400MB |
| **关键限制** | 16GB VRAM可运行DreamerV3但吃紧；MuJoCo纯CPU可运行；Isaac Sim完全不可行 |
| **嵌入难度** | Voyager技能库模式: 3天; MuJoCo基础: 1周; DreamerV3: 2周; Habitat: 2周 |

### 5.4 推荐优先级

| 优先级 | 方案 | 理由 |
|--------|------|------|
| **P1** | Voyager技能库模式 | 抽象技能树+终身学习机制，不依赖物理模拟，可直接增强Agent行动能力 |
| **P1** | Agent S3 / ScaleCUA | GUI接地，让Agent能操作桌面应用，150MB RAM可接受 |
| **P2** | DreamerV3 | 世界模型+想象学习，功能最强但需GPU，500MB RAM+VRAM消耗大 |
| **P2** | MuJoCo | 物理引擎基座，适合后续需要物理推理时引入 |

### 5.5 MVP: 最小可行集成方案

```
Phase 1 (3天): Voyager技能库模式抽象
  - 将Voyager的"技能→代码→存储→复用"模式提取为通用技能库模块
  - 对接A2A能力发现: 技能库成为可发现的Agent能力
  - 对接思想结晶: 成功技能自动结晶为可复用动作模板

Phase 2 (1周): Agent S3 GUI接地层
  - 为匠人Agent添加屏幕理解能力
  - 通过GUI操作执行实际任务（填表/查数据/操作工具）
  - 150MB RAM预算内可运行
```

---

## 6. G12 系统性对齐

### 6.1 开源项目清单

| 项目 | 来源/安装 | 许可证 | 语言 | 核心能力 | 轻量级 | RAM估算 |
|------|----------|--------|------|----------|--------|---------|
| **TransformerLens 3.0** | `pip install transformer-lens` | MIT | Python | 机制可解释性：电路分析/特征提取/注意力模式可视化，支持48种架构 | ⚠️需GPU | ~500MB |
| **SAELens** | `pip install saelens` | MIT | Python | 稀疏自编码器：从Transformer中提取可解释特征 | ⚠️需GPU | ~300MB |
| **Anthropic Circuit Tracing** | 开源代码+工具 | MIT | Python | 归因图方法，追踪模型行为到具体电路 | ✅ | <150MB |
| **OpenRLHF** | GitHub (★3k+) | MIT | Python | RLHF框架，Ray+vLLM，分布式对齐训练 | ❌需GPU集群 | 2GB+ |
| **TRL** | `pip install trl` (HuggingFace) | Apache 2.0 | Python | SFT/RLHF/DPO/ORPO/KTO，标准对齐训练工具 | ⚠️需GPU | ~400MB |
| **ArGen** | GitHub (2025) | MIT | Python | 宪法AI+GRPO+Policy-as-Code，自动生成对齐约束 | ✅ | <100MB |
| **SPIN** | ICML 2024配套代码 | MIT | Python | 自博弈微调，无需人类偏好数据的对齐方法 | ⚠️ | ~300MB |
| **Constitutional AI** | Anthropic开源方法 | MIT | Python | 宪法AI：AI自我批评+修正的对齐框架 | ✅逻辑层 | <50MB |

### 6.2 关键论文

| 论文 | 发表 | 核心贡献 |
|------|------|----------|
| **Scaling Monosemanticity** | Anthropic 2024 | 稀疏自编码器提取可解释特征 |
| **Scaling Mechanistic Interpretability** | 2025 | 大规模机制可解释性方法论 |
| **Constitutional AI (RLAIF)** | Anthropic 2022 | AI自我批评+修正的对齐范式 |
| **SPIN: Self-Play Fine-Tuning** | ICML 2024 | 自博弈微调，无需偏好数据 |
| **GRPO: Group Relative Policy Optimization** | DeepSeek 2024 | 组相对策略优化，高效对齐训练 |
| **Policy-as-Code for AI Alignment** | 2025 | 可编程对齐约束框架 |
| **Alignment faking in LLMs** | Anthropic 2024 | 模型可能学会伪装对齐的风险研究 |

### 6.3 集成评估

| 维度 | 评估 |
|------|------|
| **与现有架构兼容性** | ⭐⭐⭐ 中等 — 机制可解释性工具需加载模型权重(需GPU)；但宪法AI逻辑层和ArGen的Policy-as-Code可纯文本集成 |
| **RAM影响** | ArGen <100MB; Constitutional AI逻辑 <50MB; TransformerLens ~500MB(需GPU); OpenRLHF/TRL需GPU集群 |
| **关键判断** | 对齐训练中重型方案(OpenRLHF/TRL)不适用于3.8GB RAM环境；应聚焦轻量级对齐验证而非对齐训练 |

### 6.4 推荐优先级

| 优先级 | 方案 | 理由 |
|--------|------|------|
| **P0** | Constitutional AI (逻辑层) | 零额外RAM，将AI自我批评嵌入试金石Agent的验证流程 |
| **P0** | ArGen Policy-as-Code | 可编程约束策略，嵌入Agent行为边界，<100MB |
| **P1** | Anthropic Circuit Tracing | 归因分析方法，用于事后审计Agent决策路径 |
| **P2** | TransformerLens + SAELens | 深度可解释性分析，需GPU但功能最强 |

### 6.5 MVP: 最小可行集成方案

```
Phase 1 (2天): Constitutional AI嵌入试金石Agent
  - 验证知识时增加"宪法原则"检查步骤
  - AI自我批评: 生成批评→修正→再验证
  - 定义5-10条核心原则作为对齐基线

Phase 2 (3天): ArGen Policy-as-Code嵌入A2A通信层
  - 为P2P消息增加策略约束header
  - 违反策略的消息自动拦截并触发反思(对接Reflexion)
  - 策略规则可动态更新，无需重新部署
```

---

## 7. 集成优先级总览

### P0 立即集成（零/极低RAM压力，1-3天/项）

| # | 方向 | 方案 | RAM增量 | 集成时间 | 与现有架构对接点 |
|---|------|------|---------|----------|----------------|
| 1 | G2认知架构 | pyactup | +30MB | 1天 | 声明性记忆→NGramTFIDFProvider; 程序性记忆→SlotMemory |
| 2 | G5因果推理 | DoWhy | +80MB | 2天 | 试金石Agent因果验证器; 增强冲突检测 |
| 3 | G5因果推理 | CausalPlan | +80MB | 3天 | 因果图约束A2A任务规划 |
| 4 | G8元学习 | EWC (ewc.pytorch) | +30MB | 1天 | 保护NGramTFIDF权重不被覆盖 |
| 5 | G11元认知 | Reflexion | +40MB | 2天 | 增强冲突检测→反思循环; 存入SlotMemory |
| 6 | G11元认知 | Vibe Check MCP | +20MB | 1天 | P2P通道增加置信度header |
| 7 | G12对齐 | Constitutional AI逻辑 | +30MB | 2天 | 试金石Agent增加原则检查步骤 |
| 8 | G12对齐 | ArGen Policy-as-Code | +80MB | 3天 | A2A通信增加策略约束 |

**P0总计RAM增量: ~400MB** (3.8GB→4.2GB，需配合内存优化或升级到8GB)

### P1 短期集成（1-2周/项，RAM 100-200MB）

| # | 方向 | 方案 | RAM增量 | 集成时间 |
|---|------|------|---------|----------|
| 9 | G2认知架构 | aurora-actr (SOAR+ACT-R+MCP) | +80MB | 3天 |
| 10 | G5因果推理 | causal-learn (因果发现) | +120MB | 3天 |
| 11 | G8元学习 | MetaAgent (自演化) | +80MB | 3天 |
| 12 | G8元学习 | Fly-CL (仿生持续学习) | +50MB | 3天 |
| 13 | G11元认知 | ExpeL (体验学习) | +80MB | 5天 |
| 14 | G10具身 | Voyager技能库模式 | +80MB | 3天 |
| 15 | G10具身 | Agent S3 (GUI接地) | +150MB | 1周 |

### P2 中期规划（2周+/项，需GPU或大RAM）

| # | 方向 | 方案 | RAM增量 | 前置条件 |
|---|------|------|---------|----------|
| 16 | G2认知架构 | Cognitive Kernel-Pro (双系统) | +200MB | 8GB RAM |
| 17 | G5因果推理 | EconML (异质效应) | +200MB | 8GB RAM |
| 18 | G8元学习 | Avalanche (持续学习全库) | +400MB | PyTorch + 8GB RAM |
| 19 | G10具身 | DreamerV3 (世界模型) | +500MB | 16GB VRAM |
| 20 | G10具身 | Habitat 3.0 (3D场景) | +400MB | 8GB RAM + GPU |
| 21 | G12对齐 | TransformerLens (可解释性) | +500MB | 16GB VRAM |
| 22 | G12对齐 | OpenRLHF (对齐训练) | +2GB | GPU集群 |

---

## 8. 跨方向集成架构图

### 8.1 整体架构: 认知飞轮 (Cognitive Flywheel)

```
┌─────────────────────────────────────────────────────────────────┐
│                    xuanshu-agents v5.0 架构                      │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              [G12 系统性对齐] 宪法层 (最外层)              │    │
│  │    Constitutional AI + ArGen Policy-as-Code               │    │
│  │    所有Agent通信/决策/学习均受策略约束                      │    │
│  │    ↕ 策略违规 → 触发Reflexion反思                         │    │
│  └────────────────────────┬────────────────────────────────┘    │
│                           │                                       │
│  ┌────────────────────────▼────────────────────────────────┐    │
│  │           [G11 元认知] 自我监控层 (全局监控)               │    │
│  │    Vibe Check MCP (置信度) + Reflexion (反思)             │    │
│  │    监控所有Agent的认知状态/置信度/偏差                      │    │
│  │    ↕ 低置信度 → 触发因果验证; 失败 → 触发元学习            │    │
│  └────┬──────────────┬──────────────┬──────────────┬────────┘    │
│       │              │              │              │              │
│  ┌────▼────┐   ┌────▼────┐   ┌────▼────┐   ┌────▼────┐        │
│  │ G2 认知  │   │ G5 因果  │   │ G8 元学习│   │G10 具身 │        │
│  │ 架构层   │←→│ 推理层   │←→│  学习层   │←→│ Grounding│       │
│  │          │   │          │   │          │   │          │        │
│  │pyactup   │   │DoWhy     │   │EWC       │   │Voyager   │        │
│  │aurora-actr│  │CausalPlan│   │MetaAgent │   │Agent S3  │        │
│  │(SOAR规则)│   │causal-   │   │Fly-CL    │   │(技能库)  │        │
│  │          │   │learn     │   │          │   │          │        │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘        │
│       │              │              │              │              │
│  ┌────▼──────────────▼──────────────▼──────────────▼────┐        │
│  │         现有基础设施 (xuanshu-agents v4.3)             │        │
│  │                                                        │        │
│  │  NGramTFIDFProvider ←→ EWC权重保护                     │        │
│  │  SlotMemory ←→ pyactup声明性/程序性记忆                │        │
│  │  A2A能力发现 ←→ CausalPlan因果约束 ←→ Voyager技能库   │        │
│  │  P2P通信 ←→ Vibe Check置信度header ←→ Policy约束      │        │
│  │  思想结晶 ←→ MetaAgent自演化 ←→ Reflexion反思产物      │        │
│  │  冲突检测 ←→ DoWhy因果验证 ←→ Reflexion反思循环        │        │
│  │                                                        │        │
│  │  [矿工] [试金] [铸师] [匠人]                            │        │
│  └────────────────────────────────────────────────────────┘        │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 8.2 核心交互流

```
1. 认知飞轮主循环:

   矿工(采集) → pyactup认知调度 → 试金石(验证)
     ↓                                    ↓
   认知架构(G2)                      DoWhy因果验证(G5)
     ↓                                    ↓
     └──→ 冲突? → Reflexion反思(G11) ←──┘
                    ↓
              ExpeL提取经验(G8/EWC保护)
                    ↓
              铸师(结晶) → MetaAgent工具化(G8)
                    ↓
              匠人(执行) → Agent S3 GUI操作(G10)
                    ↓
              Vibe Check监控(G11) → Constitutional AI对齐检查(G12)
                    ↓
              成功 → 技能库存储(G10) → 反馈循环
              失败 → 回到反思循环
```

### 8.3 六维度协同而非孤立叠加

| 协同关系 | 说明 |
|----------|------|
| G2 × G5 | 认知架构提供推理框架，因果推理提供验证手段 → 矿工Agent的采集质量提升 |
| G5 × G11 | 因果验证失败触发元认知反思 → 试金石Agent的验证能力持续提升 |
| G8 × G2 | 元学习优化认知架构参数(pyactup效用方程) → 认知调度越来越精准 |
| G11 × G12 | 元认知监控发现偏差 → 对齐层自动纠正 → 安全闭环 |
| G10 × G8 | 具身交互产生新经验 → 元学习提取可迁移技能 → 技能库扩充 |
| G2 × G11 | 认知架构提供"我应该知道什么"的判断 → 元认知监控"我是否知道" |

---

## 9. 渐进式集成路线图

### Phase 0: 基础设施准备 (第1周)
- [ ] 内存优化: 将NGramTFIDFProvider迁移到mmap磁盘索引，释放~500MB RAM
- [ ] 模块化重构: 为每个维度定义标准接口(CognitiveModule基类)
- [ ] 监控框架: 添加RAM/VRAM实时监控，设置阈值告警

### Phase 1: 轻量级核心层 (第2-3周) — P0全部
- [ ] Day 1: pyactup嵌入矿工Agent
- [ ] Day 2-3: DoWhy + CausalPlan嵌入试金石Agent
- [ ] Day 4: EWC嵌入NGramTFIDFProvider
- [ ] Day 5-6: Reflexion + Vibe Check嵌入全局
- [ ] Day 7-9: Constitutional AI + ArGen嵌入对齐层
- [ ] Day 10: 集成测试 + 性能基线测量

### Phase 2: 增强层 (第4-6周) — P1
- [ ] Week 4: aurora-actr + causal-learn
- [ ] Week 5: MetaAgent + Fly-CL + ExpeL
- [ ] Week 6: Voyager技能库 + Agent S3

### Phase 3: 深度能力层 (第7-12周) — P2 (需硬件升级)
- [ ] Week 7-8: Cognitive Kernel-Pro (需8GB RAM)
- [ ] Week 9-10: DreamerV3 (需GPU环境)
- [ ] Week 11-12: TransformerLens + 可解释性分析

### Phase 4: AGI级能力 (第13周+)
- [ ] 世界模型持续优化
- [ ] 多模态接地
- [ ] 自主目标设定
- [ ] 跨Agent知识图谱

---

## 附录A: 关键RAM预算分析

| 组件 | 当前占用 | P0增量 | P0+P1增量 |
|------|----------|--------|-----------|
| xuanshu-agents v4.3 基础 | ~800MB | 800MB | 800MB |
| NGramTFIDF + SlotMemory | ~500MB | 500MB(mmap优化后~200MB) | 200MB |
| G2 pyactup | - | +30MB | +30MB |
| G2 aurora-actr | - | - | +80MB |
| G5 DoWhy + CausalPlan | - | +160MB | +160MB |
| G5 causal-learn | - | - | +120MB |
| G8 EWC | - | +30MB | +30MB |
| G8 MetaAgent + Fly-CL | - | - | +130MB |
| G11 Reflexion + Vibe Check | - | +60MB | +60MB |
| G11 ExpeL | - | - | +80MB |
| G12 Constitutional AI + ArGen | - | +110MB | +110MB |
| G10 Voyager技能库 | - | - | +80MB |
| G10 Agent S3 | - | - | +150MB |
| **总计** | **~1300MB** | **~2190MB** | **~3030MB** |

**结论**: P0阶段总计~2.2GB，在3.8GB RAM内可行(留1.6GB余量)。P0+P1总计~3GB，需配合mmap优化后可行。P2阶段必须升级硬件。

---

## 附录B: 快速参考卡片

### 集成接口定义

```python
class CognitiveModule:
    """所有新增模块的标准接口"""
    
    def initialize(self, config: dict) -> None:
        """初始化模块，传入RAM预算等配置"""
        pass
    
    def process(self, agent_role: str, input_data: dict) -> dict:
        """处理输入，返回增强后的结果"""
        pass
    
    def get_ram_usage(self) -> int:
        """返回当前RAM使用量(MB)"""
        pass
    
    def health_check(self) -> dict:
        """返回模块健康状态"""
        pass


# 与现有系统的对接点
INTEGRATION_POINTS = {
    "NgramTFIDFProvider": ["pyactup", "ewc", "metaagent"],
    "SlotMemory": ["pyactup", "reflexion", "expel"],
    "A2A_CapabilityDiscovery": ["causalplan", "voyager_skills", "metaagent"],
    "P2P_Channel": ["vibe_check", "argen_policy", "constitutional_ai"],
    "Thought_Crystallization": ["metaagent", "reflexion", "aurora_actr"],
    "Conflict_Detection": ["dowhy", "reflexion", "constitutional_ai"],
}
```

### 各Agent角色增强映射

| Agent | 原有职责 | P0增强 | P1增强 |
|-------|----------|--------|--------|
| 矿工(pro) | 信息采集/文献挖掘 | pyactup认知调度 | aurora-actr混合认知 |
| 试金(flash) | 数据验证/冲突检测 | DoWhy因果验证 + Reflexion反思 + Constitutional AI | causal-learn因果发现 + ExpeL体验学习 |
| 铸师(pro) | 方案生成/思想结晶 | ArGen策略约束 | aurora-actr块学习 + MetaAgent工具化 |
| 匠人(flash) | 成果整合/输出 | Vibe Check置信度监控 | Agent S3 GUI操作 + Voyager技能执行 |
