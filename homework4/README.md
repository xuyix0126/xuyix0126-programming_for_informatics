# homework4


**Programmer:** Yixi Xu

**Programming Language:** R (R studio/Rmarkdown)

**Date:** 11/4/2023

---

## Description

This repository is designed to pratice the following:
- **1:** create basic objects in R

- **2:** carry out mathematical operations in R

- **3:** installing R libraries

- **4:** use R functions to perform statistical operations and measurements

It includes: R markdown script hw4_info.Rmd that will show the answers of homework questions.

---
## Required files:

### `README.md`
- **Description:** This readme file providing information about the script.
- 
### ` hw4_info.Rmd`
- **Description:** An R markdown script .
- **Usage:** practice with fundamental R programming concepts and data manipulation techniques (including explore vector creation, matrix manipulation, logical operations, and function development. Additionally, include real-world data analysis and manipulation using external datasets)
---

## Requirements
- **R:** The script is written in R to perform basic r commands.

## Execution:
1. **Clone the Repository:**  
  ```bash
git clone https://github.iu.edu/xuyix/homework4.git
  ```

2. **Run R Markdown script:**
  download and open the R markdown file then click knit; The results will be generated in html/PDF format depend on your preference


## Output files:
hw4_info.pdf

The results of the Rmarkdown PDF file will includes the following:

1. a vector containing each number between 1 and 50, inclusively.  

  a. a 5 x 10 matrix construct by a previous vector
  
  b. a logical matrix where the values of the matrix is evenly divisible by 3 or has a remainder of 1 when divided by 6.
  
  c. extracted values of the matrix where the logical matrix made in part b.
  
  d. a function called hailstone(x) where the function should determine if x is odd or even. If x is odd, multiply x by 3 and add 1, otherwise divide x by 2. Repeat this process until the number is 1. The function should return the number of the cycles that the number goes through before reaching 1.
  
  e. The results after applying the function that created in part d to the values extracted in part c.

2. Install the ISLR library and load the Auto dataset.

  a. data that remove qualitative data columns from the Auto data.
  
  b. a loop that will iterate through the columns and print the range of each quantitative variable.
  
  c. a matrix containing the mean and the standard deviation of each column.
  
  d. a data that removes the rows that have less than the mean amount of mpg.
  
  f. a matrix with recalculated mean and standard deviation of each column now that values with below average mpg have been removed.

3. comment of comparing and contrasting the R code and the equivalent Python code, and personal preference for one of the languages
