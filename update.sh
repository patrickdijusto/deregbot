#!/bin/bash

cd deregbot

rm -rf image.jpg
rm -rf deregbot.csv

wget https:deregbotcsv?dl=1 -O deregbot.csv

python deregbot.python
