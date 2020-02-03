import pandas as pd

# df = pd.DataFrame({"ID": [1, 2, 3, 4], "Name": ["a", "b", "c", "d"]})
# df.set_index("Name")
# print(df)


df = pd.read_excel("./demo.xlsx")
# df.columns = ["a1", "a2", "a3"]

print(df.columns)
print(df.head(2))
print(df.tail(2))

# df.to_excel("demo.xlsx")
# print("success")
