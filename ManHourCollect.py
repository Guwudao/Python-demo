from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import re
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
    print("—————————————————— 牛🐂 Finish 逼 ——————————————————")
    print("备注：为方便校验，已将自动填充单元格标为红色\n")


def value_print(name, staff_id, value, coordinate, date):
    pass
    # print(name)
    # print(staff_id)
    # print(value)
    # print(coordinate)
    # print(date)
    # print("-" * 30)


def get_working_data():
    print("=" * 20 + " 开始数据过滤 " + "=" * 20)
    sheet = workingTime[working_time_sheet_name]
    working_data = []
    for row in sheet.rows:
        staff_id = row[2].value
        name = row[5].value
        for cell, date in zip(row, sheet["3"]):
            # print(cell.value)
            if cell.value is None:
                continue

            if type(cell.value) is str and len(cell.value) < 5:
                # column = re.findall(r"\d+", cell.value)
                column = "".join(filter(lambda c: ord(c) < 256, cell.value))
                # print(column)

                if "事" in cell.value:
                    # 事假
                    working_data.append((name, staff_id, column, "事假", date.value))
                    value_print(name, staff_id, column, "事假", date.value)
                elif "调" in cell.value:
                    # 调休
                    # working_data.append((name, staff_id, column, "调休", date.value))
                    value_print(name, staff_id, column, "调休", date.value)
                elif "年" in cell.value:
                    # 年假
                    working_data.append((name, staff_id, column, "年假", date.value))
                    value_print(name, staff_id, column, "年假", date.value)
                elif "婚" in cell.value:
                    # 婚假
                    working_data.append((name, staff_id, column, "婚假", date.value))
                    value_print(name, staff_id, column, "婚假", date.value)
                elif "产" in cell.value:
                    # 产假
                    working_data.append((name, staff_id, column, "产假", date.value))
                    value_print(name, staff_id, column, "产假", date.value)
                elif "哺" in cell.value:
                    # 哺乳假
                    working_data.append((name, staff_id, column, "哺乳假", date.value))
                    value_print(name, staff_id, column, "哺乳假", date.value)
                elif "病" in cell.value:
                    # 病假
                    working_data.append((name, staff_id, column, "病假", date.value))
                    value_print(name, staff_id, column, "病假", date.value)
                elif "丧" in cell.value:
                    # 丧假
                    working_data.append((name, staff_id, column, "丧假", date.value))
                    value_print(name, staff_id, column, "丧假", date.value)
                elif "检" in cell.value:
                    # 产检假
                    working_data.append((name, staff_id, column, "产检假", date.value))
                    value_print(name, staff_id, column, "产检假", date.value)
                elif "陪" in cell.value:
                    # 陪产假
                    working_data.append((name, staff_id, column, "陪产假", date.value))
                    value_print(name, staff_id, column, "陪产假", date.value)
    # print(working_data)
    return working_data


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

    template_path = "./Excel/导出工时明细0928.xlsx"
    template_sheet_name = "工时数据"
    working_time_path = "./Excel/9月请假明细.xlsx"
    working_time_sheet_name = "Sheet1"
    background_color = "FF0000"

    print(">" * 20 + " 开始导入Excel " + "<" * 20)
    workingTime = load_workbook(filename=working_time_path)
    template = load_workbook(filename=template_path)
    working_data = get_working_data()
    update_template(working_data)
