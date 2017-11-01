import pandas

# using absolute path
dataframe = pandas.read_csv("/home/fazt/Escritorio/python/python3-course/data-examples/supermarkets.csv")
# using relative path
# pandas.read_csv("../data-examples/supermarkets.csv")


print(dataframe)
