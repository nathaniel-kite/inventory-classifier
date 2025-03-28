import pandas
import csv

df = pandas.read_csv("phoible-2.0/data/phoible.csv")

df.to_csv("phoible-2.0/data/phoible-modified.csv", quoting=csv.QUOTE_ALL, na_rep='?', index=False)

print(df)