DATA1="41467_2022_33749_MOESM6_ESM.xlsx"
DATA2="41467_2022_34346_MOESM4_ESM.xlsx"
DATA3="Figure_3h.csv"

all: data/$(DATA1) data/$(DATA2)
.PHONY: clean

data:
	mkdir data

data/$(DATA1): data
	wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9568535/bin/$(DATA1) -O data/$(DATA1)

data/$(DATA2): data
	wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9663433/bin/$(DATA2) -O data/$(DATA2)

data/41467_2022_34334_MOESM6_ESM.zip: data
	wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9668842/bin/41467_2022_34334_MOESM6_ESM.zip -O data/41467_2022_34334_MOESM6_ESM.zip

data/saunders_source_data/$(DATA3): data data/41467_2022_34334_MOESM6_ESM.zip
	unzip data/41467_2022_34334_MOESM6_ESM.zip -d data

data/student.zip: data
	URL="https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"
	wget $(URL1) -O data/$(FILE1)

clean:
	rm -r data/41467_2022_34334_MOESM6_ESM.zip data/__MACOSX
