# README 素材维护

## 下载与视频入口

首页正文使用公司对外的 App 介绍口径。以下四个链接是预留替换位，在填入实际地址后即可作为下载与观看入口使用：

| 标记 | 对应入口 |
| :--- | :--- |
| `APK_DOWNLOAD_URL` | LuxiInfer Android 安装包 |
| `DEMO_SMALL_MODEL_URL` | Qwen3.5-0.8B / 2B 小模型实机视频 |
| `DEMO_MOE_URL` | Qwen3.6-35B-A3B MoE 实机视频 |
| `DEMO_APP_URL` | App 选模型、一键下载、加载与对话的完整演示 |

在首页 `README.md` 中将对应 `href` 值替换为实际链接。各入口旁也有同名 HTML 注释，便于定位。

现有 SVG 是品牌横幅和视频封面设计，不是实机运行截图。使用真实录屏封面时，将 PNG / JPG 文件放入本目录，更新对应 `img src` 和 `alt` 即可。录屏建议标明手机 / SoC、模型、App 版本和输入输出长度，并保留实际加载、等待与生成过程。

## 小模型性能图

- `gdn-performance-sm8750.png`：SM8750 在 4K 上下文下的 Prefill / Decode 柱状对比，首页直接引用。
- `gdn-performance-sm8850.png`：SM8850 在 4K 上下文下的 Prefill / Decode 柱状对比，首页直接引用。
- 同名 SVG：可缩放版本，便于公司材料排版与导出。
- `gdn-performance.csv`：原始速度数据，单位 token/s。
- `plot_gdn_performance.py`：Matplotlib 绘图脚本。

更新 CSV 后，在仓库根目录执行：

```bash
python assets/plot_gdn_performance.py
```

绘图环境需要 Matplotlib、NumPy 和中文字体，例如 Noto Sans CJK。两张图均为 4K 上下文档位。图中每个倍数均为 `LuxiInfer / 高通官方`，按图内数据计算并保留两位小数。

重点结论：SM8750 的 2B Prefill 为高通官方方案的 2.17 倍；SM8850 的 0.8B Decode 为 2.35 倍，2B Decode 为 2.09 倍。最高 Prefill 与最高 Decode 倍数对应不同测试组合。测试条件和高通官方来源保留在首页性能图后的折叠说明中。

## 品牌与演示封面

| 文件 | 用途 |
| :--- | :--- |
| `luxiinfer-banner.svg` | 首页品牌横幅 |
| `demo-small-model.svg` | 小模型实机视频封面 |
| `demo-moe.svg` | MoE 实机视频封面 |
| `demo-app.svg` | App 操作演示封面 |

## MoE 对外性能说明

正文使用不含前瞻专家调度与投机解码的实测数据：最高 Decode 13.58 tokens/s、最高 Prefill 352.44 tokens/s，分别对应正文标注的配置。

高通官方对照来源：[2026 年 9 月 22 日公告](https://www.qualcomm.cn/news/releases/2026/09/releases-2026-09-22-2)，报告 StepEdge-Omni 30B-MoE 在 NPU+GPU 双引擎协同下 Prefill 超过 330 tokens/s。正文按不同模型与执行配置的吞吐量级进行对照。
