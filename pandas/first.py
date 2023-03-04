import pandas

# to print a set of data
myfirstDataFrame = pandas.DataFrame([
    [1, 2, 3],
    [10, 20, 30]
])

# we can pass the name of the columns as well
mySecondtDataFrame = pandas.DataFrame([
    [1, 2, 3],
    [10, 20, 30]
], columns = ["Price", "Age", "Value"])

# we can rename index of the rows
myThirdDataFrame = pandas.DataFrame([
[1, 2, 3],
[10, 20, 30]
], columns = ["Price", "Age", "Value"],
    index = ["First Row", "Second Row"])

# you can pass dictionaries
myFourDataFrame = pandas.DataFrame([
    {"Name": "Bruce"},
    {"Name": "Ryan"}
])

# if we have more columns, we obtain NaN
myFourDataFrame = pandas.DataFrame([
    {"Name": "Bruce", "Surname": "Batman"},
    {"Name": "Ryan"}
])

# to see all methods
dir(myfirstDataFrame)

# to see the type
type(myfirstDataFrame)

# to obtain average
# it returns a pandas Series
average = myfirstDataFrame.mean()
type(average)

# to obtain average of the results
average2 = myfirstDataFrame.mean().mean()

# we can obtain a specifif colum of the DataFrame
myprice = mySecondtDataFrame.Price

# and to aplly the mean method
average3= mySecondtDataFrame.Price.mean()
print(average3)
