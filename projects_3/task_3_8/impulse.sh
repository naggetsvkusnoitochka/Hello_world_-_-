#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Недостаточно входящих данных"
    exit 1
fi
NAME="$1"
QUANTITY="$2"
if ! [[ $2 =~ ^[0-9]+$ ]]; then
    echo "Ошибка: экспрессия должна быть целым числом"
    exit 1
fi
echo -e "Экспрессия гена $NAME составляет $QUANTITY единиц"
