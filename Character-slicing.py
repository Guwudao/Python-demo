
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

new = """
1. WeChat 许月英 【11人】
2. Staff App &VB 苟肖朋 【12】
3. MobileR & RBBLending 候梦璇 〔10人〕
4. Saas 谭立志 6人
5. MobileX & jade 林俊杰 【7人】
6. GBA QR 朱纯佳 10人
7. Mobile 1.5 胡超 6人
8. API 杨佳 【27人】
9. Mvtm 张璐 5人
10. Apollo8 陈少轩 【9人】
11. mobilex 李凯 14人
12. sMP 田晶/王杨 31人
13. Staff App & VB 苟肖朋 【12】
14. CCA 赵得华 10人
15. GBAOMP 谢研 12人
16. China Mobile +Mobile Foundation 周亚 【12】
17. Payment 苏俊 15人
18. GBA Macau 王腾/林健卜 11人
19. apollo7 刘昌旭 8人
"""

today = """
#接龙

02.21健康打卡情况
例 团队 TL 人数

1. MobileX & Jade 林俊杰【7人】
2. apollo7 刘昌旭 8人
3. WeChat  许月英【11人】
4. mvtm 张璐 【5人】
5. Payment 王勇【15人】
6. GBA Macau 王腾/林健卜 【11人】
7. Mobile 1.5 胡超 【6人】
8. Mobilex 李凯【14】
9. MobileR & RBBLending 候梦璇〔9人〕
10. China Mobile +Mobile Foundation 周亚  【12】
11. API 杨佳 【26】
12. 田晶/王杨 [28]
13. Apollo 8 陈少轩 【9人】
14. Saas 谭立志【6人】
15. GBA QR 朱纯佳【10人】
16. cca 赵得华 10人
17. Staff App&VB 苟肖朋 【12】
18. GBA OMP 谢研 12人"""


leader_list = ['许月英', '苟肖朋', '王勇', '周亚', '朱纯佳', '张璐', '胡超', '谭立志', '林俊杰', '李凯', '陈少轩', '杨佳', '田晶/王杨', '刘昌旭', '赵得华', '谢研', '候梦璇', '王腾/林健卜']

team_list = ['WeChat', 'Staff', 'Payment', 'China', 'GBA', 'MVTM', 'Mobile', 'Saas', 'MobileX', 'Mobilex', 'Apollo', 'API', 'SMP', 'louis', 'cca', 'GBA', 'MobileR', 'GBA']

def unclock_list(today):
    result_list = []
    for team, leader in zip(team_list, leader_list):
        # for today in today_list:
        if leader not in today:
            unclock = "未打卡：" + team + " " + leader
            result_list.append(unclock)
            # print(unclock)

    index = today.index("1.")
    new_today = today[index:]
    today_list = new_today.split("\n")
    sum = 0

    for t in today_list:
        team_separate = t.split(".")[1]
        num = re.findall(r"\d+\.?\d*", team_separate)

        if len(num) > 1:
            sum += int(num[1])
        sum += int(num[0])

    print(sum)
    print(result_list)
    return (result_list, sum)

remind_list = unclock_list(today)
# print(remind_list)


new_list =new.split("\n")

name_list = []
for n in new_list:
    # print(n)
    n_list = n.split(" ")
    name = n_list[-2]
    name_list.append(name)

    team = n_list[1]
    print(team)

    if name not in today:
        print("new leader: ", name)

    if team not in today:
        print("new team: ",   team)

print(name_list)
