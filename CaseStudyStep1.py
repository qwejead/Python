import pandas as pd

Border="-"*30

#######################################################################################################
#step1:Load the data set
#######################################################################################################

print(Border)
print("step 1: Load the Database")
print(Border)

DataPath="iris.csv"

df=pd.read_csv(DataPath)


"""
df=pd.read_csv(DataPath)    इथे df हा एक DataFrame object आहे.
                            DataFrame म्हणजे basically Python मधील table

                            Python process च्या memory मध्ये DataFrame object तयार होतो.
                            आणि df हा variable त्या object कडे reference ठेवतो.
"""

print("DataBase Loaded Succesfully")

print("Inital entries from dataset are :")

print(df.head())

"""
head() default ने पहिल्या 5 rows दाखवतो.

Full DataFrame
      ↓
पहिल्या 5 rows select
      ↓
नवीन छोटा DataFrame representation
      ↓
print()
      ↓
Screen
"""