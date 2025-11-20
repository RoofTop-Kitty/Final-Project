"""Quick helper to dump headline attrition statistics for the README narrative."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from generate_readme_images import load_data


def main() -> None:
    df = load_data()

    dept = (
        df.groupby("Department", observed=False)["Attrition_Flag"]
        .mean()
        .sort_values(ascending=False)
        * 100
    )
    tenure_bins = [0, 1, 3, 5, 10, 20, float("inf")]
    tenure_labels = ["<1 yr", "1-2 yrs", "3-4 yrs", "5-9 yrs", "10-19 yrs", "20+ yrs"]
    df["TenureBucket"] = pd.cut(
        df["YearsAtCompany"],
        bins=tenure_bins,
        labels=tenure_labels,
        right=False,
        include_lowest=True,
    )
    tenure = (
        df.groupby("TenureBucket", observed=False)["Attrition_Flag"]
        .mean()
        .reindex(tenure_labels)
        * 100
    )

    distance_bins = [0, 2, 5, 10, 15, 20, 30, float("inf")]
    distance_labels = ["0-1 km", "2-4 km", "5-9 km", "10-14 km", "15-19 km", "20-29 km", "30+ km"]
    df["DistanceBucket"] = pd.cut(
        df["DistanceFromHome"],
        bins=distance_bins,
        labels=distance_labels,
        right=False,
        include_lowest=True,
    )
    distance = (
        df.groupby("DistanceBucket", observed=False)["Attrition_Flag"]
        .mean()
        .reindex(distance_labels)
        * 100
    )

    print("Attrition by Department (%):")
    print(dept.round(1))
    print("\nAttrition by Tenure (%):")
    print(tenure.round(1))
    print("\nAttrition by Commute Distance (%):")
    print(distance.round(1))


if __name__ == "__main__":
    main()

