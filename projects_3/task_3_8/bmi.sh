#!/bin/bash

read -p "Введите ваш рост (в метрах): " HEIGHT
read -p "Введите ваш вес (в килограммах): " WEIGHT
BMI=$(echo "scale=2; $WEIGHT/($HEIGHT * $HEIGHT)" | bc)
echo "Ваш ИМТ равен $BMI"
