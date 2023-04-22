#!/bin/bash

set -eux

DATA1="41467_2022_33749_MOESM6_ESM.xlsx"
DATA2="41467_2022_34346_MOESM4_ESM.xlsx"
DATA3="Figure_3h.csv"
DATA4="41467_2022_32521_MOESM10_ESM.xlsx"

if [ ! -d data ]; then
	mkdir data
fi

function download_data() {
	if [ ! -f data/$1 ]; then
		wget $2 -O data/$1
	fi
}

download_data $DATA1 "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9568535/bin/$DATA1"

download_data $DATA2 "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9663433/bin/$DATA2"

if [ ! -d data/saunders_source_data ]; then
	wget "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9668842/bin/41467_2022_34334_MOESM6_ESM.zip" \
		-O data/41467_2022_34334_MOESM6_ESM.zip
	unzip data/41467_2022_34334_MOESM6_ESM.zip -d data

fi

download_data ${DATA4} "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9668842/bin/${DATA4}"
data/$(DATA4):
	wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9448806/bin/$(DATA4) -O data/$(DATA4)

clean:
	rm -r data/41467_2022_34334_MOESM6_ESM.zip data/__MACOSX
