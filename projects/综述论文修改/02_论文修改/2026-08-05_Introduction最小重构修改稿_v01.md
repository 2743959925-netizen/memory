# Introduction 最小重构修改稿 v01

## 修改定位

- 保留原稿“电池需求 → 技术路线 → 固态挑战 → 自组装 → 本综述范围”的总体方向。
- 将原稿中分散的三条锂电池升级路线合并，减少重复背景。
- 将跨领域自组装案例压缩为一个段落，避免偏离电池主线。
- 不再预设液态自组装策略能够直接迁移到固态，而是将本文任务改为评价迁移条件、证据等级和适用边界。
- 暂用方括号表示原稿参考文献编号，后续写回 Word 时再统一为目标期刊格式。

## 术语暂定

| 统一术语 | 首次出现形式 | 原稿中的问题 | 本稿决定 |
|---|---|---|---|
| lithium-ion batteries | lithium-ion batteries (LIBs) | `LIB` 单复数混用 | 缩写统一为 `LIBs` |
| solid-state electrolytes | solid-state electrolytes (SSEs) | `SSE` 单复数混用 | 缩写统一为 `SSEs` |
| solid-state batteries | solid-state batteries (SSBs) | `SSB` 单复数混用 | 缩写统一为 `SSBs` |
| lithium metal anodes | lithium metal anodes (LMAs) | `LMA` 与 lithium metal 混用 | 首次定义后使用 `LMAs` |
| self-assembled monolayers | self-assembled monolayers (SAMs) | `SAM`、`SAMs` 混用 | 按单复数使用 |
| zinc ions | Zn²⁺ | 原稿写为 `Zn+` | 更正为 `Zn²⁺`，仍需结合原文逐处核对 |

## Revised Introduction

### 1. Introduction

Rechargeable batteries underpin portable electronics, electric vehicles, and the expanding integration of renewable energy. The commercialization of lithium-ion batteries (LIBs) in 1991 marked a decisive step in this development [1]. Their combination of high energy density, long cycle life, and reversible graphite-based anodes has supported widespread deployment across consumer and transportation applications [2,3]. Nevertheless, conventional LIBs remain constrained by the flammability and volatility of organic liquid electrolytes, as well as by the limited cell-level energy density attainable with established electrode chemistries [4,5]. Meeting the simultaneous requirements of higher energy density, improved safety, and longer service life therefore requires coordinated advances in electrode materials, electrolytes, and interfaces.

Several complementary routes have been pursued to address these limitations. Ni-rich layered oxides and Li-rich manganese-based oxides increase cathode capacity and operating voltage, and their combination with lithium metal or anode-free configurations has enabled high-energy pouch-cell demonstrations [6–8]. Replacing liquid electrolytes with solid-state electrolytes (SSEs) offers another route to improve thermal stability and compatibility with high-energy electrodes, although electrochemical and mechanical stability remain strongly dependent on electrolyte chemistry and interfacial design [9,10]. Lithium metal anodes (LMAs), with a theoretical specific capacity of 3860 mAh g⁻¹ and a low redox potential, further increase the attainable energy density [11]. Their practical use, however, is limited by nonuniform deposition, parasitic reactions, and unstable solid electrolyte interphase (SEI) formation, motivating the development of artificial interphases and surface-passivation strategies [12,13]. These routes should therefore be considered as coupled components of a cell rather than as independent solutions.

Related challenges arise in sodium- and zinc-based batteries. Although these chemistries offer advantages in resource availability, cost, or safety, their performance is also affected by sluggish ion-transfer kinetics, heterogeneous metal deposition, interfacial corrosion, and structural degradation. The transition from liquid to solid-state batteries (SSBs) introduces an additional set of constraints. Eliminating bulk liquid does not remove interfacial instability; instead, ion transport must proceed across comparatively rigid solid–solid contacts that are susceptible to chemical incompatibility, void formation, stress accumulation, and loss of physical contact. Conventional approaches, including conformal coatings and deposited artificial interphases, can mitigate some of these problems [14], but their effectiveness and manufacturability depend on processing conditions, coating uniformity, and long-term interfacial evolution. A strategy capable of organizing functional components across molecular, interfacial, and mesoscale dimensions is therefore of considerable interest.

Self-assembly provides one such strategy. In its broad physicochemical sense, self-assembly describes the organization of molecular or colloidal building blocks into structured configurations through interactions such as hydrogen bonding, electrostatic attraction, van der Waals forces, hydrophobic interactions, or coordination. Because these interactions can encode spatial organization and dynamic responsiveness, self-assembly has been used to construct vesicles for molecular encapsulation, self-assembled monolayers for interfacial passivation, and hierarchically organized polymeric structures [15–17] (Figure 2). These examples establish the versatility of self-assembly as a materials-design principle. They do not, however, imply that every adsorption, phase-separation, interfacial reaction, or externally driven ordering process should be classified as self-assembly. A working definition and explicit evidence criteria are therefore required before self-assembly strategies can be compared across battery systems.

