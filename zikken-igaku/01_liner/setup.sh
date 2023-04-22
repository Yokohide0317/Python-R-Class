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

DATA1="41586_2022_5354_MOESM5_ESM.xlsx"
download_data ${DATA1} "https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-022-05354-0/MediaObjects/${DATA1}"


DATA2="41467_2022_32521_MOESM10_ESM.xlsx"
download_data ${DATA2} "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9448806/bin/${DATA2}"

DATA3="41467_2022_33721_MOESM9_ESM.xlsx"
download_data ${DATA3} "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9562072/bin/${DATA3}"