"""Submit your results as a .py file via your GitHub repository.
1. Import numpy as np and print the version number. 
2. Create a 1D array of numbers from 0 to 9. Desired output:
    #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
3. Import a dataset with numbers and texts keeping the text intact in python numpy.
Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site.. (20 Points)
4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset.
Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site.. (20 Points)
5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
Input:
    np.random.seed(100)
    a = np.random.uniform(1,50, 20)
(20 Points)
"""

"1."
import numpy as np
print("1. = version", np.__version__)

"2."
a = np.arange(10)
print("2. =", a)

"3."
# URL of the Iris dataset for question 3
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Load the dataset using genfromtxt
#dtype=object bc dataset contains #s and text
iris_dataset = np.genfromtxt(url, delimiter=',', dtype=object, encoding='utf-8')
# Print dataset
print("3. Iris dataset imported =", iris_dataset)

"4."
#extract 4th column, which is the petalwidth
petalwidth = iris_dataset [:, 3].astype(float) #making sure the column is a float before applying conditions
#boolean mask setting condition: petalwidth needs to be greater than 1.0
mask = petalwidth > 1.0
#find the first occurrence of True (first value that meets the condition)
first_index = np.argmax(mask)
print("4. First occurrence of petalwidth > 1.0 is at position", first_index)

"5."
np.random.seed(100)
a = np.random.uniform(1,50,20)
#np.clip, anything less than 10 becomes 10 and anything greater than 30 becomes 30 (faster than setting a min & max)
a = np.clip(a, 10, 30)
print("5. =", a)
