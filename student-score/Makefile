#!/bin/bash
FILE1 = "student.zip"
URL1="https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"

all: data/student/student-mat.csv
.PHONY: clean

data:
	mkdir data

data/student/student-mat.csv: data  data/student.zip
	unzip -d data/student data/$(FILE1)

data/student.zip: data
	URL="https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"
	wget $(URL1) -O data/$(FILE1)

clean:
	rm data/$(FILE1)
