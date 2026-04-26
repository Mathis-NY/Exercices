# 1. IMPORTS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")

print("=" * 60)
print("  ESG & Financial Performance Analysis")
print("=" * 60)

# 2. DATA IMPORT

FILE_PATH = "company_esg_financial_dataset.csv"

df = pd.read_csv(FILE_PATH)
print(f"\n[Data Import] Dataset loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(df.head(3).to_string())

# 3. VARIABLES & ARITHMETIC EXPRESSIONS

total_companies   = df["CompanyID"].nunique()
total_years       = df["Year"].nunique()
avg_esg           = round(df["ESG_Overall"].mean(), 2)
avg_revenue       = round(df["Revenue"].mean() / 1e9, 2)   # in billions
avg_profit_margin = round(df["ProfitMargin"].mean(), 2)
esg_revenue_corr  = round(df["ESG_Overall"].corr(df["Revenue"]), 4)

print("\n[Key Metrics]")
print(f"  Total unique companies : {total_companies}")
print(f"  Years covered          : {df['Year'].min()} – {df['Year'].max()} ({total_years} years)")
print(f"  Average ESG Score      : {avg_esg}")
print(f"  Average Revenue        : ${avg_revenue}B")
print(f"  Average Profit Margin  : {avg_profit_margin}%")
print(f"  ESG ↔ Revenue corr.    : {esg_revenue_corr}")

# 4. DATA CLEANING & PREPARATION

print("\n[Data Cleaning]")
print(f"  Missing values before: {df.isnull().sum().sum()}")

df["GrowthRate"] = df.groupby("Industry")["GrowthRate"].transform(
    lambda x: x.fillna(x.median())
)

df["ESG_Tier"] = df["ESG_Overall"].apply(
    lambda score: "High" if score >= 70 else ("Medium" if score >= 50 else "Low")
)

print(f"  Missing values after : {df.isnull().sum().sum()}")
print(f"  ESG Tier distribution:\n{df['ESG_Tier'].value_counts().to_string()}")

# 5. PYTHON FUNDAMENTALS – Lists & Dictionaries

industries = list(df["Industry"].unique())
industries.sort()

industry_stats = {}

print("\n[Industry Loop] Average ESG score per industry:")
for industry in industries:                          # for-loop
    subset      = df[df["Industry"] == industry]
    avg_esg_i   = round(subset["ESG_Overall"].mean(), 2)
    avg_rev_i   = round(subset["Revenue"].mean() / 1e9, 2)
    industry_stats[industry] = {
        "avg_esg": avg_esg_i,
        "avg_revenue_B": avg_rev_i,
        "n_records": len(subset)
    }
    label = "✓ Above Average ESG" if avg_esg_i >= avg_esg else "✗ Below Average ESG"
    print(f"  {industry:<20} ESG={avg_esg_i:>5}  Revenue=${avg_rev_i:>7.2f}B  {label}")

# 6. PANDAS – Series & DataFrames

print("\n[Descriptive Statistics]")
numeric_cols = ["Revenue","ProfitMargin","MarketCap","ESG_Overall",
                "ESG_Environmental","ESG_Social","ESG_Governance",
                "CarbonEmissions","GrowthRate"]
print(df[numeric_cols].describe().round(2).to_string())

esg_means = df[["ESG_Environmental","ESG_Social","ESG_Governance"]].mean()
print("\n[ESG Sub-score Means (Series)]")
print(esg_means.round(2))

# 7. DATA AGGREGATION – groupby & pivot table

print("\n[Aggregation 1] Mean ESG & Revenue by Industry")
agg_industry = df.groupby("Industry").agg(
    Avg_ESG       = ("ESG_Overall",  "mean"),
    Avg_Revenue_B = ("Revenue",      lambda x: x.mean() / 1e9),
    Avg_Margin    = ("ProfitMargin", "mean"),
    Count         = ("CompanyID",    "count")
).round(2)
print(agg_industry.to_string())

print("\n[Aggregation 2] Mean ESG by Region & Year (pivot)")
pivot = df.pivot_table(
    values  = "ESG_Overall",
    index   = "Region",
    columns = "Year",
    aggfunc = "mean"
).round(1)
print(pivot.to_string())

print("\n[Aggregation 3] ESG Tier impact on Profit Margin")
tier_agg = df.groupby("ESG_Tier")[["ProfitMargin","Revenue","MarketCap"]].mean().round(2)
tier_agg["Revenue_B"] = (tier_agg["Revenue"] / 1e9).round(2)
print(tier_agg.drop(columns="Revenue").to_string())

# 8. LINEAR REGRESSION – ESG Score → Profit Margin

print("\n" + "=" * 60)
print("  LINEAR REGRESSION: ESG Score → Profit Margin")
print("=" * 60)

X = df[["ESG_Overall", "ESG_Environmental", "ESG_Social", "ESG_Governance",
        "CarbonEmissions", "GrowthRate", "Revenue"]].copy()
y = df["ProfitMargin"].copy()

mask  = X.notna().all(axis=1) & y.notna()
X, y  = X[mask], y[mask]

X["Revenue"]        = np.log1p(X["Revenue"])
X["CarbonEmissions"]= np.log1p(X["CarbonEmissions"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2   = round(r2_score(y_test, y_pred), 4)
rmse = round(np.sqrt(mean_squared_error(y_test, y_pred)), 4)

print(f"\n  R² Score : {r2}")
print(f"  RMSE     : {rmse}")
print("\n  Coefficients:")
for feat, coef in zip(X.columns, model.coef_):
    print(f"    {feat:<22} : {coef:+.4f}")
print(f"  Intercept               : {model.intercept_:+.4f}")

# 9. VISUALIZATIONS

plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("ESG & Financial Performance Dashboard", fontsize=16, fontweight="bold")

ax = axes[0, 0]
esg_by_ind = agg_industry["Avg_ESG"].sort_values()
bars = ax.barh(esg_by_ind.index, esg_by_ind.values, color="#4C72B0")
ax.axvline(avg_esg, color="red", linestyle="--", label=f"Overall avg ({avg_esg})")
ax.set_title("Avg ESG Score by Industry")
ax.set_xlabel("ESG Score")
ax.legend(fontsize=8)

ax = axes[0, 1]
tier_order = ["High", "Medium", "Low"]
data_box   = [df[df["ESG_Tier"] == t]["ProfitMargin"].dropna() for t in tier_order]
bp = ax.boxplot(data_box, labels=tier_order, patch_artist=True,
                boxprops=dict(facecolor="#4C72B0", alpha=0.6),
                medianprops=dict(color="red", linewidth=2))
ax.set_title("Profit Margin by ESG Tier")
ax.set_ylabel("Profit Margin (%)")

ax = axes[0, 2]
esg_time = df.groupby("Year")["ESG_Overall"].mean()
ax.plot(esg_time.index, esg_time.values, marker="o", color="#55A868", linewidth=2)
ax.set_title("Avg ESG Score Over Time (2015–2025)")
ax.set_xlabel("Year")
ax.set_ylabel("ESG Score")
ax.xaxis.set_major_locator(mticker.MultipleLocator(2))

ax = axes[1, 0]
sample = df.sample(500, random_state=1)
ax.scatter(sample["ESG_Overall"], sample["Revenue"] / 1e9,
           alpha=0.4, color="#C44E52", s=20)
ax.set_title("ESG Score vs Revenue (sample n=500)")
ax.set_xlabel("ESG Overall Score")
ax.set_ylabel("Revenue (Billions $)")

ax = axes[1, 1]
ax.scatter(y_test[:300], y_pred[:300], alpha=0.4, color="#8172B2", s=20)
lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
ax.plot(lims, lims, "r--", linewidth=1.5, label="Perfect fit")
ax.set_title(f"Regression: Actual vs Predicted\n(R²={r2}, RMSE={rmse})")
ax.set_xlabel("Actual Profit Margin (%)")
ax.set_ylabel("Predicted Profit Margin (%)")
ax.legend(fontsize=8)

ax = axes[1, 2]
rev_tier = df.groupby("ESG_Tier")["Revenue"].mean().reindex(["Low","Medium","High"]) / 1e9
ax.bar(rev_tier.index, rev_tier.values,
       color=["#C44E52","#CCB974","#4C72B0"])
ax.set_title("Avg Revenue by ESG Tier")
ax.set_xlabel("ESG Tier")
ax.set_ylabel("Revenue (Billions $)")

plt.tight_layout()
plt.savefig("esg_dashboard.png", dpi=150, bbox_inches="tight")
plt.close()
print("\n[Visualizations] Dashboard saved → esg_dashboard.png")

# 10. SUMMARY REPORT

print("\n" + "=" * 60)
print("  FINAL SUMMARY")
print("=" * 60)
print(f"  Dataset       : {total_companies} companies, {total_years} years (2015–2025)")
print(f"  Mean ESG      : {avg_esg}  |  High-tier share: "
      f"{(df['ESG_Tier']=='High').mean()*100:.1f}%")
print(f"  Regression R² : {r2}  — ESG & financial vars explain "
      f"{r2*100:.1f}% of Profit Margin variance")

top_esg_ind = agg_industry["Avg_ESG"].idxmax()
low_esg_ind = agg_industry["Avg_ESG"].idxmin()
print(f"  Highest ESG industry : {top_esg_ind} ({agg_industry.loc[top_esg_ind,'Avg_ESG']})")
print(f"  Lowest  ESG industry : {low_esg_ind} ({agg_industry.loc[low_esg_ind,'Avg_ESG']})")
print("\n  Analysis complete.")
