#!/usr/bin/env python
# coding: utf-8

# 1. In the first assignment, you downloaded the sequence for chr1_GL383518v1_alt.fa. Write a Python program to read the complete sequence from the file. (5 points)

file_name = "chr1_GL383518v1_alt.fa"

with open("/Users/xuyixeric/Informatics_573/chr1_GL383518v1_alt.fa", 'r') as file:
    sequence = ''
    for line in file:
        if line.startswith('>'):
            # Skip headers
            continue
        else:
            # Remove leading and trailing whitespace and append the sequence
            #+= provides a convenient way to add a value to an existing variable 
            #and assign the new value back to the same variable
            sequence += line.strip()
    
    #print(sequence)


# a.Print the 10th letter of this sequence.

print(sequence[9])


# b.Print the 758th letter of this sequence.

print(sequence[757])


# 2. Write a Python program to create the reverse complement of the encoded DNA molecule used in Part 1. Remember to reverse the sequence, and substitute the bases with their Watson-Crick-Franklin pair. (10 points)

def reverse_complement(dna_sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Reverse the DNA sequence
    reversed_sequence = dna_sequence[::-1].upper()
    
    # Replace bases with their complement
    complemented_sequence = ''.join([complement_dict[base] for base in reversed_sequence])
    
    return complemented_sequence

#Check if the function works 
#encoded_dna = "ATCGTAGCTAGC"
# Create the reverse complement of the DNA sequence
#reverse = reverse_complement(encoded_dna)
#print("Sample Original DNA Sequence:", encoded_dna)
#print("Sample Reverse Complement:", reverse)
#works


# a.Print the 79th letter of this sequence.

re_data = reverse_complement(sequence)


print(re_data[78])


# b.Print the 500th through the 800th letters of this sequence.


print(re_data[499:799])


# 3. Write a Python program that asks the user for a number, and generates a list of numbers that contains that many terms of the Fibonacci numbers. (10 points)


nt = int(input("Your Number of terms: "))
try:
    print("You entered:", nt)
except ValueError:
    print("Error: Please enter an integer.")

def gen_fib(nt):
    f_seq = []
   # first two terms
    n1 = 0; n2 = 1
    for _ in range(nt):
       f_seq.append(n1)
       nts = n1 + n2
     # update values
       n1 = n2; n2 = nts
    return f_seq
        
f_list = gen_fib(nt)
print("Fibonacci List:", f_list)


# a.Use your generated list of Fibonacci numbers to make a second list of numbers, where the first number is 1, and each subsequent number is quotient of the corresponding Fibonacci number and the previous Fibonacci number.


# Function to create the second list as described
def gen_second_list(fibonacci_list):
    second_list = [1]  # First number is 1
    for i in range(1, len(fibonacci_list)):
       # Calculate the quotient of the current Fibonacci number and the previous one
        if fibonacci_list[i - 1] == 0:
            quotient = 0  # Handle division by zero
        else:
            quotient = fibonacci_list[i] / fibonacci_list[i - 1]
        second_list.append(quotient)
    return second_list

second_list = gen_second_list(f_list)

# Print the second list
print("Second List:", second_list)


# b.Use your second list of numbers to make a third group of numbers, where the first two elements are 0, and each subsequent element is the difference of the corresponding element in the second list and the previous element in the list group.

# Function to create the third list as described
def gen_third_list(second_list):
    third_list = [0, 0]  # First two elements are 0
    for i in range(2, len(second_list)):
        # Calculate the difference of the corresponding element in the second list
        # and the previous element in the third list
        diff = second_list[i] - second_list[i - 1]
        third_list.append(diff)
    return third_list
# Create the third blist
third_list = gen_third_list(second_list)
# Print the third list
print("Third List:", third_list)


# 4. Write a Python program that uses nested loops to create a 10 by 10 matrix from nested lists that contains consecutive odd numbers starting at 1. (15 points)

# Initialize an empty matrix (a list of lists)
matrix = []

#first number start at 1
odd = 1

# Define the number of rows and columns
rows = 10; cols = 10

# Create the matrix using nested loops
for i in range(rows):
    # Initialize a row for the current iteration
    row = []
    for j in range(cols):
        # Append the next odd number to the current row
        row.append(odd)
        # Increment the odd number by 2 for the next iteration
        odd += 2
    # Append the current row to the matrix
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)


# a. Calculate the trace of this matrix using list index positions. Store it as a variable.
# Initialize a new variable to store the trace
trace = 0
for i in range(len(matrix)):
    trace += matrix[i][i]
print(trace)


# b. Display the trace with the sentence “The trace of your matrix is X”, where X is the variable containing the calculated trace.
# 

print(f"The trace of your matrix is {trace}")


# c. Calculate the sum of all elements in the upper triangle of the matrix. Store it as a variable.


# Initialize a new variable to store the sum of upper triangle elements
upper_sum = 0
for i in range(len(matrix)):
    for j in range(i, len(matrix)):
        upper_sum += matrix[i][j]
print(upper_sum)


# d. Display the sum of all elements in the upper triangle of the matrix with the sentence “The sum of upper triangular elements in your matrix is X.”, where X is the variable containing the calculated sum of upper triangular elements.
#

# Print the sum of upper triangle elements
print(f"The sum of upper triangular elements in your matrix is {upper_sum}")


# e. Calculate the sum of all elements in the lower triangle of the matrix. Store it as a variable.
#

# Initialize a new variable to store the sum of lower triangle elements
lower_sum = 0

# Calculate the sum of lower triangle elements
for i in range(len(matrix)):
    for j in range(i+1):
        lower_sum += matrix[i][j]
        
print(lower_sum)


# f. Display the sum of all elements in the upper triangle of the matrix with the sentence “The sum of lower triangular elements in your matrix is X.”, where X is the variable containing the calculated sum of lower triangular elements.
#

# Print the sum of lower triangle elements
print(f"The sum of lower triangular elements in your matrix is {lower_sum}")


# 5. Write a Python program to read the sequence used in Part 1. (20 points)



# Create a nested dictionary that contains the number of times each letter appears in the downloaded sequence, as a function of which kilobase of the sequence you are looking at.


# Initialize the nested dictionary
my_dict = {}

# Iterate through the sequence
for i in range(0, len(sequence), 1000):
    # Initialize a dictionary for the current kilobase
    kilobase_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    # Get the current kilobase sequence
    kilobase_sequence = sequence[i:min(i+1000,len(sequence))]
    
    # Count the occurrences of each nucleotide in the kilobase sequence
    for nucleotide in kilobase_sequence:
        if nucleotide in kilobase_dict:
            kilobase_dict[nucleotide] += 1
    
    # Store the kilobase dictionary in the main dictionary
    my_dict[i] = kilobase_dict

# Print the nested dictionary 5000 for example
print(my_dict[5000])




print(my_dict[5000]["A"])








