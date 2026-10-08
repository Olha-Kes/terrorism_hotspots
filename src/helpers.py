from matplotlib import ticker
import statsmodels.api as sm
import seaborn as sns
from cycler import cycler

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

def set_theme(normal=True):
    BG, FG, ACCENT = "#16181a", "#a0aab2", "#e65100"
    PALETTE_NORMAL = [ACCENT, "#eb7a2e", "#f29e6d", "#f7cbaf", "#fcf2eb", "#e5dfdc"]

    if isinstance(normal, bool):
        palette_set = PALETTE_NORMAL if normal else PALETTE_NORMAL[::-1]
    else:
        palette_set = normal

    sns.set_theme(style="dark", rc={
        "figure.dpi": 150,
        "figure.facecolor": BG,
        "axes.facecolor": BG,
        "savefig.facecolor": BG,
        "text.color": FG,
        "axes.labelcolor": FG,
        "axes.titlecolor": "white",
        "xtick.color": FG,
        "ytick.color": FG,
        "xtick.labelsize": 9,
        "xtick.labelsize": 9,
        "axes.spines.left": False,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.spines.bottom": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": "#ffffff",
        "grid.alpha": 0.2,
        "grid.linestyle": "--",
        "axes.prop_cycle": cycler(color=palette_set),
    })

def prepare_stacked_data(wide_df, accent_palette=None, other_labels=None):
    if accent_palette is None:
        accent_palette = ["#f7cbaf", "#f29e6d", "#eb7a2e", "#e65100"]
    if other_labels is None:
        other_labels = ["Other"]
    active_others = [col for col in other_labels if col in wide_df.columns]
    regular_cols = [col for col in wide_df.columns if col not in active_others]

    sorted_regular = wide_df[regular_cols].sum().sort_values(ascending=False).index.tolist()

    final_order = sorted_regular + active_others
    wide_sorted = wide_df[final_order]

    color_mapping = {}

    for i, col in enumerate(sorted_regular):
        color_mapping[col] = accent_palette[i % len(accent_palette)]

    gray_palette = ["#fcf2eb", "#e5dfdc"]
    for i, col in enumerate(active_others):
        color_mapping[col] = gray_palette[i % len(gray_palette)]

    colors_list = [color_mapping[col] for col in final_order]

    return wide_sorted, colors_list

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