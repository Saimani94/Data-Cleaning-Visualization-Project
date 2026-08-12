# Data Cleaning & Visualization Project

An end-to-end Python data analytics project that transforms a messy retail-sales dataset into clean, analysis-ready data and communicates insights through visualizations.

## Objective

- Handle missing values
- Detect and remove duplicate records
- Standardize inconsistent categorical data
- Identify and treat numeric outliers
- Explore trends and performance with Pandas
- Create clear visualizations with Matplotlib and Seaborn
- Document findings for data storytelling

## Dataset

The included `data/raw_sales_data.csv` is a small synthetic retail-sales dataset designed to demonstrate real-world preprocessing. It intentionally contains missing values, duplicate transactions, inconsistent category labels, and numerical outliers.

Columns include transaction date, product category, region, units sold, unit price, discount, and revenue.

## Workflow

1. Load and inspect the raw data.
2. Profile missing values, duplicates, data types, and suspicious values.
3. Clean missing values using field-appropriate rules.
4. Standardize categories and convert dates/numerics to consistent types.
5. Remove duplicate transactions.
6. Detect outliers using the IQR method and cap extreme values to reduce distortion while retaining the records.
7. Recalculate revenue from units, price, and discount.
8. Explore category, regional, and time-based patterns.
9. Build charts for trends, distributions, and comparisons.
10. Save the cleaned dataset and generated figures.
11. Summarize findings in `reports/findings.md`.

## Project Structure

```text
Data-Cleaning-Visualization-Project/
├── data/
│   └── raw_sales_data.csv
├── notebooks/
│   └── data_cleaning_visualization.ipynb
├── reports/
│   └── findings.md
├── src/
│   └── analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies

- Python 3.10+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Run the Project

```bash
pip install -r requirements.txt
python src/analysis.py
```

The script creates `data/cleaned_sales_data.csv` and PNG visualizations in `reports/figures/`.

For interactive exploration, open `notebooks/data_cleaning_visualization.ipynb` in Jupyter Notebook or VS Code.

## Learning Outcomes

This project provides hands-on practice with data preprocessing, exploratory data analysis, outlier handling, visualization, and communicating insights through a reproducible GitHub workflow.

## Submission Checklist

- [x] Raw dataset included
- [x] Missing values handled
- [x] Duplicates handled
- [x] Outliers identified and treated
- [x] Pandas preprocessing implemented
- [x] Matplotlib/Seaborn visualizations included
- [x] Findings report included
- [x] Reproducible project structure included

## Author

Saimani94
