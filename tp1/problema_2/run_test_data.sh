#!/bin/bash

set -euo pipefail

test_data="test_data"
output="results.txt"

> "$output"

for archivo in "$test_data"/*.txt; do
    python3 problema_2_for_test.py "$archivo" >> "$output"
    echo "" >> "$output"
done

echo "Todos los resultados se guardaron en '$output'."
