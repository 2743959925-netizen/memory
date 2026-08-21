# Introduction：AM 综合审查与修改稿 v02

## 论文信息

- **论文类型**：Review
- **目标期刊**：Advanced Materials（导向）
- **文章题目**：*Self-Assembly for Rechargeable Metal Batteries: Translating Liquid-Phase Principles into Solid-State Architectures*
- **本节标题**：1. Introduction
- **本节核心任务**：说明为什么需要从自组装视角重新审视可充电金属电池，并将本文定位为对液态自组装原则向固态体系迁移条件、证据等级和适用边界的批判性评价。
- **修改边界**：保留原稿参考文献 1–20 的来源关系，不补造数据、文献或机理；尚未逐篇核实原始文献。

## A. 一句话判断

原 Introduction 目前未达到 Advanced Materials 综述的论证水平，最主要的问题不是语法，而是背景路线重复、范围漂移，并将“液态体系中存在自组装案例”过快推导为“自组装可以全面迁移至固态电池”。

## B. 逻辑诊断

### B1. 原有论证链

`LIB 商业化与不足 → 高能正极/SSE/锂金属三条升级路线 → 钠和锌电池 → 再次引入固态电池 → 自组装的跨领域应用 → 液态或含液电池案例 → 自组装可迁移至固态`

### B2. 主要问题

1. **背景重复**：SSE 在第 6 段已经作为 LIB 升级路线出现，第 9 段又将 SSB 作为新的主要路线，造成叙事回环。
2. **中心问题出现过晚**：前半部分大量介绍具体材料和性能，直到后半部分才说明文章真正关心的是自组装。
3. **综述范围漂移**：LIB、LMA、SSB、SIB、ZIB、药物递送、光伏和一般聚合物自组装被赋予近似权重，削弱 rechargeable metal batteries 主线。
4. **证据跳跃**：液态或含液体系中观察到界面调控效果，并不能直接证明相同机制在低分子迁移率和固–固接触环境中仍然成立。
5. **本文贡献表述不准确**：原稿将文章定位为论证迁移的可行性和巨大潜力，缺少对反例、边界和证据等级的评价。

### B3. 推荐的新论证链

`电池的能量密度–安全性矛盾 → 电极/电解质/界面需要协同优化 → 不同金属电池共有的界面与结构问题 → 自组装可提供的调控能力及定义边界 → 液态或含液体系中的代表性证据 → 固态迁移带来的新约束 → 本综述评价迁移条件、证据等级和设计边界`

### B4. 段落任务

| 段落 | 单一任务 |
|---|---|
| 第 1 段 | 建立可充电电池的应用价值以及能量密度–安全性矛盾 |
| 第 2 段 | 综合高能正极、SSE 和 LMA 路线，并指出它们必须在全电池层面协同 |
| 第 3 段 | 提炼不同金属电池及固态化过程中的共同界面问题 |
| 第 4 段 | 定义自组装的能力，同时提出概念纳入边界 |
| 第 5 段 | 概括电池中的代表性自组装证据及其证据局限 |
| 第 6 段 | 明确液态向固态迁移不能被预设，并列出迁移判据 |
| 第 7 段 | 说明本文的组织方式、评价任务和贡献边界 |

## C. 科学性与证据审查