In rechargeable metal batteries, self-assembly has been explored to regulate metal nucleation, ion flux, solvation environments, and interphase chemistry. For example, ordered self-assembled monolayers containing carboxyl groups have been used to regulate SEI formation on lithium metal [18], whereas electric-field-responsive modifiers can reorganize near the electrode surface and influence lithium stripping and deposition [19]. Multilayer molecular assembly has also been employed to restructure the electric double layer and stabilize zinc metal interfaces [20]. Collectively, these studies show that self-assembled structures can modify local chemical and electrostatic environments in liquid or liquid-containing cells. However, improved electrochemical performance alone does not establish the proposed assembly mechanism; direct structural characterization, control experiments, and condition-matched electrochemical measurements are needed to distinguish self-assembly from conventional adsorption or reaction-induced interphase formation.

More importantly, the successful operation of a self-assembly strategy in a liquid electrolyte does not guarantee its direct transfer to a solid-state environment. Liquid electrolytes generally provide relatively high molecular mobility, efficient wetting, and continuous interfacial reorganization. By contrast, solid-state systems restrict molecular and segmental motion and introduce solid–solid contact, mechanical confinement, and stress-dependent interfacial evolution. These differences can alter the thermodynamic driving force, kinetic pathway, defect tolerance, and reversibility of an assembly process. As illustrated conceptually in Figure 1, translation from liquid to solid-state batteries should therefore be evaluated according to whether the relevant driving force remains operative, whether the target structure can form and persist, and whether its electrochemical function is demonstrated under solid-state boundary conditions.

Against this background, this Review examines self-assembly in rechargeable metal batteries from physicochemical principles to component-level applications. We first discuss the thermodynamic and kinetic foundations of self-assembly and classify the principal interactions and external stimuli involved. We then analyse representative applications in electrode architectures, liquid and solid-state electrolytes, and electrode–electrolyte interfaces. Rather than assuming universal transferability, we distinguish strategies demonstrated directly in solid-state cells from those supported by liquid-phase evidence or conceptual analogy, and identify the molecular-mobility, interfacial, mechanical, and processing conditions that govern their translation. Finally, we assess the remaining evidence gaps and outline design and validation criteria for implementing self-assembly in practical solid-state battery architectures.

## 建议同步修改的图题

### Figure 1

原图题：

> Examples and outcomes of the technology transfer of self-assembly from liquid to solid

建议改为：

> **Conceptual framework for evaluating the translation of self-assembly from liquid to solid-state batteries.** The framework distinguishes differences in molecular mobility, interfacial contact, mechanical constraint, structural persistence, and the level of direct experimental evidence.

### Figure 2

建议改为：

> **Representative manifestations of self-assembly across different material systems.** Non-battery examples are included to illustrate general assembly principles rather than to establish their direct transferability to electrochemical systems.

## 论证链变化

原稿：

`LIB发展与不足 → 三条升级路线 → 钠/锌电池 → 固态电池 → 自组装跨领域应用 → 电池案例 → 自组装可迁移到固态`

修改稿：

`电池的能量与安全矛盾 → 电极/电解质/界面必须协同 → 不同金属电池的共同界面问题 → 自组装的能力与定义边界 → 液态电池中的直接证据 → 固态迁移的新增约束 → 本综述评价什么`

## 需要作者后续核实

- 文献 [7] 和 [8] 中 510 Wh kg⁻¹、604 Wh kg⁻¹ 的能量密度核算口径是否为 cell level，以及是否包含封装质量。
- 文献 [9] 是否支持对 SSE 剪切模量的概括；原稿的“所有 SSE 约为 10⁹ Pa”不宜保留为普遍结论。
- 文献 [10] 中 SnF₂/PEO 体系的准确作用位置、界面组成和电池构型。
- 文献 [18–20] 是否提供直接的自组装结构证据，而不仅是性能改善或机理示意。
- 文献 [20] 的电流密度在原始 Word 提取文本中缺失，当前修改稿未补写该数值。

## 当前证据边界

- **可支持**：自组装已用于调控液态或含液体系中的电极界面、离子分布和界面膜形成。
- **需进一步分级**：哪些策略已在真正的全固态电池中直接验证。
- **目前不能直接支持**：液态体系中的自组装原则可以普遍、无条件地迁移到所有固态电池。
