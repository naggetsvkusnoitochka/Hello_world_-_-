#!/bin/bash
awk -F "," '{print $2}' data.csv 
awk -F "," '{
    if ($3 > 20)
        print $2, $3
}' data.csv
awk -F "," '{sum += $3; n++} END {print sum/n}' data.csv