| 级别 | 原稿问题 | 风险判断与处理 |
|---|---|---|
| 【必须修改】 | 将 `self-assembly` 广泛用于吸附、相分离、原位成膜和外场诱导过程 | 不同过程的自发性、可逆性、驱动力和能量输入不同。修改稿明确提出后文需要工作定义和证据标准。 |
| 【必须修改】 | 将液态电池案例直接作为向固态电池迁移的依据 | 液态中的分子迁移、润湿和界面重构与固态中的固–固接触、机械约束和低迁移率不等价。修改稿改为评价迁移条件。 |
| 【必须修改】 | `SSE has an exceptionally high shear modulus (approximately 10⁹ Pa)` | 不同无机、聚合物和复合 SSE 的模量跨越较大范围，不宜概括为统一数值；本版删除普遍化表述。 |
| 【必须修改】 | SSE `fundamentally eliminates` 可燃组分并统一拓宽至 −20–100 °C | 聚合物、复合和部分准固态体系可能仍含可燃或挥发组分，温度范围也依赖具体材料；本版删除绝对表述。 |
| 【必须修改】 | `Zn+` | 常见锌电池载流离子应写为 `Zn²⁺`；仍需逐处结合具体化学物种核对。 |
| 【必须修改】 | 文献 [20] 的电流密度在原始提取文本中缺失 | 不能猜测或补写。本版保留策略描述，删除缺失数值，等待核对原始 Word 和原文。 |
| 【建议修改】 | “LFP 电池能量密度低于 200 Wh kg⁻¹，而下一代 EV 迫切要求超过 400 Wh kg⁻¹” | 该比较依赖电芯/电池包口径、设计目标和应用场景，容易形成不公平比较。本版改为定性描述。 |
| 【需作者确认】 | 文献 [7] 的 510 Wh kg⁻¹、14 Ah 和文献 [8] 的 604 Wh kg⁻¹ | 需核实是材料、活性物质、电芯还是其他核算口径，并确认循环条件及封装质量是否计入。本版仅概括为 high-energy pouch-cell demonstrations。 |
| 【需作者确认】 | 文献 [10] 中 SnF₂/PEO 的作用被描述为构建 `lithiophilic–lithiophobic interface` | 需核对实际界面位置、形成机制、关键表征和电池构型，避免将作者示意图直接写成已证实机制。 |
| 【需作者确认】 | 文献 [18–20] 被视为自组装直接证据 | 需检查是否包含结构表征、时间演化或对照实验，还是仅有性能改善和机理推断。 |
| 【建议修改】 | 多次使用 `exceptional`、`fundamentally`、`formidable`、`breakthrough`、`tremendous` | 无明确比较对象，放大了证据强度。本版删除或改为可核验的功能描述。 |

## D. 润色后的英文

### 1. Introduction

Rechargeable batteries underpin portable electronics, electric vehicles, and the expanding integration of renewable energy. The commercialization of lithium-ion batteries (LIBs) in 1991 marked a decisive step in this development [1]. Their combination of high energy density, long cycle life, and reversible graphite-based anodes has supported widespread deployment across consumer and transportation applications [2,3]. Nevertheless, conventional LIBs remain constrained by the flammability and volatility of organic liquid electrolytes, as well as by the limited cell-level energy density attainable with established electrode chemistries [4,5]. Meeting the simultaneous requirements of higher energy density, improved safety, and longer service life therefore requires coordinated advances in electrode materials, electrolytes, and interfaces.

Several complementary routes have been pursued to address these limitations. Ni-rich layered oxides and Li-rich manganese-based oxides increase cathode capacity and operating voltage, and their combination with lithium metal or anode-free configurations has enabled high-energy pouch-cell demonstrations [6–8]. Replacing liquid electrolytes with solid-state electrolytes (SSEs) offers another route to improve thermal stability and compatibility with high-energy electrodes, although electrochemical and mechanical stability remain strongly dependent on electrolyte chemistry and interfacial design [9,10]. Lithium metal anodes (LMAs), with a theoretical specific capacity of 3860 mAh g⁻¹ and a low redox potential, further increase the attainable energy density [11]. Their practical use, however, is limited by nonuniform deposition, parasitic reactions, and unstable solid electrolyte interphase (SEI) formation, motivating the development of artificial interphases and surface-passivation strategies [12,13]. These routes should therefore be considered as coupled components of a cell rather than as independent solutions.

Related challenges arise in sodium- and zinc-based batteries. Although these chemistries offer advantages in resource availability, cost, or safety, their performance is also affected by sluggish ion-transfer kinetics, heterogeneous metal deposition, interfacial corrosion, and structural degradation. The transition from liquid to solid-state batteries (SSBs) introduces an additional set of constraints. Eliminating bulk liquid does not remove interfacial instability; instead, ion transport must proceed across comparatively rigid solid–solid contacts that are susceptible to chemical incompatibility, void formation, stress accumulation, and loss of physical contact. Conventional approaches, including conformal coatings and deposited artificial interphases, can mitigate some of these problems [14], but their effectiveness and manufacturability depend on processing conditions, coating uniformity, and long-term interfacial evolution. A strategy capable of organizing functional components across molecular, interfacial, and mesoscale dimensions is therefore of considerable interest.

