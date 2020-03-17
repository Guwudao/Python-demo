from pyecharts.charts import Bar, Line
from pyecharts.options import InitOpts, TitleOpts, ToolboxOpts, LegendOpts, AxisOpts, LabelOpts

import matplotlib.pyplot as plt


def work_data_analysis(dtotal_data_list):
    # print(data_list[0])
    title_list = dtotal_data_list[0]
    working_list, leave_list, other_list = [], [], []

    for i in range(len(dtotal_data_list[0])):
        working_list.append(0)
        leave_list.append(0)
        other_list.append(0)

    is_skip_first = True
    for data_list in dtotal_data_list:

        if not is_skip_first:
            for index, data in enumerate(data_list):
                if data == "在家办公（WFH）" or data == "公司现场":
                    working_list[index] += 1
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

    for a, b, c, d in zip(working_list, leave_list, other_list, title_list):
        if a > 0:
            final_working_list.append(a)
            final_leave_list.append(b)
            final_other_list.append(c)
            final_title_list.append(d)

    print(final_working_list)
    print(final_leave_list)
    print(final_other_list)
    print(final_title_list)

    # fig, ax = plt.subplots()
    #
    # men_means = [20, 35, 30, 35, 27, 20, 35, 30, 35, 27, 20, 35, 30, 35, 27, 20, 35]
    # women_means = [25, 32, 34, 20, 25, 25, 32, 34, 20, 25, 25, 32, 34, 20, 25, 25, 32]
    # ax.bar(final_title_list, men_means, final_working_list, label="Working")
    # ax.bar(final_title_list, women_means, final_leave_list, label="Leave")
    # ax.bar(final_title_list, women_means, final_other_list, label="Other")
    #
    # ax.set_ylabel("Count")
    # ax.set_title("Statistical")
    #
    # ax.legend()
    # plt.show()

    working_analysis(final_title_list, final_working_list, final_leave_list, final_other_list)


def working_analysis(title_list, working_list, leave_list, other_list):
    bar = (
                Bar(
                    init_opts=InitOpts(page_title="中软汇丰业务线返工人数分析", width="1000px")
                )
                .add_xaxis(title_list)
                .add_yaxis("返工人数", working_list, stack="stack1", category_gap="50%")
                .add_yaxis("休假人数", leave_list, stack="stack1", category_gap="50%")
                .add_yaxis("其他人数", other_list, stack="stack1", category_gap="50%")
                .set_series_opts(label_opts=LabelOpts(is_show=False))
                .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True),
                                 title_opts=TitleOpts(title="业务线返工情况数据统计"),
                                 legend_opts=LegendOpts(),
                                 xaxis_opts=AxisOpts(axislabel_opts=LabelOpts(rotate=45)),
                                 )
                .render("开工情况_bar.html")
            )

    line = (
                Line(
                    init_opts=InitOpts(page_title="中软汇丰业务线返工人数分析", width="1000px")
                )
                .add_xaxis(title_list)
                .add_yaxis("返工人数", working_list)
                .add_yaxis("休假人数", leave_list)
                .add_yaxis("其他人数", other_list)
                .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True),
                                 title_opts=TitleOpts(title="业务线返工情况数据统计"),
                                 legend_opts=LegendOpts())
                .render("开工情况_line.html")
            )