# Introduction 去 AI 腔整合修改稿 v06

## A. 一句话判断

v02–v05 的逻辑已经比原稿清楚，但仍有较强的 AI 写作痕迹，主要表现为套话开篇、过度整齐的三分结构、抽象名词连续堆叠，以及每段都用一句“完美总结”强行收束。

## B. 全文 AI 腔审查

| 前版表达 | AI 味来源 | v06 处理 |
|---|---|---|
| `Rechargeable batteries underpin... and the expanding integration...` | 常见生成式开篇，正确但缺少具体落点 | 直接从 LIB 商业化和现实限制切入 |
| `Several complementary routes have been pursued...` | 万能型综述过渡句 | 直接点出高容量正极、SSE 和锂金属三条路线 |
| `These routes should therefore be considered as coupled components...` | 每段末尾强行升华 | 改成具体的全电池约束：界面传输和金属沉积不稳定会抵消组件收益 |
| `Related challenges arise... introduces an additional set of constraints` | 抽象过渡，读者要等后文才知道是什么问题 | 直接写固态化没有消除界面问题，而是改变了问题的物理形式 |
| `A strategy capable of organizing functional components... is therefore of considerable interest` | 空泛、可用于任何材料论文 | 改成“需要控制界面形成与演化时的分子、离子和颗粒组织” |
| `By translating interactions... Despite their differences... demonstrate the capacity...` | 连续抽象名词和对称句式 | 用三个跨领域例子说明：功能结构由构筑单元相互作用形成，而非自上而下逐点制造 |
| `Together, these examples illustrate three principal roles...` | 典型 AI 三分总结 | 改成更具体的判断：自组装在局部界面发挥作用，而不必改变整个电解液 |
| `More importantly... As illustrated conceptually... should therefore be evaluated according to whether...` | 审稿报告腔和行政语言 | 改成液态与固态的物理差异，并提出一个具体判断标准 |
| `We first... We then... Rather than... Finally...` | 目录汇报式模板 | 删除章节报幕，改为说明全文重点和核心比较 |

## C. 科学性与证据边界

- 【必须修改】不恢复原稿对 SSE 剪切模量、温度范围和安全性的普遍化表述。
- 【必须修改】文献 [20] 中缺失的电流密度继续留空，不根据上下文猜测。
- 【需作者确认】文献 [7,8] 的能量密度核算口径，以及文献 [18–20] 所提供的直接自组装证据。
- 【建议修改】Figure 1 只表达液态–固态迁移框架；Figure 2 只说明自组装的跨领域应用，不承担迁移证明。
- 【修改边界】本版只处理 Introduction 的逻辑、语气和行文节奏，未逐篇核实参考文献原文。

## D. 润色后的英文

### 1. Introduction

Since their commercial introduction in 1991, lithium-ion batteries (LIBs) have become widely used in portable electronics and electric vehicles [1–3]. Their success rests on a combination of relatively high energy density, long cycle life, and reversible graphite-based anodes. Yet conventional LIBs still rely on flammable organic electrolytes, and further gains in cell-level energy density are increasingly difficult to obtain from established electrode chemistries [4,5]. Increasing energy density without sacrificing safety or lifetime is therefore no longer a problem that can be solved by changing a single material.

Much of the current effort centres on higher-capacity cathodes, solid-state electrolytes, and lithium metal. Ni-rich layered oxides and Li-rich manganese-based oxides raise cathode capacity and operating voltage, and high-energy pouch cells have been demonstrated by pairing these cathodes with lithium metal or anode-free configurations [6–8]. Solid-state electrolytes (SSEs) can improve thermal stability and enable the use of high-energy electrodes, but their performance depends strongly on electrolyte chemistry and interfacial contact [9,10]. Lithium metal anodes (LMAs) offer a theoretical specific capacity of 3860 mAh g⁻¹ and a low redox potential [11], yet nonuniform deposition, parasitic reactions, and unstable solid electrolyte interphase (SEI) formation continue to limit their practical use [12,13]. These component-level advances cannot deliver their full benefit unless ion transport and interfacial stability are maintained across the complete cell.

