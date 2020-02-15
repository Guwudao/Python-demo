import pandas as pd
from datetime import date, timedelta

"""
# df = pd.DataFrame({"ID": [1, 2, 3, 4], "Name": ["a", "b", "c", "d"]})
# df.set_index("Name")
# print(df)


# df = pd.read_excel("./demo.xlsx")
# df.columns = ["a1", "a2", "a3"]

# print(df.columns)
# print(df.head(2))
# print(df.tail(2))

# s = pd.Se"?}{

# s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name="A")
# s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name="B")
# s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name="C")
#
# print(pd.DataFrame([s1, s2, s3]))
# print(pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3}))

# df.to_excel("demo.xlsx")
# print("success")
"""

"""
def month_calculate(y, m, d):
    y = y + m // 12
    m = m % 12
    if m == 0:
        m = 12
    return date(y, m, d)


start = date(2020, 1, 5)
book = pd.read_excel("Book.xlsx", skiprows=4, usecols="C:F", dtype={"index": str, "instore": str, "date": str})
for i in book.index:
    book["index"].at[i] = i + 1
    book["instore"].at[i] = "YES" if i % 2 == 0 else "NO"

    final_date = month_calculate(start.year, start.month + i, start.day)
    # print(final_date)
    book["date"].at[i] = final_date
    #
    # book.at[i, "index"] = i + 1
    # book.at[i, "instore"] = "YES" if i % 2 == 0 else "NO"
    # book.at[i, "date"] = final_date

print(book)
"""

book = pd.read_excel("BookPrice.xlsx", index_col="index")

# book["final"] = book["price"] * book["undercut"]
# book.sort_values(by=["special", "price"], inplace=True, ascending=[False, True])

book = book.loc[book["price"].apply(lambda x: 30 <= x < 50)].loc[book["undercut"].apply(lambda x: x > 0.6)]
print(book)

