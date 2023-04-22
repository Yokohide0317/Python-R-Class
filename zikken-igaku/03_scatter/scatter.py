#%%
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
mpl.rcParams["figure.dpi"] = 300
sns.set(style="ticks")

# %%
data_file = "./data/41467_2022_31113_MOESM16_ESM.xlsx"
df = pd.read_excel(data_file,
                   sheet_name="Fig.1a",
                   usecols="A:F",
                   index_col=0)
df

# %%
color_map = {"BS": "b", "RS": "g",
             "RE": "pink", "VE": "r",
             "SE": "y", "LE": "palegreen",
             "P": "skyblue"}
style_map = {"CK": "o", "NPK": "^", "NPKM": "s"}
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
sns.scatterplot(data=df, x="x", y="y",
                hue="Compartments",
                style="Treatment",
                palette=color_map,
                markers=style_map,
                ax=ax)

ax.legend(bbox_to_anchor=(1.3,1))
ax.set_xlabel("PCoA 1(41.32%)")
ax.set_ylabel("PCoA 2(22.03%)")
sns.despine()

# %%
data_file = "./data/41467_2022_35319_MOESM4_ESM.xlsx"
df1 = pd.read_excel(data_file, skiprows=3,
                    sheet_name="Fig. 4a")
df2 = pd.read_excel(data_file, skiprows=3,
                    sheet_name="Fig. 4b")
df1

# %%
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121)

# Fig.4a
sns.scatterplot(data=df1,
                x="UMAP1", y="UMAP2",
                hue="cluster_labels",
                ec="none", legend=False,
                alpha=0.5, s=12, ax=ax1)

for label in df1["cluster_labels"].unique():
    coord = df1[df1["cluster_labels"] == label].iloc[:, :2].mean(axis=0)

    ax1.text(*coord, label,
             fontsize=12, ha="center",
             bbox={"boxstyle": "round",
                   "ec": "k", "fc": "w",
                   "alpha": .3},
            )

sns.despine(left=True, bottom=True)
ax1.tick_params(axis="both", which="both",
                   labelbottom=False, bottom=False,
                   labelleft=False, left=False)

# %%
fig = plt.figure(figsize=(12, 6))
ax2 = fig.add_subplot(121)

sns.scatterplot(
    data=df2[df2["IL17A_label"] == "IL17A"],
    x="UMAP1", y="UMAP2", label="$IL17^+$ cells",
    zorder=2, color="blue",
    alpha=1.0, s=14, ax=ax2
)
sns.scatterplot(
    data=df2[df2["IL17A_label"] == "Others"],
    x="UMAP1", y="UMAP2", label="$IL17^-$ cells",
    zorder=1, color="gray",
    alpha=0.3, s=14, ax=ax2
)
sns.despine(left=True, bottom=True)
ax2.tick_params(axis="both", which="both",
                labelbottom=False, bottom=False,
                labelleft=False, left=False)

# %%
df = pd.read_excel(data_file,
                   skiprows=3,
                   sheet_name="Fig. 4c")
df["-log10FDR"] = -np.log10(df["padj"])

df["Class"] = ["n.a."] * len(df)
df.loc[(df["log2fc"].abs() >= 1) &
       (df["padj"] <= 0.05),
       "Class"] = "FDR <= 0.05; log2FC >= 1"
df.loc[(df["log2fc"].abs() < 1) &
       (df["padj"] > 0.05),
       "Class"] = "FDR > 0.05; log2FC < 1"
df.loc[(df["log2fc"].abs() >= 1) &
       (df["padj"] > 0.05),
       "Class"] = "FDR > 0.05; log2FC >= 1"
df.loc[(df["log2fc"].abs() < 1) &
       (df["padj"]<= 0.05),
       "Class"] = "FDR <= 0.05; log2FC < 1"

fig = plt.figure(figsize=(3,3))
ax = fig.add_subplot(111)

sns.scatterplot(data=df,
                x="log2fc", y="-log10FDR",
                hue="Class", ec="none",
                s=1, ax=ax,
                palette=["r", "orange", "gray", "b"])
ax.axvline(x=1, ls="--", lw=.5, c="k")
ax.axvline(x=-1, ls="--", lw=.5, c="k")
ax.axhline(y=-np.log10(0.05),
           ls="--", lw=.5, c="k")
ax.text(30, -np.log10(0.05),
        "5% FDR", fontsize=6,
        va="bottom")

gene = df[df["gene_symbol"] == "IL17F"]
ax.annotate("IL17F",
            xy=(gene["log2fc"],
                gene["-log10FDR"]),
            xycoords="data", xytext=(20,25),
            arrowprops={"fc": "k", "shrink": .05,
            "width": 2,
            "headwidth": 5,
            "headlength": 5},
            ha="left", va="top",
            fontsize=5)
ax.legend(loc="upper left", fontsize=5)
ax.set_xlim(-40, 40)
ax.set_ylim(0, 35)
sns.despine()
# %%
