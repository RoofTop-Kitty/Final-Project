"""Utility script that recreates a few key visuals from the HR attrition notebook.

Running this module saves PNG files under `assets/` so the README can embed
up-to-date images without opening the full notebook.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "hrdb2.xlsx"
ASSETS_DIR = PROJECT_ROOT / "assets"


def load_data() -> pd.DataFrame:
    """Load and merge the two HR data sheets, mirroring the notebook logic."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Expected dataset at {DATA_PATH}")

    df_main = pd.read_excel(DATA_PATH, sheet_name="1")
    df_attr = pd.read_excel(DATA_PATH, sheet_name="2")
    df = df_main.merge(df_attr, on="EmployeeNumber", how="left")
    df.columns = df.columns.str.strip()
    df["Attrition_Flag"] = (df["Attrition"].astype(str).str.strip() == "Yes").astype(int)
    return df


def plot_attrition_by_department(df: pd.DataFrame) -> None:
    summary = (
        df.groupby("Department", observed=False)["Attrition_Flag"]
        .mean()
        .sort_values(ascending=True)
        * 100
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.barh(summary.index, summary.values, color="#c94c4c")
    ax.set_title("Attrition Rate by Department (%)")
    ax.set_xlabel("Attrition Rate (%)")
    ax.set_xlim(0, max(summary.values) * 1.15)

    for bar, pct in zip(bars, summary.values, strict=False):
        ax.text(
            pct + 0.5,
            bar.get_y() + bar.get_height() / 2,
            f"{pct:.1f}%",
            va="center",
            fontsize=10,
        )

    fig.tight_layout()
    fig.savefig(ASSETS_DIR / "attrition_by_department.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_attrition_by_tenure(df: pd.DataFrame) -> None:
    bins = [0, 1, 3, 5, 10, 20, np.inf]
    labels = ["<1 yr", "1-2 yrs", "3-4 yrs", "5-9 yrs", "10-19 yrs", "20+ yrs"]
    df = df.copy()
    df["TenureBucket"] = pd.cut(
        df["YearsAtCompany"], bins=bins, labels=labels, right=False, include_lowest=True
    )

    summary = (
        df.groupby("TenureBucket", observed=False)["Attrition_Flag"]
        .mean()
        .reindex(labels)
        * 100
    )

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(summary.index, summary.values, color="#4c72b0")
    ax.set_title("Attrition Rate by Tenure Bucket (%)")
    ax.set_ylabel("Attrition Rate (%)")
    ax.set_ylim(0, max(summary.values) * 1.2)

    for bar, pct in zip(bars, summary.values, strict=False):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            pct + 0.5,
            f"{pct:.1f}%",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    fig.tight_layout()
    fig.savefig(ASSETS_DIR / "attrition_by_tenure.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_attrition_by_distance(df: pd.DataFrame) -> None:
    bins = [0, 2, 5, 10, 15, 20, 30, np.inf]
    labels = ["0-1 km", "2-4 km", "5-9 km", "10-14 km", "15-19 km", "20-29 km", "30+ km"]
    df = df.copy()
    df["DistanceBucket"] = pd.cut(
        df["DistanceFromHome"], bins=bins, labels=labels, right=False, include_lowest=True
    )
    summary = (
        df.groupby("DistanceBucket", observed=False)["Attrition_Flag"]
        .mean()
        .reindex(labels)
        * 100
    )

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(summary.index, summary.values, color="#dd8452")
    ax.set_title("Attrition Rate by Commute Distance (%)")
    ax.set_ylabel("Attrition Rate (%)")
    ax.set_ylim(0, max(summary.values) * 1.2)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
        tick.set_ha("right")

    for bar, pct in zip(bars, summary.values, strict=False):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            pct + 0.5,
            f"{pct:.1f}%",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    fig.tight_layout()
    fig.savefig(ASSETS_DIR / "attrition_by_commute.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ASSETS_DIR.mkdir(exist_ok=True)
    df = load_data()
    plot_attrition_by_department(df)
    plot_attrition_by_tenure(df)
    plot_attrition_by_distance(df)
    print("Saved README visuals to", ASSETS_DIR)


if __name__ == "__main__":
    main()