Self-assembly provides one such strategy. In its broad physicochemical sense, self-assembly describes the organization of molecular or colloidal building blocks into structured configurations through interactions such as hydrogen bonding, electrostatic attraction, van der Waals forces, hydrophobic interactions, or coordination. Because these interactions can encode spatial organization and dynamic responsiveness, self-assembly has been used to construct vesicles for molecular encapsulation, self-assembled monolayers for interfacial passivation, and hierarchically organized polymeric structures [15–17] (Figure 2). These examples establish the versatility of self-assembly as a materials-design principle. They do not, however, imply that every adsorption, phase-separation, interfacial reaction, or externally driven ordering process should be classified as self-assembly. A working definition and explicit evidence criteria are therefore required before self-assembly strategies can be compared across battery systems.

In rechargeable metal batteries, self-assembly has been explored to regulate metal nucleation, ion flux, solvation environments, and interphase chemistry. For example, ordered self-assembled monolayers containing carboxyl groups have been used to regulate SEI formation on lithium metal [18], whereas electric-field-responsive modifiers can reorganize near the electrode surface and influence lithium stripping and deposition [19]. Multilayer molecular assembly has also been employed to restructure the electric double layer and stabilize zinc metal interfaces [20]. Collectively, these studies show that self-assembled structures can modify local chemical and electrostatic environments in liquid or liquid-containing cells. However, improved electrochemical performance alone does not establish the proposed assembly mechanism; direct structural characterization, control experiments, and condition-matched electrochemical measurements are needed to distinguish self-assembly from conventional adsorption or reaction-induced interphase formation.

More importantly, the successful operation of a self-assembly strategy in a liquid electrolyte does not guarantee its direct transfer to a solid-state environment. Liquid electrolytes generally provide relatively high molecular mobility, efficient wetting, and continuous interfacial reorganization. By contrast, solid-state systems restrict molecular and segmental motion and introduce solid–solid contact, mechanical confinement, and stress-dependent interfacial evolution. These differences can alter the thermodynamic driving force, kinetic pathway, defect tolerance, and reversibility of an assembly process. As illustrated conceptually in Figure 1, translation from liquid to solid-state batteries should therefore be evaluated according to whether the relevant driving force remains operative, whether the target structure can form and persist, and whether its electrochemical function is demonstrated under solid-state boundary conditions.

Against this background, this Review examines self-assembly in rechargeable metal batteries from physicochemical principles to component-level applications. We first discuss the thermodynamic and kinetic foundations of self-assembly and classify the principal interactions and external stimuli involved. We then analyse representative applications in electrode architectures, liquid and solid-state electrolytes, and electrode–electrolyte interfaces. Rather than assuming universal transferability, we distinguish strategies demonstrated directly in solid-state cells from those supported by liquid-phase evidence or conceptual analogy, and identify the molecular-mobility, interfacial, mechanical, and processing conditions that govern their translation. Finally, we assess the remaining evidence gaps and outline design and validation criteria for implementing self-assembly in practical solid-state battery architectures.

## E. 中文对照

可充电电池支撑着便携式电子设备、电动汽车以及不断扩大的可再生能源并网需求。1991 年锂离子电池（LIBs）的商业化是这一发展过程中的关键节点 [1]。凭借较高的能量密度、较长的循环寿命和可逆工作的石墨负极，LIBs 已广泛应用于消费电子和交通领域 [2,3]。然而，传统 LIBs 仍受到有机液态电解液易燃、易挥发，以及现有电极化学体系可实现的电芯级能量密度有限等问题的制约 [4,5]。因此，同时满足更高能量密度、更高安全性和更长使用寿命，需要电极材料、电解质和界面的协同改进。

