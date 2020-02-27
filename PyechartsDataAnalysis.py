from pyecharts.charts import Bar, Line
from pyecharts.options import InitOpts, TitleOpts, ToolboxOpts, LegendOpts, AxisOpts, LabelOpts


def working_analysis(title_list, working_list, leave_list, other_list):
    bar = (
                Bar(
                    init_opts=InitOpts(page_title="中软汇丰业务线返工人数分析", width="1400px")
                )
                .add_xaxis(title_list)
                .add_yaxis("返工人数", working_list, stack="stack1")
                .add_yaxis("休假人数", leave_list, stack="stack1")
                .add_yaxis("其他人数", other_list, stack="stack1")
                .set_series_opts(label_opts=LabelOpts(is_show=False))
                .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True),
                                 title_opts=TitleOpts(title="业务线返工情况数据统计"),
                                 legend_opts=LegendOpts(),
                                 xaxis_opts=AxisOpts(axislabel_opts=LabelOpts(rotate=45))
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