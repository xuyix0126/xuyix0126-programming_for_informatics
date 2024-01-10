#!/usr/bin/env python
# coding: utf-8

# ## HOMEWORK 3 ##

# **1.** A key property in the mathematics of sequences and in computer algorithms is the idea of convergence. A definition of convergence is that a series converges to an asymptote such that the difference between the series and the asymptote can be made arbitrarily small with high and known probability. (30 points)
# 
# 

# In[307]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# a. 
# Write a function that takes an integer X as an input and will return a numpy array that contains the first X numbers of the Fibonacci numbers.
# 
# 

# In[308]:


def gen_fib(nt):
    f_seq = np.zeros(nt,dtype=np.int64)
    if nt>1:
        f_seq[1] = 1
    for i in range(2,nt):
        f_seq[i] = f_seq[i - 1] + f_seq[i - 2]
    return f_seq
        
#f_list = gen_fib(nt)
#print("Fibonacci numpy array:", f_list)


# b. Use the previous function to create a numpy array with the first 20 values of the Fibonacci numbers.
# 
# 

# In[309]:


nt=20
f_list = gen_fib(nt)
print("Fibonacci numpy array:", f_list)


# c.
# Use this numpy array to recreate the arrays from part 3 of the second assignment, one array that is the quotient of consecutive Fibonacci numbers, and the difference of the quotient of consecutive Fibonacci numbers.
# 
# 

# In[310]:


# Function to create the second list as described
def gen_second_list(fibonacci_list):
    second_array = np.array([1])   # First number is 1
    for i in range(1, len(fibonacci_list)):
       # Calculate the quotient of the current Fibonacci number and the previous one
        if fibonacci_list[i - 1] == 0:
            quotient = 0  # Handle division by zero
        else:
            quotient = fibonacci_list[i] / fibonacci_list[i - 1]
            
        second_array = np.append(second_array, quotient)
    return second_array 

second_array = gen_second_list(f_list)

# Print the second list
print("Second List:", second_array)


# In[311]:


# Function to create the third list as described
def gen_third_list(second_list):
    third_array = np.array([0, 0])  # First two elements are 0
    for i in range(2, len(second_list)):
        # Calculate the difference of the corresponding element in the second list
        # and the previous element in the third list
        diff = second_list[i] - second_list[i - 1]
        third_array = np.append(third_array, diff)
    return third_array 
# Create the third blist
third_array = gen_third_list(second_array)
# Print the third list
print("Third List:", third_array)


# d. Plot all 3 of these series on the same graph. You may need to adjust the parameters of the plot in order to clearly view all three series at once.
# 
# 

# In[312]:


# Create an array of indices for plotting
indices = np.arange(1, 21)
# Create the primary y-axis for Fibonacci Numbers
plt.figure(figsize=(12, 6))
ax1 = plt.gca()
ax1.plot(indices, f_list, label="Fibonacci Numbers")
ax1.set_xlabel("Integer")
ax1.set_ylabel("Fibonacci Number")

# Create a secondary y-axis for 2nd and 3rd array
ax2 = ax1.twinx()
ax2.plot(indices, second_array, label="Quotient", color='green')
ax2.plot(indices, third_array, label="Difference", color='red')
ax2.set_ylabel("Values for Second and Third Arrays")

# Set labels and legend for both y-axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines + lines2, labels + labels2, loc='upper left')

plt.title('Fibonacci Numbers, Quotient, and Difference of Quotient')
plt.grid(True)
plt.xticks(np.arange(min(index), max(index) + 1, 1))
plt.show()


# e.Based upon your observation, do any of these series appear to be converging? If so what values do they appear to be converging to? Feel free to reference the values of the series when determining what value it appears to be converging to.
# 
# 

# Based upon my observation: quotient converge to 1.6 approximately and difference converge to 0

# **2.** Exploratory Data Analysis (EDA) is a critical initial step in the data analysis process. It involves systematically examining and visualizing data sets to gain insights, detect patterns, and identify anomalies. EDA helps data analysts and scientists understand the structure and characteristics of their data, making it easier to formulate hypotheses and guide subsequent analysis. (30 points)

# 1.Download data about the Titanic disaster from the Kaggle study link below. You will want both the training data and the testing data.
# https://www.kaggle.com/datasets/dbdmobile/tita111 Links to an external site.
# 
# 

# In[318]:


#! pip install opendatasets
#import opendatasets as od
#od.download("https://www.kaggle.com/datasets/dbdmobile/tita111")
#API is required to download datasets
import pandas as pd
import os

# List files in the "tita111" directory
file_list = os.listdir("tita111")
print(file_list)


# In[327]:


