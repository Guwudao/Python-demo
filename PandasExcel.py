import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import numpy as np
import PyechartsDataAnalysis


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

def book_operation():
    book = pd.read_excel("BookPrice.xlsx", index_col="Name")

    # book["final"] = book["price"] * book["undercut"]
    # book.sort_values(by=["special", "price"], inplace=True, ascending=[False, True])

    # new_book = book.loc[book["price"].apply(lambda x: 30 <= x < 50)].loc[book["undercut"].apply(lambda x: x > 0.6)]
    # print(new_book)
    #
    # drop_book = book.drop(book[book.price < 20].index)
    # print(drop_book)

    # print(book["price3"].sort_values())
    # book["price3"].sort_values().plot.pie(fontsize=10, startangle=-270)
    # plt.title("Book Price", fontdict={
    #     "size": 12,
    #     "weight": "bold"
    # })
    # plt.ylabel("Bookkkk", fontsize=12)
    # plt.show()

    print(book.index)
    print(type(book.index))
    print(type(book["index"]))
    print(np.array(book["index"]))


    print(book.columns)
    book.plot(y=['price1', 'price2', 'price3'])
    plt.title("line charts")
    plt.ylabel("namesss", fontsize=10, fontweight="bold")
    # plt.xticks(np.array(book["index"]), fontsize=8)
    plt.show()


def student_opera():
    student = pd.read_excel("Student.xlsx")
    student.sort_values(by="Number", inplace=True, ascending=False)
    student.plot.bar(x="Field", y="Number", title="Students sort")

    plt.show()
    print(student)

def student_compare():
    student = pd.read_excel("Student.xlsx")
    student.sort_values(by="2016", inplace=True)
    student.plot.barh(x="Field", y=["2016", "2017"], stacked=True)

    plt.show()
    print(student)


def hsbc_leave_file():
    hsbc = pd.read_excel("HSBC业务线Base版2月25日人员休假-移动.xlsx", sheet_name="明细", usecols="C, E, G:AC")
    # print(hsbc)
    # print(hsbc.head(5))
    # print(hsbc.columns)
    # print(hsbc.loc[0:2])
    # print(hsbc.loc[[2, 3, 8]])

    data_totally_list = np.array(hsbc)
    print(data_totally_list)

    PyechartsDataAnalysis.work_data_analysis(data_totally_list)


def hsbc_working_file():
    hsbc = pd.read_excel("电子签到单-2月3~25日 - 数字移动-移动.xlsx", sheet_name="Sheet1")
    # print(hsbc.head(3))
    # print(np.array(hsbc.loc[2])[-1])
    # l = np.array(hsbc.loc[2])
    # print(l[-1])

    # print(hsbc.iloc[:, 9])
    # print("--" * 20)
    # print(hsbc.loc[[1, 3, 5]])
    # print(hsbc["TL"])

    print(type(hsbc))
    print(type(hsbc.loc[hsbc["TL"] == "林俊杰"]))

    # l = np.array(hsbc.loc[hsbc["TL"] == "林俊杰"])
    # print(l)
    # for s in l:
    #     print(s)

    # ljj = hsbc.loc[hsbc["TL"] == "林俊杰"]
    # ljj.to_excel("ljj.xlsx")

    total_tl_list = np.array(hsbc["TL"])
    leader_list = []

    for leader in total_tl_list:
        if leader not in leader_list:
            leader_list.append(leader)

    print(leader_list)

    for leader in leader_list:
        data = hsbc.loc[hsbc["TL"] == leader]
        data.to_excel("{}.xlsx".format(leader))


# hsbc_leave_file()
# hsbc_working_file()
book_operation()