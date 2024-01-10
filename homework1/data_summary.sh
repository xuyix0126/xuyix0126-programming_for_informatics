#!/bin/bash

# Step 1: Navigate to the user's home directory
cd ~

# Step 2: Create and navigate to the "Informatics_573" directory
mkdir -p Informatics_573
cd Informatics_573

# Step 3: Download chromosome 1 assemblies (except chr1.fa.gz)
wget --timestamping --accept "chr1_*" --reject "chr1.fa.gz" 'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/*'

# Step 4: Unzip downloaded assemblies
gunzip chr1_*.fa

# Step 5: Create an empty "data_summary.txt" file
touch data_summary.txt

# Step 6: Append detailed information to "data_summary.txt"
ls -l chr1_*.fa >> data_summary.txt

# Step 7 and 8: Append the first 10 lines and line count to "data_summary.txt" for each assembly
for file in chr1_*.fa; do
    echo "Assembly: $file" >> data_summary.txt
    echo "Line count: $(wc -l < "$file")" >> data_summary.txt
    echo "First 10 lines:" >> data_summary.txt
    head -n 10 "$file" >> data_summary.txt
    echo "-----------------------------------" >> data_summary.txt
done

echo "All tasks completed."
