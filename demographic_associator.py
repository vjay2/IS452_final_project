import pandas as pd
import numpy as np
import pprint

#testing merge with simpler files to make sure it works correctly
df1 = pd.read_csv("test1.csv", header =[0])
df2 = pd.read_csv("test2.csv", header =[0])

test = pd.merge(df1, df2)
pprint.pprint(test)

test.to_csv("test.csv")

df3 = pd.read_csv("counted_file.csv", header =[0])
df4 = pd.read_csv("demographics_information.csv", header =[0])
new_df = pd.merge(df3, df4)
new_df.to_csv("combined.csv")
