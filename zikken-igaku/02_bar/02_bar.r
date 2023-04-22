setwd("~/workspace/Python-R-Class/zikken-igaku/")

install.packages("readxl")
install.packages("reshape2")
install.packages("ggsci")
library(readxl)
library(ggplot2)
library(ggsci)

data_file = "./data/41467_2022_33749_MOESM6_ESM.xlsx"
df_basal = read_xlsx(data_file, sheet="Fig 6", range="A132:C135")
df_atp = read_xlsx(data_file, sheet="Fig 6", range="D132:F135")
df_max = read_xlsx(data_file, sheet="Fig 6", range="G132:I135")

melt_genotype <- function(tmp, condition) {
    tmp = reshape2::melt(tmp,
                        variable.name="Genotype",
                        value.name="OCR (pmol/min/well)",
                        na.rm=TRUE)
    tmp$Condition = c(rep(condition, nrow(tmp)))
    return(tmp)
}

df_basal = melt_genotype(df_basal, "Basal")
df_atp = melt_genotype(df_atp, "ATP Production")
df_max = melt_genotype(df_max, "mMaximal")

df = rbind(df_basal, df_atp, df_max)
df

ggplot(df, aes(x="Genotype", y="OCR (pmol/min/well)", fill="Condition"))+
    geom_bar(stat="identity", position=position_dodge())+
    geom_text(aes(label="OCR (pmol/min/well)"), vjust=1.6, color="white",
              position = position_dodge(0.9), size=3.5)+
    scale_fill_brewer(palette="Paired")+
    theme_minimal()

ggplot(data=df, aes("Condition", y="OCR (pmol/min/well)", group="Genotype")) + 
    geom_bar(aes(fill="Genotype"), stat="identity", 
             position="dodge") + 
    coord_flip()

