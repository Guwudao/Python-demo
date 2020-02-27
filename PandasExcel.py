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
    book = pd.read_excel("BookPrice.xlsx", index_col="index")

    # book["final"] = book["price"] * book["undercut"]
    # book.sort_values(by=["special", "price"], inplace=True, ascending=[False, True])

    book = book.loc[book["price"].apply(lambda x: 30 <= x < 50)].loc[book["undercut"].apply(lambda x: x > 0.6)]
    print(book)

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


def hsbc_file():
    hsbc = pd.read_excel("HSBC业务线Base版2月25日人员休假-移动.xlsx", sheet_name="明细", usecols="C, E, G:AC")
    # print(hsbc)
    # print(hsbc.head(5))
    # print(hsbc.columns)
    # print(hsbc.loc[0:2])
    # print(hsbc.loc[[2, 3, 8]])
    data_totally_list = np.array(hsbc)
    print(data_totally_list)


    # print(data_totally_list[0])
    title_list = data_totally_list[0]
    woring_list, leave_list, other_list = [], [], []

    for i in range(len(data_totally_list[0])):
        woring_list.append(0)
        leave_list.append(0)
        other_list.append(0)

    is_skip_first = True
    for data_list in data_totally_list:

        if not is_skip_first:
            for index, data in enumerate(data_list):
                if data == "在家办公（WFH）" or data == "公司现场":
                    woring_list[index] += 1
                elif data == "休假":
                    leave_list[index] += 1
                else:
                    other_list[index] += 1
        else:
            is_skip_first = False

    # print(woring_list)
    # print(leave_list)
    # print(other_list)

    final_working_list, final_leave_list, final_other_list, final_title_list = [], [], [], []

    for a, b, c, d in zip(woring_list, leave_list, other_list, title_list):
        if a > 0:
            final_working_list.append(a)
            final_leave_list.append(b)
            final_other_list.append(c)
            final_title_list.append(d)

    print(final_working_list)
    print(final_leave_list)
    print(final_other_list)
    print(final_title_list)

    PyechartsDataAnalysis.working_analysis(final_title_list, final_working_list, final_leave_list, final_other_list)


hsbc_file()
