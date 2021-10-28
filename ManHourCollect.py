from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from pyecharts.charts import Bar, Pie
from pyecharts.options import InitOpts, TitleOpts, ToolboxOpts
import sys

WARNING_STRING = """
-> 请确保请假考勤按以下格式填写，如：
-> 事假: 事8
-> 调休: 调8
-> 年假: 年8
-> 婚假: 婚8
-> 产假: 产8
-> 哺乳假: 哺8
-> 病假: 病8
-> 丧假: 丧8
-> 产检假: 检8
-> 陪产假: 陪8
"""

TIPS_STRING = """
-> 输入格式有误，请从上往下依次输入，中间空格隔开
-> python
-> ManHourCollect.py
-> 统计工时文件路径名称，如：./Excel/出勤信息-2021Daisy0812.xlsx
-> 统计工时表单（sheet）名称，如：8月（总）
-> 模板文件路径名称，如：./Excel/导出工时明细.xlsx
-> 模板工时表单（sheet）名称，如：工时数据

--> 最终样式模板：python ManHourCollect.py ./Excel/出勤信息-2021Daisy0812.xlsx 8月（总） ./Excel/导出工时明细.xlsx 工时数据
"""

def chart_generation(data_list, title):
    pie_city = (
        Pie(init_opts=InitOpts(
            page_title=title,
            width="1400px",
            height="800px",
        ))
        .add(
            data_pair=data_list,
            series_name=title,
            radius=["25%", "75%"],
            rosetype="radius"
        )
        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True, pos_top="50px"),
                             title_opts=TitleOpts(title=title, pos_top="80px", pos_left="200px"))
        .render(f"{title}_pie.html")
    )

    type_list = [i for i, j in data_list]
    hour_list = [j for i, j in data_list]

    bar_sex = Bar(init_opts=InitOpts(page_title=title))
    bar_sex.add_xaxis(type_list)
    bar_sex.add_yaxis("请假类型", hour_list)
    bar_sex.set_global_opts(title_opts=TitleOpts(title=title, pos_left="200"))
    bar_sex.render(f"{title}_bar.html")


def update_template(working_data):
    sheet = template[template_sheet_name]
    print(">" * 20 + " 开始自动关联填写 " + "<" * 20)
    for (name, staff_id, hour, type, date) in working_data:
        # print(name, hour, type, date)

        for row in sheet.rows:
            target_staff_id = row[2].value
            working_type = row[6].value
            if target_staff_id != staff_id or working_type != type:
                continue

            for cell, working_date in zip(row, sheet["1"]):
                day = working_date.value.split("-")[-1]

                if target_staff_id == staff_id and day.isdigit() and int(day) == int(date):
                    # print(staff_name)
                    pattern_fill = PatternFill(fill_type="solid", fgColor=background_color)
                    cell.fill = pattern_fill
                    cell.value = float(hour)
                    # print("-" * 30)
                    print(f"{name} {working_date.value} {type} {hour} 小时 已自动导入")

    template.save(filename=template_path)
    print(f"\n——————————— 已自动导入 {len(working_data)} 条请假数据 ———————————")
    print("🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂🐂")
    print("——————————————— 牛🐂finish🐂逼 ———————————————")
    print("备注：为方便校验，已将自动填充单元格标为 &>> 紫色 <<&\n")


