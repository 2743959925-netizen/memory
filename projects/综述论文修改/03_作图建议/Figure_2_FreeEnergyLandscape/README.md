# Figure 2 — Free-energy landscape

## Structure

- `source/`：Python 源代码。
- `output/`：SVG、PDF、600 dpi TIFF 和 PNG 预览图。SVG 与 PDF 可继续编辑；TIFF 适合需要位图投稿副本的情形。

## Figure contract

- **Core conclusion**：自组装的热力学平衡态、亚稳态、动力学捕获态和耗散非平衡稳态具有不同的能量与驱动条件；耗散稳态不应被画成 Gibbs 自由能曲线上的普通局部最低点。
- **Archetype**：single-panel conceptual schematic。
- **Final size**：183 mm × 110 mm，适用于双栏宽度的横向图件。
- **Scientific boundary**：曲线仅表示三个非耗散状态的 Gibbs 自由能地形；右侧蓝色状态是依赖持续能量或物质输入的受驱动稳态。

## Regenerate

在当前 Codex 工作区中运行 `source/plot_free_energy_landscape.py` 即可重新导出全部格式。该脚本使用当前工作区已有的 Python 图形库；若在普通系统 Python 中运行，需先确认其中包含 `Pillow` 和 `reportlab`。

生成的 SVG 以 `<text>` 节点保存文字，便于后续替换字体、调整位置或修改英文表述。
