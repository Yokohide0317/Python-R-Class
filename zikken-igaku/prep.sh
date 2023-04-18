#!/bin/bash

if [ ! -d data ]; then
    mkdir data
fi

DATA1="41467_2022_33749_MOESM6_ESM.xlsx"
if [ ! -f data/${DATA1} ]; then
    wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9568535/bin/${DATA1} -O data/${DATA1}
fi


DATA2="41467_2022_34346_MOESM4_ESM.xlsx"
if [ ! -f data/${DATA2} ]; then
    wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9663433/bin/${DATA2} -O data/${DATA2}
fi


DATA3="Figure_3h.csv"
DATA3_DIR="saunders_source_data"
if [ ! -f data/${DATA3_DIR}/${DATA3} ]; then
    wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9668842/bin/41467_2022_34334_MOESM6_ESM.zip -O data/41467_2022_34334_MOESM6_ESM.zip
    unzip data/41467_2022_34334_MOESM6_ESM.zip -d data
    rm data/41467_2022_34334_MOESM6_ESM.zip
fi