def get_working_data():
    print("=" * 20 + " 开始数据分析过滤 " + "=" * 20)
    sheet = workingTime[working_time_sheet_name]
    shiJia, tiaoXiu, nianJia, hunJia, chanJia, buRuJia, bingJia, sangJia, chanJianJia, peiChanJia = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for row in sheet.rows:
        staff_id = row[2].value
        name = row[5].value
        for cell, (index, date) in zip(row, enumerate(sheet[2])):
            # print(cell.value, index, date.value)
            if index < 8:  # 前7列非请假数据自动跳过
                continue

            if type(cell.value) is str and len(cell.value) >= 5:
                exception_data.append((name, date.value, cell.value))

            if type(cell.value) is str and len(cell.value) < 5:
                # column = re.findall(r"\d+", cell.value)
                column = "".join(filter(lambda c: ord(c) < 256, cell.value))
                # print(column)

                count_zh = 0
                for s in cell.value:
                    if s.isalpha():
                        count_zh += 1

                if count_zh >= 2:  # 混合类型假期
                    exception_data.append((name, date.value, cell.value))
                    continue

                if "事" in cell.value:
                    # 事假
                    shiJia += float(column)
                    working_data.append((name, staff_id, column, "事假", date.value))
                elif "调" in cell.value:
                    # 调休
                    # working_data.append((name, staff_id, column, "调休", date.value))
                    tiaoXiu += float(column)
                    pass
                elif "年" in cell.value:
                    # 年假
                    nianJia += float(column)
                    working_data.append((name, staff_id, column, "年假", date.value))
                elif "婚" in cell.value:
                    # 婚假
                    hunJia += float(column)
                    working_data.append((name, staff_id, column, "婚假", date.value))
                elif "产" in cell.value:
                    # 产假
                    chanJia += float(column)
                    working_data.append((name, staff_id, column, "产假", date.value))
                elif "哺" in cell.value:
                    # 哺乳假
                    buRuJia += float(column)
                    working_data.append((name, staff_id, column, "哺乳假", date.value))
                elif "病" in cell.value:
                    # 病假
                    bingJia += float(column)
                    working_data.append((name, staff_id, column, "病假", date.value))
                elif "丧" in cell.value:
                    # 丧假
                    sangJia += float(column)
                    working_data.append((name, staff_id, column, "丧假", date.value))
                elif "检" in cell.value:
                    # 产检假
                    chanJianJia += float(column)
                    working_data.append((name, staff_id, column, "产检假", date.value))
                elif "陪" in cell.value:
                    # 陪产假
                    peiChanJia += float(column)
                    working_data.append((name, staff_id, column, "陪产假", date.value))

    print(f"事假共 {shiJia} 小时，\n调休共 {tiaoXiu} 小时，\n年假共 {nianJia} 小时，\n婚假共 {hunJia} 小时，\n产假共 {chanJia} 小时，"
          f"\n哺乳假共 {buRuJia} 小时，\n病假共 {bingJia} 小时，\n丧假共 {sangJia} 小时，\n产检假共 {chanJianJia} 小时，\n陪产假共 {peiChanJia} 小时")
    # print(working_data)
    data_list = [("事假", shiJia), ("调休", tiaoXiu), ("年假", nianJia), ("婚假", hunJia), ("产假", chanJia),
                 ("哺乳假", buRuJia), ("病假", bingJia), ("丧假", sangJia), ("产检假", chanJianJia), ("陪产假", peiChanJia)]
    chart_generation(data_list, chart_title)
    return data_list


def help_tips(s):
    sys.stderr.write(s)
    sys.stderr.write("\n")
    sys.stderr.flush()


if __name__ == '__main__':
    print("+" * 50)
    # help_tips(WARNING_STRING)
    #
    # if len(sys.argv) != 5:
    #     help_tips(TIPS_STRING)
    #     exit(404)

    template_path = "./Excel/导出工时明细1028.xlsx"
    template_sheet_name = "工时数据"
    working_time_path = "./Excel/10月请假明细给JJ.xlsx"
    working_time_sheet_name = "Sheet1"
    background_color = "9933cc"
    chart_title = "10月请假数据分析"

    working_data = []
    exception_data = []

    print(">" * 20 + " 开始导入Excel " + "<" * 20)
    workingTime = load_workbook(filename=working_time_path)
    template = load_workbook(filename=template_path)

    get_working_data()
    update_template(working_data)
    print(f"无法处理数据 {len(exception_data)} 条，需手动校正：")
    for data in exception_data:
        print(data)
