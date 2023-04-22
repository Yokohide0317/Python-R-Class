#%%
%matplotlib inline
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
mpl.rcParams["figure.dpi"]
sns.set(style="ticks")

#%%
#data_url = "https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-022-05354-0/MediaObjects/41586_2022_5354_MOESM5_ESM.xlsx"
data_url = "./data/41586_2022_5354_MOESM5_ESM.xlsx"
df = pd.read_excel(data_url,
                   sheet_name="Fig.3g BLI",
                   usecols="A:E",
                   index_col=0)
df.head()
# %%
conc_to_colors = {"600 nM": "lavender",
                  "300 nM": "lightskyblue",
                  "150 nM": "lightsteelblue",
                  "75 nM": "lightslategray"}

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)

for conc in df.columns:
    ax.plot(df.index, df[conc],
            label=conc,
            color=conc_to_colors[conc])

    ax.legend(loc="lower right", prop={"size": 9})
    ax.set_xlabel("Time (s)", fontsize=12)
    ax.set_ylabel("STLING response (nm)",
                  fontsize=12)
    sns.despine()

# %%
data_url = "./data/41467_2022_32521_MOESM10_ESM.xlsx"
df = pd.read_excel(data_url,
                   sheet_name="Figure1",
                   usecols="B:T",
                   index_col=0,
                   skiprows=1,
                   nrows=7)
df

# %%
Glc_labels = [("Glc", f"Replicate{x}") for x in range(6)]
Lac_labels = [("Lac", f"Replicate{x}") for x in range(6)]
Unt_labels = [("Untreated", f"Replicate{x}") for x in range(6)]
df.columns = pd.MultiIndex.from_tuples(Glc_labels + Lac_labels + Unt_labels,
                                       names=["Treatment regimen", "Replicates"])
df = df.reset_index()
df

# %%
df = df.melt(id_vars=["Days"],
             value_name="Total volume")
df

# %%
fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)
sns.pointplot(data=df,
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
