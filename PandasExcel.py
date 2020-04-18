import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

import PyechartsDataAnalysis

# import matplotlib.font_manager

# _rebuild()

# a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
#
# for i in a:
#     print(i)

plt.rcParams["font.sans-serif"] = ["FangSong_GB2312"]

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

# os.chdir("Excel")
# print(os.getcwd())

def book_operation():
    book = pd.read_excel("./Excel/BookPrice.xlsx", index_col="index")

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

    # print(book.index)
    # print(book["price1"])
    # print(type(book.index))
    # print(type(book["index"]))
    # print(np.array(book["index"]))


    # print(book.columns)
    book.plot(y=["price1", "price2", "price3"])
    plt.xticks(book.index, fontsize=8)
    book.plot.area(y=["price1", "price2", "price3"])
    plt.xticks(book.index, fontsize=9)
    book.plot.bar(y=["price1", "price2", "price3"], stacked=True)
    plt.xticks(book.index, fontsize=10, rotation=360)

    # book.plot.scatter(x="price1", y="undercut")
    # book.price1.plot.hist(bins=100)
    # plt.xticks(range(0, max(book.price1), 5), fontsize=8)

    # print(book.corr())

    # plt.title("line charts")
    # plt.ylabel("namesss", fontsize=10, fontweight="bold")

    plt.show()


def student_opera():
    student = pd.read_excel("./Excel/Student.xlsx")
    student.sort_values(by="Number", inplace=True, ascending=False)
    student.plot.bar(x="Field", y="Number", title="Students sort")

    plt.show()
    print(student)


def student_compare():
    student = pd.read_excel("./Excel/Student.xlsx")
    student.sort_values(by="2016", inplace=True)
    student.plot.bar(x="Field", y=["2016", "2017"], stacked=True)

    plt.show()
    print(student)


def hsbc_leave_file():
    hsbc = pd.read_excel("./Excel/HSBC业务线Base版2月25日人员休假-移动.xlsx", sheet_name="明细", usecols="C, E, G:AC")
    # print(hsbc)
    # print(hsbc.head(5))
    # print(hsbc.columns)
    # print(hsbc.loc[0:2])
    # print(hsbc.loc[[2, 3, 8]])

    data_totally_list = np.array(hsbc)
    print(data_totally_list)

    PyechartsDataAnalysis.work_data_analysis(data_totally_list)


def hsbc_working_file():
    hsbc = pd.read_excel("./Excel/电子签到单-2月3~25日 - 数字移动-移动.xlsx", sheet_name="Sheet1")
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

def pbb_work():
    # pbb = pd.read_excel("现场保障表—移动全员.xlsx")

    pbb = pd.read_excel("./Excel/HSBC业务线返工明细信息统计（汇总）.xlsx", sheet_name="明细")
    print(pbb.columns)
    # my = pbb.loc[pbb["保长"] == "林俊杰"]
    # my.to_excel("demo.xlsx")
    new = pbb.sort_values(by="保长")
    new.to_excel("new_pbb.xlsx")


def data_combine():
    pd.set_option('display.max_columns', None)
    price = pd.read_excel("./Excel/BookPrice.xlsx", sheet_name="price")
    content = pd.read_excel("./Excel/BookPrice.xlsx", sheet_name="content")

    # print(price)
    # print(content)
    p = price.loc[:, ~price.columns.str.contains("^Unnamed")]
    print(p.merge(content, how="left", on="Name").fillna(0))
    # .to_excel("content.xlsx")

def price_validate(row):
    try:
        assert row.price1<=40
    except:
        print(f'#{row.Name}\t has not a validate price {row.price1}')


def book_data_validate():
    book = pd.read_excel("./Excel/BookPrice.xlsx", index_col="index", sheet_name="price")
    print(book)

    # book.apply(price_validate, axis=1)

    temp = book[["price1", "price2", "price3"]]
    # print(temp)

    book["total"] = temp.sum(axis=1)
    book["average"] = temp.mean(axis=1)

    col_mean = book[["price1", "price2", "price3", "total", "average"]].mean()
    book = book.append(col_mean, ignore_index=True)
    print(book)


def drop_duplicated():
    book = pd.read_excel("./Excel/BookPrice.xlsx", sheet_name="price")
    print(book[:,["B", "C"]])

    dupe = book.duplicated(subset=["Name"])
    dupe = dupe[dupe == True]
    print(dupe.index)
    print(book.iloc[dupe.index])

    slope, intercept, r, prob, std_err = linregress(book.index, book.price1)
    exp = book.index * slope + intercept
    plt.scatter(book.index, book.price1)
    plt.plot(book.index, exp, color="green")
    plt.xticks(book.index)
    print(slope, intercept, r, prob, std_err)

    # book.plot.bar(y=["price1", "price2"])
    # plt.bar(book.index, book.price1)
    # plt.xticks(book.index)
    # plt.tight_layout()

    # plt.show()


def pivot_table():

    pd.options.display.max_columns = 999
    pt = pd.read_excel("./Excel/class/第3节.xlsx", sheet_name="数据源")
    # print(pt)
    print(pt.head())

    pt1 = pt.pivot_table(index="产品类别", columns="销售人员", values=["金额", "数量"], aggfunc=np.sum)
    # print(pt1.head())
    print(pt1.index)
    # pt1.to_excel("./Excel/pt1.xlsx")

    p2_groups = pt.groupby(["销售人员", "产品类别"])
    # print(groups)

    p2_s = p2_groups["金额"].sum()
    p2_c = p2_groups["数量"].count()

    pt2 = pd.DataFrame({"sum":p2_s, "count":p2_c})
    print(pt2)
    # print(pt2.index)
    pt2.to_excel("./Excel/pt2.xlsx")
    # print(groups["产品类别"])

    # pt2["count"].hist(bins=100)
    # pt.plot.scatter(x="数量", y="金额")
    # plt.show()

    p3_groups = pt.groupby(["销售部门", "销售人员"])
    p3_sum = p3_groups["金额"].sum()
    p3_count = p3_groups["数量"].count()

    p3 = pd.DataFrame({"Sum": p3_sum, "Count": p3_count})
    print(p3)
    pt2.to_excel("./Excel/pt3.xlsx")


def work_performance():
    work = pd.read_excel("./Excel/MNC业务群2020年Q1绩效考核表-数字移动 - 移动业务交付部 - v.10.xlsx", skiprows=4)
    print(type(work))
    print(work.columns)
    work = work.loc[work["直接主管*"] == "林俊杰"]
    print(work)
    work.to_excel("绩效.xlsx")
    # print(work.loc[:,["C"]])


def working_time():
    # work = pd.read_excel("./Excel/HSBC业务线加班资源池-2020.xls", sheet_name="OT资源池", skiprows=2)
    # work = work.loc[(work["RM"] == "黄英") & (work["交付部"] == "移动业务交付部")]
    # work = work.loc[work["姓名"] == "张广洋"]
    # print(work)
    # work.to_excel("./Excel/OT.xlsx")

    ot = pd.read_excel("./Excel/OT.xlsx")
    ot = ot.loc[(ot["姓名"] == "林俊杰") | (ot["姓名"] == "戴国明") | (ot["姓名"] == "李彬特") | (ot["姓名"] == "黄文斌") | (ot["姓名"] == "陈洋平") | (ot["姓名"] == "张广洋")]
    print(ot)
    ot.to_excel("./Excel/our_ot.xlsx")


# hsbc_leave_file()
# hsbc_working_file()
# book_operation()
# student_compare()
# pbb_work()
# data_combine()
# book_data_validate()
# drop_duplicated()
# pivot_table()
# work_performance()
working_time()