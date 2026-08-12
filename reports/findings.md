# Findings Report

## Data Quality Findings

The raw dataset was intentionally designed to contain common data-quality problems found in practical analytics work.

- Missing `units_sold` was filled with the median because sales quantity is numeric and a median is less sensitive to extreme values.
- Missing `discount` was filled with the median discount.
- Category and region labels were trimmed and standardized to title case, resolving values such as `electronics` and `south`.
- Duplicate transaction IDs were removed, keeping the first occurrence.
- An extreme `units_sold` value was identified with the 1.5×IQR rule and capped rather than deleting the transaction.
- Revenue was recalculated from cleaned units, price, and discount so the derived metric remains internally consistent.

## Analysis Questions

The project investigates:

1. Which product categories contribute the most revenue?
2. Which regions generate the highest revenue?
3. How does revenue change over time?
4. How widely do sales quantities vary across categories?

## Visual Report

Running `python src/analysis.py` generates four charts in `reports/figures/`:

- `monthly_revenue.png` — revenue trend by month
- `revenue_by_category.png` — category-level revenue comparison
- `revenue_by_region.png` — regional revenue comparison
- `units_distribution.png` — sales quantity distribution by category

## Interpretation

Because this repository uses a synthetic teaching dataset, the charts are intended to demonstrate the analytical workflow rather than represent real business performance. The most important learning outcome is the reasoning process: inspect the raw data, apply explainable cleaning rules, validate the cleaned output, visualize patterns, and communicate limitations clearly.

## Conclusion

A reliable visualization starts with reliable data. Cleaning missing values, duplicates, inconsistent labels, and outliers before aggregation prevents misleading conclusions and makes the analysis easier to reproduce and explain.
