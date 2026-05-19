#!/usr/bin/env python3
"""
Generate assignment charts for:
  Assignment_Poverty_Inequality_SSNP_Bangladesh.md

Run from the personal/ folder:
  python3 generate_assignment_graphs.py

In Jupyter / Colab / Kaggle: run all cells, or set BASE_DIR below.
Charts save to generated_graphs/ (next to script, or current working directory).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def _base_dir() -> Path:
    """Script directory when run as .py; cwd in notebooks (no __file__)."""
    try:
        return Path(__file__).resolve().parent
    except NameError:
        return Path.cwd()


# Optional: in a notebook, set BASE_DIR = Path("/content/personal") before running
BASE_DIR = _base_dir()
OUT_DIR = BASE_DIR / "generated_graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Presentation colour palette (green / blue / grey theme)
COLOR_PRIMARY = "#2e7d32"
COLOR_SECONDARY = "#1565c0"
COLOR_ACCENT = "#ef6c00"
COLOR_NEUTRAL = "#616161"
COLOR_LIGHT = "#e0e0e0"


def save(fig: plt.Figure, name: str) -> Path:
    path = OUT_DIR / name
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  saved {path.name}")
    return path


def figure1_poverty_glance():
    """Figure 1: National & extreme poverty, 2022 vs 2025."""
    categories = ["National poverty", "Extreme poverty"]
    y2022 = [18.7, 5.6]
    y2025 = [27.9, 9.3]
    x = np.arange(len(categories))
    w = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - w / 2, y2022, w, label="2022", color=COLOR_SECONDARY)
    ax.bar(x + w / 2, y2025, w, label="2025 (proj.)", color="#c62828")
    ax.set_ylabel("Rate (%)")
    ax.set_title("Poverty at a Glance: Bangladesh (2022 vs 2025)")
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 35)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    for bars in ax.containers:
        ax.bar_label(bars, fmt="%.1f%%", padding=2, fontsize=9)
    fig.text(
        0.5,
        0.02,
        "Note: ~62 million people vulnerable to poverty (2025, presentation estimate).",
        ha="center",
        fontsize=8,
        color=COLOR_NEUTRAL,
    )
    return save(fig, "figure1_poverty_glance.png")


def figure2_poverty_trends():
    """Figure 2: Poverty rate bar chart 2010–2025."""
    years = ["2010", "2016", "2022", "2025"]
    rates = [31.5, 24.3, 18.7, 22.9]  # 2025 from trend table; see slide for 27.9%

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(years, rates, color=COLOR_SECONDARY, edgecolor="white", width=0.6)
    bars[-1].set_color(COLOR_ACCENT)
    ax.set_ylabel("Poverty rate (%)")
    ax.set_title("Trends in Poverty in Bangladesh")
    ax.set_ylim(0, 35)
    ax.grid(axis="y", alpha=0.3)
    ax.bar_label(bars, fmt="%.1f%%", padding=2)
    fig.text(
        0.5,
        0.02,
        "2025 bar uses trend-table value (22.9%). Current-situation slide: 27.9%.",
        ha="center",
        fontsize=8,
        color=COLOR_NEUTRAL,
    )
    return save(fig, "figure2_poverty_trends.png")


def figure3_income_inequality():
    """Figure 3: National income shares (2022) + Gini headline."""
    labels = ["Top 10%\n(richest)", "Middle 40%", "Bottom 50%\n(poorest)"]
    sizes = [40.9, 40.05, 19.05]
    colors = ["#c62828", "#fbc02d", COLOR_SECONDARY]

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90,
        textprops={"fontsize": 9},
    )
    axes[0].set_title("Distribution of National Income (2022)")

    gini_years = [2010, 2016, 2022]
    gini_vals = [0.46, 0.48, 0.50]
    axes[1].plot(gini_years, gini_vals, marker="o", color=COLOR_PRIMARY, linewidth=2)
    axes[1].set_title("Gini Coefficient (summary)")
    axes[1].set_ylabel("Gini")
    axes[1].set_ylim(0.44, 0.52)
    axes[1].grid(alpha=0.3)
    for yr, val in zip(gini_years, gini_vals):
        axes[1].annotate(f"{val:.2f}", (yr, val), textcoords="offset points", xytext=(0, 8), ha="center")

    fig.suptitle("Current Income Inequality in Bangladesh", fontsize=12, y=1.02)
    fig.text(
        0.5,
        -0.02,
        "Bottom 10% income share: 1.31% (2022) vs 2.58% (1990–91). "
        "Urban Gini ≈ 0.54; Rural Gini ≈ 0.45. Top 10% wealth share ≈ 58%.",
        ha="center",
        fontsize=8,
        color=COLOR_NEUTRAL,
    )
    fig.tight_layout()
    return save(fig, "figure3_income_inequality.png")


def figure4_gini_trend():
    """Figure 4: Gini line chart 2010–2022."""
    years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
    # interpolate between anchor points for smooth visual
    anchor_x = [2010, 2016, 2022]
    anchor_y = [0.46, 0.48, 0.50]
    gini = np.interp(years, anchor_x, anchor_y)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(years, gini, color=COLOR_SECONDARY, linewidth=2.5, marker="o", markersize=8)
    ax.scatter([2010, 2016, 2022], [0.46, 0.48, 0.50], color=COLOR_SECONDARY, s=80, zorder=5)
    ax.set_xlabel("Year")
    ax.set_ylabel("Gini coefficient")
    ax.set_title("Income Inequality Trend in Bangladesh (Gini Coefficient)")
    ax.set_xlim(2009, 2023)
    ax.set_ylim(0.455, 0.505)
    ax.grid(alpha=0.3)
    for yr, val in zip([2010, 2016, 2022], [0.46, 0.48, 0.50]):
        ax.annotate(f"{val:.2f}", (yr, val), textcoords="offset points", xytext=(0, 10), ha="center")
    return save(fig, "figure4_gini_trend.png")


def figure5_rural_urban():
    """Figure 5: Rural vs urban Gini comparison."""
    areas = ["Rural", "Urban"]
    gini = [0.45, 0.54]
    colors = [COLOR_PRIMARY, COLOR_ACCENT]

    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(areas, gini, color=colors, width=0.5, edgecolor="white")
    ax.set_ylabel("Gini coefficient")
    ax.set_title("Rural vs Urban Income Inequality")
    ax.set_ylim(0.4, 0.6)
    ax.axhline(0.50, color=COLOR_NEUTRAL, linestyle="--", linewidth=1, label="National ~0.50 (2022)")
    ax.bar_label(bars, fmt="%.2f", padding=2)
    ax.legend(loc="upper left")
    ax.grid(axis="y", alpha=0.3)
    fig.text(
        0.5,
        0.02,
        "Rural areas: lower Gini but higher poverty incidence. Urban: higher inequality and rising poverty.",
        ha="center",
        fontsize=8,
        color=COLOR_NEUTRAL,
    )
    return save(fig, "figure5_rural_urban.png")


def figure6_budget_allocation():
    """Figure 6: SSNP budget breakdown (presentation figures)."""
    labels = [
        "Total SSNP\nallocation",
        "Pro-poor\nprogrammes",
        "Other SSNP\n(spend)",
    ]
    # BDT crore
    total = 116731
    pro_poor = 37076
    other = total - pro_poor
    values = [total, pro_poor, other]
    colors = [COLOR_NEUTRAL, COLOR_PRIMARY, COLOR_LIGHT]

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].barh(labels, values, color=colors)
    axes[0].set_xlabel("BDT crore")
    axes[0].set_title("Social Safety Net Spending (FY budget, presentation)")
    for i, v in enumerate(values):
        axes[0].text(v + 2000, i, f"{v:,.0f}", va="center", fontsize=9)

    shares = ["Share of\nnational budget", "Share of\nGDP"]
    pct = [16.8, 3.01]
    axes[1].bar(shares, pct, color=[COLOR_SECONDARY, COLOR_ACCENT], width=0.45)
    axes[1].set_ylabel("Percent (%)")
    axes[1].set_title("SSNP as % of Budget and GDP")
    axes[1].bar_label(axes[1].containers[0], fmt="%.2f%%", padding=2)

    fig.suptitle("Budget Allocation for Social Safety Nets", fontsize=12, y=1.02)
    fig.text(
        0.5,
        -0.02,
        "99 programmes (down from 140); 7.68 crore listed beneficiaries; 39 pro-poor schemes.",
        ha="center",
        fontsize=8,
        color=COLOR_NEUTRAL,
    )
    fig.tight_layout()
    return save(fig, "figure6_budget_allocation.png")


def figure7_international_comparison():
    """Figure 7: Poverty and Gini bars across five countries."""
    countries = ["Bangladesh", "India", "Nepal", "Vietnam", "Thailand"]
    poverty = [19, 22, 25, 6, 7]
    gini = [0.50, 0.36, 0.33, 0.35, 0.44]
    colors = ["#2e7d32", "#1565c0", "#c62828", "#ef6c00", "#6a1b9a"]

    fig, axes = plt.subplots(1, 2, figsize=(11, 5))

    axes[0].bar(countries, poverty, color=colors)
    axes[0].set_ylabel("Poverty rate (%)")
    axes[0].set_title("Poverty Rate Comparison")
    axes[0].tick_params(axis="x", rotation=25)
    axes[0].set_ylim(0, 30)
    axes[0].grid(axis="y", alpha=0.3)
    axes[0].bar_label(axes[0].containers[0], fmt="%d%%", padding=2)

    axes[1].bar(countries, gini, color=colors)
    axes[1].set_ylabel("Gini coefficient")
    axes[1].set_title("Income Inequality (Gini) Comparison")
    axes[1].tick_params(axis="x", rotation=25)
    axes[1].set_ylim(0, 0.6)
    axes[1].grid(axis="y", alpha=0.3)
    axes[1].bar_label(axes[1].containers[0], fmt="%.2f", padding=2)

    fig.suptitle("International Comparison (approx. 2022–23)", fontsize=12, y=1.02)
    fig.text(
        0.5,
        -0.02,
        "Sources cited in presentation: World Bank, ADB, UNDP.",
        ha="center",
        fontsize=8,
        color=COLOR_NEUTRAL,
    )
    fig.tight_layout()
    return save(fig, "figure7_international_comparison.png")


def main():
    print(f"Writing charts to: {OUT_DIR}\n")
    figure1_poverty_glance()
    figure2_poverty_trends()
    figure3_income_inequality()
    figure4_gini_trend()
    figure5_rural_urban()
    figure6_budget_allocation()
    figure7_international_comparison()
    print("\nDone. Update markdown image paths to generated_graphs/ if needed.")


if __name__ == "__main__":
    main()
