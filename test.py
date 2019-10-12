
#BMI = 体重kg / 身高 * 身高（m）
#体脂率 = 1.2 * BMI + 0.23 * 年龄 - 0.54 - 10.8 * 性别（男1.女0）/ 100

name = input("请输入姓名 ")
age = int(input("请输入年龄 "))
height = float(input("请输入身高(m) "))
if height > 10:
    height = height/100

weight = float(input("请输入体重(kg) "))
gender = input("请输入性别 ")
gender = 1 if gender == "男" else 0

BMI = weight / (height * height)
body_fat = (1.2 * BMI + 0.23 * age - 0.54 - 10.8 * gender) / 100


body_fat_rate = ((0.25, 0.28), (0.15, 0.18))
min_fat, max_fat = body_fat_rate[gender]

result = "正常"
if body_fat < min_fat:
    result = "偏瘦"
elif body_fat > max_fat:
    result = "偏胖"


# print(name, age, height, weight, gender)

print("BMI = %f" % BMI, "体脂率 = %f" % body_fat)
print("您的体重属于%s" % result)