为解决这些限制，研究者已经探索了多条互补路线。富镍层状氧化物和富锂锰基氧化物能够提高正极容量和工作电压；将其与锂金属或无负极构型结合，已实现高能量软包电池的验证 [6–8]。以固态电解质（SSEs）替代液态电解液，是提高热稳定性以及高能电极兼容性的另一条路线，但体系的电化学和机械稳定性仍然强烈依赖电解质化学组成与界面设计 [9,10]。锂金属负极（LMAs）具有 3860 mAh g⁻¹ 的理论比容量和较低的氧化还原电位，可进一步提高可达到的能量密度 [11]。然而，其实际应用受到不均匀沉积、副反应和不稳定固态电解质界面膜（SEI）形成的限制，因此需要人工界面层和表面钝化策略 [12,13]。由此可见，这些路线应作为电芯中相互耦合的组成部分进行考虑，而不是彼此独立的解决方案。

钠基和锌基电池也面临相关问题。尽管这些化学体系在资源可获得性、成本或安全性方面具有一定优势，其性能仍会受到离子转移动力学缓慢、金属沉积不均匀、界面腐蚀和结构退化的影响。从液态电池向固态电池（SSBs）转变还会引入额外约束。去除体相液体并不会消除界面不稳定性；相反，离子必须跨越相对刚性的固–固接触界面传输，而这些界面容易发生化学不相容、孔洞形成、应力积累和物理接触丧失。包括保形涂层和沉积型人工界面在内的传统方法可以缓解其中部分问题 [14]，但其有效性和可制造性取决于加工条件、涂层均匀性以及界面的长期演化。因此，能够在分子、界面和介观尺度上组织功能组分的策略具有重要研究价值。

自组装提供了这样一种策略。从广义物理化学角度看，自组装是分子或胶体构筑单元通过氢键、静电吸引、范德华力、疏水相互作用或配位作用等相互作用，组织成具有一定结构的构型。由于这些相互作用能够编码空间组织和动态响应，自组装已被用于构筑分子包载囊泡、界面钝化自组装单分子层以及具有层级结构的聚合物体系 [15–17]（Figure 2）。这些例子说明自组装是一种具有广泛适用性的材料设计原理。然而，它们并不意味着所有吸附、相分离、界面反应或外场驱动的有序化过程都应被归类为自组装。因此，在比较不同电池体系中的自组装策略之前，需要建立工作定义和明确的证据判据。

在可充电金属电池中，自组装已被用于调控金属成核、离子通量、溶剂化环境和界面膜化学。例如，含羧基的有序自组装单分子层被用于调控锂金属表面的 SEI 形成 [18]；电场响应型修饰剂可以在电极附近发生重组，并影响锂的剥离和沉积 [19]；多层分子组装也被用于重构双电层并稳定锌金属界面 [20]。总体而言，这些研究说明，自组装结构可以改变液态或含液电池中的局部化学和静电环境。然而，仅凭电化学性能改善并不能证实所提出的组装机制。还需要直接结构表征、对照实验和测试条件匹配的电化学测量，以区分自组装与常规吸附或反应诱导的界面膜形成。

更重要的是，自组装策略在液态电解液中能够有效工作，并不意味着它可以直接迁移到固态环境。液态电解液通常具有相对较高的分子迁移能力、良好的润湿性和持续的界面重组能力。相比之下，固态体系会限制分子和链段运动，并引入固–固接触、机械约束以及受应力影响的界面演化。这些差异可能改变组装过程的热力学驱动力、动力学路径、缺陷容忍度和可逆性。如 Figure 1 所示，从液态向固态电池的迁移应根据以下问题进行评价：相关驱动力是否仍然有效，目标结构能否形成并长期保持，以及其电化学功能是否已在固态边界条件下得到证明。

在此背景下，本综述从物理化学原理到电池组件层面的应用，讨论可充电金属电池中的自组装。首先介绍自组装的热力学和动力学基础，并对主要相互作用和外部刺激进行分类；随后分析其在电极结构、液态与固态电解质以及电极–电解质界面中的代表性应用。本文不预设所有策略均可迁移，而是区分已在固态电池中直接验证的策略、仅由液态证据支持的策略和仍处于概念类比阶段的策略，并识别控制其迁移的分子运动、界面、机械和加工条件。最后，本文评估尚存的证据缺口，并提出将自组装应用于实用固态电池架构所需的设计与验证标准。

## F. 关键修改说明

