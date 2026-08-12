from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw_sales_data.csv"
CLEAN_PATH = ROOT / "data" / "cleaned_sales_data.csv"
FIG_DIR = ROOT / "reports" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def cap_outliers_iqr(series: pd.Series) -> pd.Series:
    """Cap extreme values using the 1.5*IQR rule while retaining rows."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series.clip(lower=lower, upper=upper)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["category"] = df["category"].astype("string").str.strip().str.title()
    df["region"] = df["region"].astype("string").str.strip().str.title()

    numeric_cols = ["units_sold", "unit_price", "discount", "revenue"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Fill missing values with transparent, reproducible rules.
    df["units_sold"] = df["units_sold"].fillna(df["units_sold"].median())
    df["discount"] = df["discount"].fillna(df["discount"].median())
    df["category"] = df["category"].fillna("Unknown")
    df["region"] = df["region"].fillna("Unknown")

    # Remove exact duplicate transactions using the transaction ID.
    df = df.drop_duplicates(subset=["transaction_id"], keep="first")

    # Cap extreme sales quantities rather than deleting the transaction.
    df["units_sold"] = cap_outliers_iqr(df["units_sold"])

    # Recalculate revenue from cleaned business inputs.
    df["revenue"] = df["units_sold"] * df["unit_price"] * (1 - df["discount"])
    df["month"] = df["date"].dt.to_period("M").astype(str)

    return df


def create_visualizations(df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(9, 5))
    monthly = df.groupby("month", as_index=False)["revenue"].sum()
    sns.lineplot(data=monthly, x="month", y="revenue", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "monthly_revenue.png", dpi=160)
    plt.close()

    plt.figure(figsize=(9, 5))
    category = df.groupby("category", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    sns.barplot(data=category, x="category", y="revenue")
    plt.title("Revenue by Product Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "revenue_by_category.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 5))
    region = df.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    sns.barplot(data=region, x="region", y="revenue")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "revenue_by_region.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="category", y="units_sold")
    plt.title("Units Sold Distribution by Category")
    plt.xlabel("Category")
    plt.ylabel("Units Sold")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "units_distribution.png", dpi=160)
    plt.close()


def main() -> None:
    raw = pd.read_csv(RAW_PATH)
    print("Raw shape:", raw.shape)
    print("Missing values before cleaning:\n", raw.isna().sum())
    print("Duplicate transaction IDs:", raw["transaction_id"].duplicated().sum())

    cleaned = clean_data(raw)
    cleaned.to_csv(CLEAN_PATH, index=False)
    create_visualizations(cleaned)

    print("Cleaned shape:", cleaned.shape)
    print("Total revenue: {:.2f}".format(cleaned["revenue"].sum()))
    print("Cleaned dataset saved to:", CLEAN_PATH)
    print("Figures saved to:", FIG_DIR)


if __name__ == "__main__":
    main()
