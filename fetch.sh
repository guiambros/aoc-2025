#!/bin/bash
TARGET="day${1}"
source ../auth-token.sh
if [[ -d "${TARGET}" ]]; then
    echo "Folder '${TARGET}' already exists; reimporting only input file."
    cd ${TARGET}
    python ../fetch.py
    mv input_2024_${1}.txt in.txt
    touch test.txt
else
    mkdir -p ${TARGET}
    cd ${TARGET}
    cp -n ../.day_template.py ${TARGET}.py
    python ../fetch.py
    mv input_2024_${1}.txt in.txt
    touch test.txt
fi