| 原表达或原结构 | 问题 | 修改思路 |
|---|---|---|
| `Rechargeable batteries ... have been ubiquitously deployed` | 开篇冗长且 `ubiquitously` 夸张 | 直接说明应用领域和研究需求 |
| 将高能正极、SSE 和 LMA 分成三个编号段落 | 类似教科书式罗列，且缺少三者耦合关系 | 合并为一个综合段，并以 cell-level coupling 收束 |
| `SSE fundamentally eliminates...` | 将不同 SSE 普遍化，因果和安全结论过强 | 改为 offers another route，并补充化学和界面依赖性 |
| 钠、锌和固态电池各自展开背景 | 范围不断扩张，中心问题不清 | 将其压缩为共同的界面和结构失效问题 |
| 大篇幅介绍药物、光伏和聚合物案例 | 偏离电池主线 | 压缩为一个概念段，仅用于说明自组装的通用能力 |
| `demonstrates robust cross-system versatility` | 性能案例被用于证明机制普适性 | 改为列举可观察的调控对象，并增加证据局限 |
| `comprehensively migrating these technologies` | 预设液态到固态迁移已经成立 | 改为评价哪些驱动力和结构能够在固态条件下保持 |
| 原结尾仅列文章包含哪些内容 | 缺少综述的独特评价任务 | 加入证据分级、迁移条件和验证标准 |

## G. 作图建议

### G1. Figure 1：建议保留并重构

- **核心结论**：液态自组装策略能否迁移到固态，不取决于概念相似性，而取决于驱动力、结构形成、结构保持和固态电化学功能是否得到验证。
- **建议图型**：三阶段迁移框架或证据阶梯图。
- **面板顺序**：
  - **a**：液态、准固态和全固态环境的分子迁移率、润湿和机械约束差异；
  - **b**：`driving force → assembled structure → electrochemical function` 因果链；
  - **c**：`liquid evidence → solid-state direct evidence → remaining hypothesis` 证据等级；
  - **d**：迁移失败的可能原因，包括动力学冻结、接触丧失、应力破坏和界面化学失配。
- **需要的数据/文献**：正文中用于支持液态和固态案例的代表性文献；如无可比较定量数据，本图应明确标为概念框架，不绘制虚构数值。
- **视觉编码**：蓝色表示液态直接证据，橙色表示固态直接证据，灰色虚线表示概念类比或待验证路径。
- **图注必须说明**：哪些部分是作者综合，哪些属于文献证据；不同电池条件不可直接比较；虚线不代表已验证因果关系。
- **建议图题**：

> **Conceptual framework for evaluating the translation of self-assembly from liquid to solid-state batteries.** The framework distinguishes differences in molecular mobility, interfacial contact, mechanical constraint, structural persistence, and the level of direct experimental evidence.

### G2. Figure 2：不建议继续作为独立大型主图

- **原因**：生物、药物递送、光伏和一般聚合物案例会强化“自组装大全”的印象，削弱 rechargeable metal batteries 的范围。
- **处理建议**：压缩为 Figure 1a 中的一个小型概念面板，或移入 Supporting Information。
- **若必须保留**：只选择 2–3 个能直接解释电池设计原理的例子，并明确其作用是解释通用组装原理，而不是证明向电池迁移。
- **建议图题**：

> **Representative manifestations of self-assembly across different material systems.** Non-battery examples are included to illustrate general assembly principles rather than to establish their direct transferability to electrochemical systems.

## H. 与上下文的衔接

### H1. 与摘要的衔接（暂定摘要末句）

> This Review therefore evaluates not only how self-assembly regulates rechargeable metal batteries, but also the physicochemical and engineering conditions under which liquid-phase principles can be translated into solid-state architectures.

### H2. Introduction 进入第 2 节的过渡句

> A rigorous assessment of this transferability first requires a clear physicochemical description of how self-assembled structures form, evolve, and persist under thermodynamic and kinetic constraints.

### H3. 第 2 节需要承担的后续任务

第 2 节不能只介绍自组装基础理论，还应在结尾回答：这些热力学与动力学原则进入低分子迁移率、固–固接触和机械受限环境后，哪些保持不变，哪些发生改变。