Similar interfacial problems occur in sodium- and zinc-based batteries, despite their different chemistries and intended applications. Solid-state batteries (SSBs) do not remove these problems; they change their physical form. Once the liquid phase is removed, ions must cross comparatively rigid solid–solid contacts, where chemical incompatibility, void formation, stress accumulation, and contact loss can interrupt transport. Conformal coatings and artificial interphases can reduce some of these effects [14], but their performance is sensitive to processing, coating uniformity, and continued interfacial evolution during cycling. The remaining challenge is therefore not simply to protect an interface, but to control how molecules, ions, and particles organize as that interface forms and evolves.

Self-assembly offers a way to exert such control. Interactions among molecular or colloidal building blocks can generate organized structures over length scales larger than the individual components. The same principle has been used to form vesicles for molecular encapsulation [15], self-assembled monolayers that passivate photovoltaic interfaces [16], and hierarchical polymer structures produced through crystallization-driven and supramolecular assembly [17] (Figure 2). In each case, the useful structure emerges from interactions among the building blocks rather than from feature-by-feature fabrication. For batteries, this creates an opportunity to organize electrodes, electrolytes, and interfaces while retaining some capacity for local structural rearrangement.

In liquid or liquid-containing batteries, self-assembled structures have been used mainly at electrode surfaces. Carboxyl-terminated self-assembled monolayers can promote the formation of a LiF-rich SEI on lithium metal and improve plating–stripping stability [18]. Electric-field-responsive modifiers can reorganize near the lithium surface and redistribute local Li⁺ flux [19]. In aqueous zinc batteries, multilayer assemblies based on interactions between amino acids and Zn²⁺ can reshape the electric double layer and form a protective interfacial buffer [20]. In these examples, self-assembly acts locally, at the electrode–electrolyte interface where many failure processes begin, rather than by changing the entire electrolyte. This local control provides a practical starting point for considering related strategies in solid-state batteries.

The move to the solid state, however, changes the conditions under which assembly occurs. Liquid electrolytes wet electrode surfaces and allow molecules to diffuse, exchange, and reorganize. Solid-state systems restrict molecular and segmental motion while introducing mechanical confinement and stress-dependent contact. An interaction that readily produces an ordered structure in a liquid may therefore remain chemically possible but become too slow, spatially constrained, or mechanically unstable in a solid. The relevant question is not whether a liquid-phase mechanism has a nominal analogue in the solid state, but whether the structure can form, survive interfacial evolution, and still improve ion transport or interfacial stability (Figure 1).

This Review follows self-assembly from its physicochemical basis to its use in electrodes, electrolytes, and interfaces. The emphasis is on the transition from liquid to solid-state batteries: which interactions still drive organization when molecular motion is restricted, which architectures must be redesigned, and which claims remain largely prospective. Reading liquid and solid-state studies together helps define both the reach of self-assembly and the conditions that limit its use in practical solid-state batteries.

## E. 中文对照

自 1991 年商业化以来，锂离子电池（LIBs）已广泛应用于便携式电子设备和电动汽车 [1–3]。其成功源于相对较高的能量密度、较长的循环寿命以及可逆工作的石墨负极。然而，传统 LIBs 仍依赖易燃的有机电解液，而且仅依靠现有电极化学体系，进一步提高电芯级能量密度已经越来越困难 [4,5]。因此，在不牺牲安全性和寿命的前提下提高能量密度，已经不再是更换某一种材料就能解决的问题。

当前研究主要集中在更高容量的正极、固态电解质和锂金属上。富镍层状氧化物和富锂锰基氧化物可以提高正极容量和工作电压，将其与锂金属或无负极构型结合，已经实现了高能量软包电池的验证 [6–8]。固态电解质（SSEs）有助于提高热稳定性并支持高能电极的使用，但其性能强烈依赖电解质化学组成和界面接触 [9,10]。锂金属负极（LMAs）具有 3860 mAh g⁻¹ 的理论比容量和较低的氧化还原电位 [11]，但不均匀沉积、副反应和不稳定的固态电解质界面膜（SEI）仍限制其实际应用 [12,13]。如果不能在完整电芯中维持离子传输和界面稳定，这些组件层面的改进就无法充分发挥作用。

