#!/bin/bash
for i in {1..10}; do
    touch "test$i.txt"
    echo "Файл test$i.txt создан"
done
i=10
while [ $i -ge 1 ]; do
    rm "test$i.txt"
    echo "Файл test$i.txt удален"
    i=$((i - 1))
done

