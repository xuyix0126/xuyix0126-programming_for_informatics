#!/bin/bash

#Navigate to the user’s home directory

cd ~

#Create a directory titled “Informatics_573” and navigate to it

mkdir ~/Informatics_573
cd ~/Informatics_573

#Download required assemblies for human chromosome 1 from University of California, Santa Cruz (UCSC) Genome browser

wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chr1_GL383518v1_alt.fa.gz' -O chr1_GL383518v1_alt.fa.gz

#Unzip the downloaded file

gunzip chr1_GL383518v1_alt.fa.gz
