from matplotlib import ticker
import statsmodels.api as sm

def describe_missing(df, mask, label, cols=None, check_fatal=True):
    if cols is None:
        cols = ["iyear", "attacktype1_txt", "nkill", "success", "targtype1_txt", "nperps", "country_txt"]
    subset = df[mask]
    rate = len(subset) / len(df) * 100
    success = subset[subset["success"] == 1]
    success_rate = len(success) / len(subset) * 100 if len(success) else 0
    if check_fatal:
        if len(success):
            successes_with_fatalities = success[success["nkill"] > 0]
            fatalities_rate = len(successes_with_fatalities) / len(success) * 100
        else:
            successes_with_fatalities = success.iloc[0:0]
            fatalities_rate = 0
    lines = [
        f"{label}: {rate:.2f}% of dataset"
        f", {success_rate:.2f}% successful attacks rate"
    ]
    if check_fatal:
        lines.append(f", {fatalities_rate:.2f}% with fatal casualties among successful")
    print("".join(lines))
    print(subset[cols].head(5).tail(5))
    return subset

def fmt_axis(ax, axis="y", kind="int"):
    fmt = {
        "int": ticker.StrMethodFormatter("{x:,.0f}"),
        "pct": ticker.PercentFormatter(decimals=0),
    }[kind]
    (ax.yaxis if axis == "y" else ax.xaxis).set_major_formatter(fmt)

def fit_ols(df, y, x):
    data = df[[x, y]].dropna()
    results = sm.OLS(data[y], sm.add_constant(data[x])).fit()
    print(f"n = {len(data)}")
    print(results.summary())
    return results