# Read the CSV files into DataFrames
test_data = pd.read_csv("tita111/tit_test.csv")
train= pd.read_csv("tita111/tit_train.csv")
sup_data = pd.read_csv("tita111/gender_submission.csv")

test = pd.merge(test_data, sup_data, on='PassengerId')
#print(test)


# 2.Open both files as pandas dataframes and concatenate them together using the concatenate command from pandas. HINT: You can look up documentation about the concatenate command either on the Pandas website, or using the help() function in Python.
# 
# 

# In[326]:


tit_data = pd.concat([train, test], ignore_index=True)
#print(tit_dat.head())


# 3.Create a summary of the pandas dataframe.
# 
# 

# In[328]:


summary = tit_data.describe()
print(summary)


# 4.Create a histogram showing the distribution of age of people on the Titanic. Make another histogram showing the distribution of age of people on the Titanic segregated by survivalship.
# 
# 

# In[329]:


# Plot a histogram of age
plt.hist(tit_data["Age"],  edgecolor="k")
plt.title("Distribution of Age on Titanic")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# In[434]:


# Plot histograms of age by survival status
plt.subplot(1,2,1)
plt.hist(tit_data[tit_data["Survived"] == 1]["Age"], alpha=0.5, label='Survived', color='blue', edgecolor="k")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Age on the Titanic by Survival status")
plt.legend()

plt.subplot(1,2,2)
plt.hist(tit_data[tit_data["Survived"] == 0]["Age"], alpha=0.5, label="Not Survived", color = 'red', edgecolor="k")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()


# Adjust spacing between subplots
plt.tight_layout()


# 5.Create a bar chart showing the percentages of who survived on the Titanic. Make another bar chart showing the percentages of who survived on the Titanic segregated by sex.
# 
# 

# In[349]:


# Calculate survival percentages
#value.counts: counts the occurrences of 0 and 1 (normalize=True return fraction)
surv_rate = tit_data["Survived"].value_counts(normalize=True) * 100
surv_rate


# In[363]:


# Plot a bar chart
surv_rate.plot.bar(rot=0,color = ["lightcoral","skyblue",]) #rot:rotation
plt.xlabel("Survived")
plt.ylabel("Percentage")
plt.title("Survival Percentage on the Titanic")
plt.xticks([0, 1], ["No", "Yes"]) #customize label
plt.show()


# In[365]:


# Group the data by sex and calculate the survival rate
surv_sex = tit_data.groupby('Sex')['Survived'].mean()* 100
plt.figure(figsize=(10, 6))
surv_sex.plot.bar(rot=0,color = ["lightcoral","skyblue"]) #rot:rotation
plt.title('Survival Percentage by Sex')
plt.xlabel('Sex')
plt.ylabel('Percentage Survived')
plt.show()


# 6.Create a boxplot showing the distribution of who survived on the Titanic vs their passenger class. Make another boxplot showing the distribution of who survived on the Titanic vs their passenger class segregated by sex.
# 
# 

# In[437]:


surv_rate_class = tit_data.groupby("Pclass")["Survived"].mean() * 100
surv_rate_class


# In[438]:


tit_data.groupby(['Pclass', 'Survived']).size().unstack()


# In[448]:


# Create a boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x="Pclass", y="Survived", data=tit_data, palette="Set1")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.title("Survival Rate on the Titanic by Passenger Class")
plt.show()
##No useful information here


# In[449]:


#try with barplot
# Calculate survival percentages by passenger class
survival_by_class = tit_data.groupby('Pclass')['Survived'].mean() * 100

# Create a bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x=survival_by_class.index, y=survival_by_class.values, palette="Set1")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.title("Survival Rate on the Titanic by Passenger Class")
plt.xticks(rotation=0)
plt.show()


# In[440]:


tit_data.groupby(['Pclass', 'Sex'])['Survived'].size().unstack()


# In[441]:


survival_by_class_sex = titanic_data.groupby(['class', 'sex'])['survived'].mean() * 100
survival_by_class_sex.index
survival_by_class_sex.values


# In[443]:


# Create a boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x="Pclass", y="Survived", hue="Sex", data=tit_data, palette="Set1")
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.title("Distribution of who survived on the Titanic vs their passenger class segregated by sex.")
plt.legend(title="Sex", loc="upper left")
plt.show()


# 7.Write a few sentence explaining the findings of your analysis. Feel free to reference any of visualizations.
# 
# BONUS: Additional embellishments to your visualizations, using matplotlib and/or seaborn functions to make your visualizations more aesthetically pleasing will be rewarded up to 20 extra points.

# The overall survival rate was around 38%. There are more female survived than male according to the bar chart. There are more peolpe with higher passenger class survived than lower passenger class from the barplot.The majortiy of people on Titianic were from 20 to 40 years old according to historgram. 

# In[ ]:




