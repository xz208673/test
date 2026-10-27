"""Render the README's 4K-context GDN comparisons from gdn-performance.csv.

Requires matplotlib and a Chinese font, such as Noto Sans CJK.
Run: python assets/plot_gdn_performance.py
"""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, Patch
import numpy as np


ROOT = Path(__file__).resolve().parent
BRAND = "#6c5ce7"
REFERENCE = "#cfd4df"
TEXT = "#253148"
SECONDARY = "#728096"
BLUE = "#486bf2"


def configure_fonts():
    names = {font.name for font in font_manager.fontManager.ttflist}
    candidates = [
        "Noto Sans CJK SC",
        "Noto Sans CJK JP",
        "Microsoft YaHei",
        "PingFang SC",
        "WenQuanYi Micro Hei",
    ]
    selected = next((name for name in candidates if name in names), None)
    if selected is None:
        raise RuntimeError("Install a Chinese font, such as Noto Sans CJK.")
    plt.rcParams.update({
        "font.family": selected,
        "font.size": 12,
        "axes.unicode_minus": False,
        "svg.fonttype": "path",
        "hatch.linewidth": 0.55,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })


def plot_platform(platform, rows):
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.45))
    fig.subplots_adjust(left=0.075, right=0.95, bottom=0.22, top=0.68, wspace=0.29)
    platform_name = {
        "SM8750": "Snapdragon 8 Elite",
        "SM8850": "Snapdragon 8 Elite Gen 5",
    }[platform]
    fig.suptitle(
        f"4K 上下文推理速度对比 · {platform}",
        y=0.965, fontsize=20, fontweight="bold", color=TEXT,
    )
    fig.text(0.5, 0.888, f"NPU · {platform_name}", ha="center", fontsize=13, color=SECONDARY)
    fig.legend(
        handles=[
            Patch(facecolor=BRAND, edgecolor="white", hatch="....", label="陆兮科技 LuxiInfer"),
            Patch(facecolor=REFERENCE, edgecolor=REFERENCE, label="高通官方"),
        ],
        loc="upper center", bbox_to_anchor=(0.5, 0.855), ncol=2,
        frameon=False, fontsize=12, handlelength=1.4, columnspacing=2.1,
    )

    x = np.arange(len(rows), dtype=float)
    width = 0.27
    for ax, metric, title, maximum, ticks in [
        (axes[0], "prefill", "输入处理速度（Prefill）", 2200, [0, 500, 1000, 1500, 2000]),
        (axes[1], "decode", "连续生成速度（Decode）", 110, [0, 25, 50, 75, 100]),
    ]:
        frame = FancyBboxPatch(
            (-0.115, -0.225), 1.175, 1.42,
            boxstyle="round,pad=0.018,rounding_size=0.025",
            transform=ax.transAxes, clip_on=False, facecolor="white",
            edgecolor="#e1e6ef", linewidth=1.1, zorder=-20,
        )
        ax.add_patch(frame)
        ours = [float(row[f"{metric}_luxiinfer"]) for row in rows]
        reference = [float(row[f"{metric}_reference"]) for row in rows]
        bars = ax.bar(x - width / 2, ours, width, color=BRAND, edgecolor="white", hatch="....", linewidth=0, zorder=3)
        refs = ax.bar(x + width / 2, reference, width, color=REFERENCE, linewidth=0, zorder=3)
        for bar, value in zip(bars, ours):
            ax.text(bar.get_x() + width / 2, value + maximum * 0.025, f"{value:.2f}", ha="center", va="bottom", fontsize=12, color=TEXT, fontweight="bold")
        for bar, row, value in zip(refs, rows, reference):
            ax.text(bar.get_x() + width / 2, value + maximum * 0.025, row[f"{metric}_reference"], ha="center", va="bottom", fontsize=12, color="#606b7c")
        for index, (ours_value, reference_value) in enumerate(zip(ours, reference)):
            y = max(ours_value, reference_value) + maximum * 0.113
            ax.annotate(
                "", xy=(index - width / 2 - 0.02, y), xytext=(index + width / 2 + 0.02, y),
                arrowprops={"arrowstyle": "<->", "lw": 1.15, "color": BLUE},
            )
            ax.text(
                index, y + maximum * 0.022, f"{ours_value / reference_value:.2f}×",
                ha="center", va="bottom", fontsize=14, color=BLUE, fontweight="bold",
                bbox={"boxstyle": "round,pad=0.15", "facecolor": "#f2f5ff", "edgecolor": "none"},
            )
        ax.set_title(title, pad=19, color=TEXT, fontsize=14)
        ax.set_ylim(0, maximum)
        ax.set_yticks(ticks)
        ax.set_xlim(-0.6, len(rows) - 0.4)
        ax.set_xticks(x, [f"Qwen3.5-{row['model']}" for row in rows])
        ax.set_ylabel("token/s", color=SECONDARY, fontsize=11, labelpad=9)
        ax.tick_params(axis="both", length=0, colors=SECONDARY, labelsize=11, pad=7)
        ax.tick_params(axis="x", colors=TEXT, labelsize=12)
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color("#d9dfea")
        ax.yaxis.grid(True, color="#edf0f5", linewidth=0.8, zorder=-5)
        ax.set_axisbelow(True)

    fig.text(0.5, 0.065, "倍数 = LuxiInfer ÷ 高通官方   ·   数值越高越好", ha="center", fontsize=11, color=SECONDARY)
    for extension in ("png", "svg"):
        fig.savefig(ROOT / f"gdn-performance-{platform.lower()}.{extension}", dpi=180)
    plt.close(fig)


def main():
    configure_fonts()
    with (ROOT / "gdn-performance.csv").open(newline="") as source:
        data = list(csv.DictReader(source))
    for platform in ("SM8750", "SM8850"):
        plot_platform(platform, [row for row in data if row["platform"] == platform])


if __name__ == "__main__":
    main()
