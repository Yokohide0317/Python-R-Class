DATA1="41467_2022_33749_MOESM6_ESM.xlsx"
DATA2="41467_2022_34346_MOESM4_ESM.xlsx"
DATA3="Figure_3h.csv"
DATA4="41467_2022_32521_MOESM10_ESM.xlsx"



all: data data/$(DATA1) data/$(DATA2) data/saunders_source_data/$(DATA3) data/$(DATA4)
.PHONY: clean

data: $(wildcard *.o)
	@if [ ! -d data ]; then \
        echo ";; mkdir data"; mkdir data; \
    fi

data/$(DATA1):
	wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9568535/bin/$(DATA1) -O data/$(DATA1)

data/$(DATA2):
	wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9663433/bin/$(DATA2) -O data/$(DATA2)

data/41467_2022_34334_MOESM6_ESM.zip:
	wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9668842/bin/41467_2022_34334_MOESM6_ESM.zip -O data/41467_2022_34334_MOESM6_ESM.zip

data/saunders_source_data/$(DATA3): data/41467_2022_34334_MOESM6_ESM.zip
	unzip data/41467_2022_34334_MOESM6_ESM.zip -d data

data/student.zip:
	URL="https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"
	wget $(URL1) -O data/$(FILE1)

data/$(DATA4):
	wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9448806/bin/$(DATA4) -O data/$(DATA4)

clean:
	rm -r data/41467_2022_34334_MOESM6_ESM.zip data/__MACOSX
