<h1 align="center">LuxiInfer</h1>

<div align="center">

**面向 Dense 与 MoE 模型的高效端侧推理，以自研核心算子、超低比特量化和动态专家调度，突破移动端计算与存储瓶颈。**

![Android](https://img.shields.io/badge/Platform-Android-green.svg) ![ExecuTorch](https://img.shields.io/badge/Runtime-ExecuTorch-blue.svg) ![Hexagon NPU](https://img.shields.io/badge/Backend-Hexagon%20NPU-blue.svg)

[🎬 实机演示](#demo) · [🚀 快速开始](#quick-start) · [📰 最新动态](#news) · [⚡ 性能表现](#performance) · [🧩 技术方案](#technology)

</div>

<a id="features"></a>

**LuxiInfer** 是陆兮科技面向高通移动平台打造的本地 AI 应用与端侧推理方案，支持不同架构和规模的模型在手机上运行，提供文本对话与图文理解。

面对模型架构日益多样、参数规模不断增长带来的挑战，LuxiInfer 基于 **ExecuTorch 与高通原生 AI 技术栈**，贯通模型适配、算子加速、低比特量化、存储管理与运行时调度，形成一套完整的端侧高性能推理方案。

- 📱 **一键下载，本地离线运行**：提供开箱即用的 App 体验。在 App 中选择并下载模型后即可开始文本对话与图文交互。模型下载完成后，全流程支持手机本地离线推理，保障数据隐私。
- ⚡ **底层算子自研，高效释放 NPU 算力**：面向高通 Hexagon NPU，结合**自研 GDN 融合算子**、HVX 向量化与模型执行优化，解决混合注意力模型在通用框架下调度频繁、访存开销大的问题，显著提升计算效率。
- 💾 **计算与存储协同，降低资源开销**：根据模型特点，结合低比特量化、动态缓存和异步加载等技术，优化权重存储、内存占用与运行时调度，让大参数模型也能适应手机端资源。
- 🧠 **一套方案，覆盖多种模型架构**：同一套端侧推理方案覆盖 Dense 与 MoE 架构。让用户既能体验 2B 模型的极速响应，也能在手机上跑通 35B 大模型进行复杂的文本问答与图文理解。

LuxiInfer 将持续扩展对不同模型架构的适配，推进更通用的端侧算子、量化与运行时解决方案，为未来的混合架构模型和本地智能应用提供支持。

<a id="demo"></a>

## 🎬 实机演示

以 Qwen3.5-2B 和 Qwen3.6-35B-A3B 为代表，展示 Dense 与 MoE 模型在手机上的输入处理、流式生成与图文问答。

<table>
  <tr>
    <td width="50%" align="center">
      <!-- DEMO_SMALL_MODEL_URL：替换为 Dense 模型实机视频地址。 -->
      <a href="DEMO_SMALL_MODEL_URL"><img src="assets/demo-small-model.svg" width="100%" alt="观看 Qwen3.5-2B Dense 模型实机演示" /></a>
      <br /><b>Dense · Qwen3.5-2B：输入处理与连续生成</b>
      <p>查看 GDN 加速下的长文本处理、流式回答与运行速度。</p>
    </td>
    <td width="50%" align="center">
      <!-- DEMO_MOE_URL：替换为 Qwen3.6-35B-A3B 实机视频地址。 -->
      <a href="DEMO_MOE_URL"><img src="assets/demo-moe-v1.2.svg" width="100%" alt="观看 Qwen3.6-35B-A3B MoE 实机演示" /></a>
      <br /><b>MoE · Qwen3.6-35B-A3B：手机本地大模型推理</b>
      <p>查看 Qwen3.6 的材料问答、图片理解与持续生成。</p>
    </td>
  </tr>
</table>

<!-- DEMO_APP_URL：替换为 App 完整体验视频地址。 -->
<p align="center">
  <a href="DEMO_APP_URL"><img src="assets/demo-app.svg" width="100%" alt="观看 LuxiInfer App 操作演示：模型选择、一键下载、加载与本地对话" /></a>
</p>
<p align="center"><b>App 完整体验：模型库 → 一键下载 → 加载模型 → 本地对话</b></p>

<a id="quick-start"></a>

## 🚀 快速开始

<a id="supported"></a>

### 1. 设备与模型

目前开放下载以下两款模型，下载前请预留相应的手机存储空间：

| 模型 | 参数规模 | 已验证芯片平台 | 支持能力 | 所需存储空间 |
| :--- | :--- | :--- | :--- | :---: |
| Qwen3.5-2B（Dense） | 2B | 高通 Snapdragon 8 elite<br>高通 Snapdragon 8 elite Gen 5 | 手机本地文本与图文推理 | 约 1.8 G |
| Qwen3.6-35B-A3B（MoE） | 35B 总参数 / 约 3B 激活参数 | 高通 Snapdragon 8 elite Gen 5 | 手机本地文本与图文推理 | 约 10.6 G |


<a id="download"></a>

### 2. 下载与安装

<!-- APK_DOWNLOAD_URL：替换为 Android 安装包下载地址。 -->
下载 [**LuxiInfer Android App**](APK_DOWNLOAD_URL)，在 Android 手机上安装并打开。

### 3. 加载模型，开始对话

1. **选择模型。** 进入 App 模型库，按任务需要选择模型。
2. **一键下载并加载。** 下载配套模型包，完成后加载模型。
3. **开始本地对话。** 输入文字或图片，体验文本问答、图片理解与流式生成。

模型下载需要网络；下载完成后，即可在离线状态下使用手机本地推理。

<a id="news"></a>

## 📰 最新动态

- 📱 **[2026-10-30]** **LuxiInfer-Android v1.0** 发布，支持模型一键下载与手机 NPU 本地推理。目前开放 Qwen3.5-2B 和 Qwen3.6-35B-A3B 套件。
- 🚀 **[2026-10-23]** 完成 **Qwen3.6-35B-A3B MoE** 手机端部署，纯文本 Prefill 达到 **516.661 tokens/s**，图文 Decode 达到 **17.262 tokens/s**。
- ⚡ **[2026-10-20]** 完成 **Qwen3.5-2B Dense** 模型加速。实测在 4K 上下文下，Prefill 达到 **1441.75 tokens/s**，Decode 达到 **50.95 tokens/s**。

<a id="performance"></a>

## ⚡ 性能表现

<a id="small-model-performance"></a>

### 🚀 Dense 模型实测：Qwen3.5-0.8B / 2B

在 **4K 上下文**下，LuxiInfer 在 **高通 Snapdragon 8 elite Gen 5** 上实现：

- **Qwen3.5-0.8B：** Prefill **1843.58 tokens/s**，Decode **90.33 tokens/s**。
- **Qwen3.5-2B：** Prefill **1441.75 tokens/s**，Decode **50.95 tokens/s**。

下图汇总 **Qwen3.5-0.8B / 2B** 在 **高通 Snapdragon 8 elite** 与 **高通 Snapdragon 8 elite Gen 5** 平台、**4K 上下文**下的推理速度：上方为 **Prefill（输入处理）**，下方为 **Decode（连续生成）**，单位均为 token/s，**数值越高，速度越快**。蓝色为 LuxiInfer，灰色为高通官方；每组标出实测速度与速度比。

![Qwen3.5-0.8B / 2B 在高通 Snapdragon 8 elite 与高通 Snapdragon 8 elite Gen 5 平台上的 4K 上下文 NPU 推理性能对比：Prefill 最高 2.17 倍，Decode 最高 2.35 倍](<assets/LuxiInfer_Qwen3.5_倍数与模型字号精简_4K.png>)

对比高通官方方案，**Prefill 速度最高达到 2.17 倍（提升 116.70%）**；**Decode 速度最高达到 2.35 倍（提升 135.20%）**。上述结果体现 GDN 算子与整模执行路径的协同优化效果。

***高通官方数据来源：** Qualcomm AI Hub，[Qwen3.5-0.8B 官方性能数据](https://github.com/qualcomm/ai-hub-models/blob/v0.65.0/src/qai_hub_models/models/qwen3_5_0_8b/perf.yaml)、[Qwen3.5-2B 官方性能数据](https://github.com/qualcomm/ai-hub-models/blob/v0.65.0/src/qai_hub_models/models/qwen3_5_2b/perf.yaml)。设备、量化细节与软件版本存在差异，结果用于同档位参考对比；图中速度比按所展示数值计算并四舍五入，提升百分比沿用测试汇总记录。*

<a id="moe-performance"></a>

### 🧠 MoE 模型实测：Qwen3.6-35B-A3B

在**不使用前瞻专家调度与投机解码技术**的情况下，LuxiInfer 实现高性能的手机端 35B MoE 推理：

- 🚀 **Decode 最高 17.262 tokens/s。** 支持手机本地连续生成，满足文本问答与图文交互需求。
- ⚡ **Prefill 最高 516.661 tokens/s。** 输入处理吞吐突破 500 tokens/s，加快长输入任务的处理。

> 💾 **35B MoE，低内存部署：** Qwen3.6-35B-A3B 在一台配备 **12 GiB 运行内存**的 **高通 Snapdragon 8 elite Gen 5** 手机上本地运行，且峰值运行内存低至 **约 3.8 GiB**。

**高通官方端侧 MoE 吞吐参考。** 高通在[官方公告](https://www.qualcomm.cn/news/releases/2026/09/releases-2026-09-22-2)中披露，StepEdge-Omni 30B-MoE 通过 NPU+GPU 双引擎协同，预填充吞吐超过 **330 tokens/s**。LuxiInfer 的 Qwen3.6-35B-A3B 在 Hexagon NPU 推理路径上达到 **516.661 tokens/s**；两者为不同模型与执行配置下的吞吐量级对照。

#### 📊 1024 → 1024 token 实测

**测试平台：高通 Snapdragon 8 elite Gen 5；总上下文：2048 token。** 以下展示同一配置下的纯文本与图文实测结果，输入与输出长度均为 1024 token。

| 输入类型 | 输入 → 输出 token | Prefill（tokens/s） | Decode（tokens/s） |
| :---: | :---: | :---: | :---: |
| 纯文本 | 1024 → 1024 | 516.661 | 14.179 |
| 图文 | 1024 → 1024 | 370.344 | 17.262 |

图文任务的首次响应还包含图片处理与视觉编码时间。

<a id="technology"></a>

## 🧩 技术方案

LuxiInfer 基于高通原生 AI 加速技术栈，以 **ExecuTorch 为推理执行底座**，面向 Dense 与 MoE 模型提供统一的端侧推理方案。通过优化混合注意力模型的核心计算，并结合 MoE 专家权重的存储与运行时调度，协同优化不同模型架构的计算与资源使用。

### GDN：混合注意力模型的计算基础

Gated DeltaNet（GDN）是混合注意力模型中的关键计算模块，通过门控与递推状态更新处理序列信息。它的执行效率直接影响模型的输入处理与连续生成速度，为采用该架构的 Dense 与 MoE 模型提供计算基础。

LuxiInfer 自研了适配 Hexagon NPU 的 **GDN 高性能融合算子**，围绕三个方向优化：

- 🧩 **融合计算：** 将关键递推计算与状态更新统一执行，减少算子拆分和中间张量搬运。
- ♻️ **复用状态：** 复用中间结果与工作状态，降低重复计算和内存读写开销。
- ⚡ **原生加速：** 结合 Hexagon 向量化与并行执行能力，提高 Prefill 和 Decode 的执行效率。


### MoE：协同优化计算、存储与调度

在 GDN 算子加速的基础上，Qwen3.6-35B-A3B 带来了新的部署挑战：虽然每次只激活部分专家，但完整权重仍需存放在设备上。模型规模增大后，**常驻内存、专家读取与加载等待**成为影响手机端推理的重要因素。

LuxiInfer 将专家存储、缓存管理与 NPU 计算结合起来，保留每层 256 个专家的真实 Top8 路由，通过五项优化降低内存与 I/O 开销：

1. **2-bit 专家量化。** 专家权重采用 `{-7, -2, 2, 7}` 四值码本，以 2-bit 索引压缩存储；执行时在 VTCM 中展开为 4-bit，配合 A8 激活，由 HVX 准备数据、HMX 执行矩阵乘。
2. **按需加载与动态缓存。** 每层使用 LRU 专家缓存，命中时直接复用，缺失时从闪存读取，让完整专家集合按需参与计算，降低常驻内存需求。
3. **Prefill 权重复用。** 采用按层优先（layer-major）调度，同一层连续处理多个 AR128 输入块，并按专家归并 token，减少重复读取、提高矩阵计算利用率。
4. **Decode 读算交叠。** 优先计算命中专家，同时异步读取缺失专家；结合就绪调度与双缓冲，交叠权重搬运和当前计算，减少等待。
5. **跨阶段资源共享。** 融合 Attention 与 Router / Shared，Prefill / Decode 共享常量和常驻 context，并复用专家缓存，减少重复加载与复制。

<a id="contact"></a>

## 🤝 交流与合作

欢迎通过项目 Issues 反馈机型适配、部署问题和性能记录。提交问题时请附手机 / SoC、系统版本、App / 模型版本、关键配置及运行日志。

面向手机、边缘设备与本地 AI 应用，陆兮科技提供模型适配、部署集成与性能优化的技术交流与合作。

- 技术交流与商务合作：[LuxiTech@luxitech.cn](mailto:LuxiTech@luxitech.cn)
- 陆兮科技：[GitHub · LuxiTech](https://github.com/LuxiTech)
- 相关项目：[LuxiChat-App](https://github.com/LuxiTech/LuxiChat-App)

感谢 ExecuTorch、Qualcomm AI 技术栈及 Qwen 开源模型社区。模型与第三方组件的来源、版本及许可说明见对应发布物。