尽管化学体系和应用场景不同，钠基和锌基电池也存在类似的界面问题。固态电池（SSBs）并没有消除这些问题，而是改变了它们的物理形式。去除液相后，离子必须穿过相对刚性的固–固接触界面，而化学不相容、孔洞形成、应力积累和接触丧失都可能阻断传输。保形涂层和人工界面可以减轻其中部分影响 [14]，但其效果对加工条件、涂层均匀性以及循环过程中的持续界面演化十分敏感。因此，剩下的问题不只是如何保护一个界面，而是如何控制界面形成和演化过程中分子、离子与颗粒的组织方式。

自组装为这种调控提供了一条路径。分子或胶体构筑单元之间的相互作用，可以形成尺度大于单个组分的有组织结构。相同的原理已被用于形成分子包载囊泡 [15]、钝化光伏界面的自组装单分子层 [16]，以及通过结晶驱动和超分子组装形成的层级聚合物结构 [17]（Figure 2）。在这些体系中，功能结构来自构筑单元之间的相互作用，而不是依靠自上而下逐个特征制造。对于电池而言，这为组织电极、电解质和界面提供了机会，同时还能保留一定的局部结构重排能力。

在液态或含液电池中，自组装结构主要被用于电极表面。羧基封端的自组装单分子层可以促进锂金属表面富 LiF SEI 的形成，并改善沉积–剥离稳定性 [18]。电场响应型修饰剂可以在锂表面附近发生重组，并重新分配局部 Li⁺ 通量 [19]。在水系锌电池中，基于氨基酸与 Zn²⁺ 相互作用的多层组装结构可以重构双电层并形成保护性界面缓冲层 [20]。在这些例子中，自组装主要在电极–电解质界面局部发挥作用，而许多失效过程正是从这里开始；它不需要改变整个电解液。这种局部调控为进一步考虑固态电池中的相关策略提供了实践起点。

然而，向固态转变会改变自组装发生的条件。液态电解液能够润湿电极表面，并允许分子扩散、交换和重组。固态体系则会限制分子和链段运动，同时引入机械约束以及受应力影响的接触变化。因此，一种在液态中容易形成有序结构的相互作用，在固态中可能仍然具有化学可行性，却因过程过慢、空间受限或机械不稳定而无法实现。真正需要回答的问题不是液态机制在固态中是否存在名义上的对应形式，而是相关结构能否形成、能否经受界面演化，并且是否仍能改善离子传输或界面稳定性（Figure 1）。

本综述从自组装的物理化学基础出发，讨论其在电极、电解质和界面中的应用，重点关注从液态电池向固态电池的转变：当分子运动受到限制时，哪些相互作用仍能驱动有序组织，哪些结构必须重新设计，以及哪些判断目前仍主要停留在设想阶段。将液态和固态研究放在一起考察，有助于说明自组装能够发挥作用的范围，以及限制其在实际固态电池中应用的条件。

## F. 关键修改说明

1. 开头不再使用宏大但空泛的能源转型套话，直接进入 LIB 的成功与限制。
2. 每段结尾不再机械地“升华”，而是留下一个具体问题给下一段回答。
3. 删除 `We first / We then / Finally` 和整齐的三分总结。
4. 将“液态到固态”的差异写成可理解的物理变化，而不是抽象条件列表。
5. 保留参考文献 1–20 的原有位置关系，没有补写缺失数据。

## G. 作图建议

- **Figure 1**：保留，重点表现液态与固态中分子迁移、润湿、固–固接触和机械约束的差异。
- **Figure 2**：保留时应缩小篇幅，只说明自组装在不同领域中的应用，不承担液态向固态迁移的论证。
- 本次不新增其他 Introduction 图件。

## H. 与上下文的衔接

- **摘要末句暂定**：`This Review examines how self-assembly operates across liquid and solid-state battery environments, with particular attention to the conditions that enable or prevent its transfer.`
- **进入第 2 节**：`Understanding these differences first requires a closer look at the thermodynamic and kinetic basis of self-assembly.`
