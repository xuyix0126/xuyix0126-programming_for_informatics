# homework2


**Programmer:** Yixi Xu

**Programming Language:** Bash, Python

**Date:** 09/20/2023

---

## Description

This repository is designed to download the sequence for chr1_GL383518v1_alt.fa. from University of California, Santa Cruz (UCSC), unzip the file with bash command, and practice basic python commands.

It includes: the bash script hw2.sh file that download the required DNA sequence, and the python script home2_573.py that will show the answers of homework questions.

---
## Required files:

### `hw2.sh`
- **Description:** The main script file.
- **Usage:** Execute this script to perform the download tasks described in the README.
### `README.md`
- **Description:** This readme file providing information about the script.
### `home2_573.py`
- **Description:** An python script .
- **Usage:** practice basic python commands
---

## Requirements
- **Bash:** The script is written in Bash and requires a Bash-compatible environment.
- **Python:** The script is written in Python to perform basic python commands.

## Execution:
1. **Clone the Repository:**  
  ```bash
git clone https://github.iu.edu/xuyix/homework2.git
  ```

2. **Make the script executable:**

  ```bash
chmod +x hw2.sh
  ```

3. **Run Python script:**
  ```bash
  #run bash 
 ./hw2.sh
#the run the python file
python home2_573.py


  ```


## Output files:

No file will be created. 

The results of the python includes:

1. The 10th and 758th letter of chr1_GL383518v1_alt.fa sequence.
2. The 79th and 500th through the 800th letter of the reverse complement of the chr1_GL383518v1_alt.fa sequence
3. Function that creates required 3 Fibonacci numbers lists.
4. Trace, sum of upper/lower tranglular of a required 10:10 matrix
5. A nested dictionary that contains the number of times each letter appears in the downloaded sequence, as a function of which kilobase of the sequence the user is looking at.
