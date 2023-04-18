#!/bin/bash

if [ ! -d data ]; then
    mkdir data
fi

DATA1="1404609_2_1.xlsx"
if [ ! -f data/${DATA1} ]; then
    wget https://www.mext.go.jp/a_menu/shotou/gakuryoku-chousa/sonota/__icsFiles/afieldfile/2018/05/07/${DATA1} -O data/${DATA1}
fi



