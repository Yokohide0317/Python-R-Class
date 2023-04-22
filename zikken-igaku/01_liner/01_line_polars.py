#%%
%matplotlib inline
import polars as pl
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

# %%
data_url = "./data/41586_2022_5354_MOESM5_ESM.xlsx"
df = pl.read_excel(data_url,
                   sheet_name="Fig.3g BLI",
                   read_csv_options={"has_header": True, 
                                     "columns": [0,1,2,3,4],},
                   )
df.head()
# %%
conc_to_colors = {"600 nM": "lavender",
                  "300 nM": "lightskyblue",
                  "150 nM": "lightsteelblue",
                  "75 nM": "lightslategray"}

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)

for conc in df.columns[1:]:
    ax.plot(df["WT"], df[conc],
            label=conc,
            color=conc_to_colors[conc])

    ax.legend(loc="lower right", prop={"size": 9})
    ax.set_xlabel("Time (s)", fontsize=12)
    ax.set_ylabel("STLING response (nm)",
                  fontsize=12)
    sns.despine()

# %%
data_url = "./data/41467_2022_32521_MOESM10_ESM.xlsx"

df = pl.read_excel(data_url,
                   sheet_name="Figure1",
                   read_csv_options={"has_header": True,
                                     "columns": list(range(1, 20)),
                                     "skip_rows": 1,
                                     "n_rows": 7,
                                     },
                   )
df = df.with_columns(
    pl.col("*").exclude("Days").cast(pl.Float64),
    pl.col("Days").cast(pl.Int32),
)
df
# %%
labels = (["Days"] +
          [f"Glu_{x}" for x in range(6)] +
          [f"Lac_{x}" for x in range(6)] +
          [f"Unt_{x}" for x in range(6)]
          )
df = df.rename(dict(zip(df.columns, labels)))
# %%
df = (df.melt(id_vars=["Days"], value_name="Total volume",)
      .with_columns(
        pl.col("variable").str.replace(r"_.*$", "")
            .alias("Treatment regimen"),
        pl.col("variable").str.replace(r"^.*_", "Replicate")
            .alias("Replicates"),
    )).drop(["variable"])
df

# %%
fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)
sns.pointplot(data=df.to_pandas(),
              x="Days", y="Total volume",
              hue="Treatment regimen",
              palette=["Skyblue", "Orange", "Gray"],
              markers=["d", "v", "o"],
              linestyles=["-", "-", ":"],
              errorbar="se",
              capsize=0.3, errwidth=1.0,
              ax=ax)
ax.legend()
ax.set_ylabel(r"Total volume ($mm^3$)")
sns.despine()
# %%
