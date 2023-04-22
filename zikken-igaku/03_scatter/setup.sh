#!/bin/bash

set -eux

if [ ! -d data ]; then
	mkdir data
fi

function download_data() {
	if [ ! -f data/$1 ]; then
		wget $2 -O data/$1
	fi
}

DATA1="41467_2022_31113_MOESM16_ESM.xlsx"
download_data $DATA1 "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9187771/bin/${DATA1}"

DATA2="41467_2022_35319_MOESM4_ESM.xlsx"
download_data $DATA2 "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9747967/bin/${DATA2}"

