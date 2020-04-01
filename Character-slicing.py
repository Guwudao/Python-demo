
# print(name[1:5:2])
# print(name[-1])
# name = "abcdabcdabcd"
#
# print(len(name))
# print(name[::-1])
# print(name[-4:-1:2])
# print(name[::2])
# print(name[-5:-1:1])
# print("-"*20)
#
# result = name.find("d")
# print(result)
# result1 = name.rfind("d")
# print(result1)
#
# result2 = name.index("d")
# print(result2)
# result3 = name.rindex("d")
# print(result3)
# print("-"*20)
#
# new_str = name.replace("a", "w", 4)
# print(new_str)

import re

new = """1. WeChat 许月英 【11人】
2. Staff App & VB 苟肖朋 【13】
3. GBA Macau 王腾/林健卜 11人
4. GBA QR 朱纯佳 10人
5. Payment 王勇 14人
6. Mvtm 张璐 4人
7. Apollo8 陈少轩 10人
8. apollo7 刘昌旭 9人
9. SaaS 赖淑茹 6人
10. MobileR & RBBLending 候梦璇 〔10人〕
11. mobilex 李凯 14
12. MobileX & jade 林俊杰 【7人】
13. GBAOMP 谢研 11人
14. SMP 田晶/王杨 32人
15. Mobile 1.5 胡超 6人
16. API 杨佳 【27人】
17. China Mobile +Mobile Foudation 周亚 【12】
18. CCA 赵得华 10人"""

today = """
#接龙
0401健康打卡

1. WeChat 许月英【11人】
2. Mvtm 张璐 4人
3. Staff App & VB 苟肖朋 【13】
4. Apollo8 陈少轩 10人
5. MobileX & jade 林俊杰 【7人】
6. GBA QR 朱纯佳 10人
7. Payment 王勇 14人
8. Mobile 1.5 胡超 6人
9. CCA 赵得华 10人
10. MobileR & RBBLending 候梦璇 〔10人〕
11. apollo7 刘昌旭 9人
12. SaaS 赖淑茹 6人
13. API 杨佳 【27人】
14. China Mobile +Mobile Foudation 周亚 【12】
15. GBAOMP 谢研 11人
16. mobilex 李凯 14
17. SMP 田晶/王杨 32人
"""


leader_list = ['许月英', '苟肖朋', '王勇', '周亚', '朱纯佳', '张璐', '胡超', '赖淑茹', '林俊杰', '李凯', '陈少轩', '杨佳', '田晶/王杨', '刘昌旭', '赵得华', '谢研', '候梦璇', '王腾/林健卜']

team_list = ['WeChat', 'Staff', 'Payment', 'China', 'GBA', 'MVTM', 'Mobile', 'SaaS', 'MobileX', 'Mobilex', 'Apollo', 'API', 'SMP', 'louis', 'cca', 'GBA', 'MobileR', 'GBA']

l_list = []
def get_leader_list(content) -> []:
    all_team = content.split("\n")
    # print(all_team)
    for team in all_team:
        team_detail = team.split(" ")
        print(team_detail)
        l_list.append(team_detail[-2])

    print(l_list)
    return l_list


def unclock_list(today):
    result_list = []
    for team, leader in zip(team_list, leader_list):
        if leader not in today:
            unclock = "未打卡：" + team + " " + leader
            result_list.append(unclock)
            # print(unclock)

    index = today.index("1.")
    new_today = today[index:]
    today_list = new_today.split("\n")
    sum = 0

    for t in today_list:
        t_list = t.split(".")
        if len(t_list) > 1:
            team_separate = t_list[1]
            num = re.findall(r"\d+\.?\d*", team_separate)

        if len(num) > 1:
            sum += int(num[1])
        sum += int(num[0])

    print(sum)
    print(result_list)
    return (result_list, sum)

remind_list = unclock_list(today)
# print(remind_list)

# get_leader_list(new)