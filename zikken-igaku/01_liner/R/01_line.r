install.packages("ggplot2", repos="https://cran.ism.ac.jp/")
library(ggplot2)
library(ggsci)
library(reshape2)
library(dplyr)

setwd("~/workspace/Python-R-Class/zikken-igaku/01_liner/R/")
df = read.csv("./41586_2022_5354_MOESM5_ESM_selected.csv")
head(df)
colnames(df) = c("Time", "X600.nM", "X300.nM", "X150.nM", "X75.nM")
head(df)

melt_df = melt(df, id.vars="Time")
head(melt_df)


g = ggplot(melt_df,
    aes(x=Time, y=value, color=variable)) +
    geom_line() +
    scale_color_manual(name="",
                       values=c("lavender", "lightskyblue", "lightsteelblue", "lightslategray"), 
                       labels=c(X600.nM="600 nM", X300.nM="300 nM", X150.nM="150 nM", X75.nM="75 nM")) +
    theme_classic(base_size = 20) +
    labs(
         x = "Time (s)",
         y = "STLING response (nm)",)
plot(g)


df = read.csv("./41467_2022_32521_MOESM10_ESM_melted.csv")
head(df)

df_summarise = group_by(df, Days, Treatment.regimen) %>% 
                summarise(mean = mean(Total.volume), 
                       sd = sd(Total.volume),
                       se = sd(Total.volume)/sqrt(length(Total.volume))
                )
head(df_summarise)

g = ggplot(df_summarise, aes(x=Days, y=mean, color=Treatment.regimen)) +
    geom_line() +
    geom_errorbar(aes(ymax=mean+se, ymin=mean-se), 
                  width = 1.0,
                  linewidth = 0.7) +
    geom_point(size=3) +
    theme_classic(base_size = 20) +
    scale_color_manual(name="",
                       values=c("Skyblue", "Orange", "Gray"),) +
    theme_classic(base_size = 20) +
    labs(
        x = "Days",
        y = "Total volume (mm^3)",)
plot(g)

