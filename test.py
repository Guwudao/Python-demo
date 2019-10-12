
#BMI = 体重kg / 身高 * 身高（m）
#体脂率 = 1.2 * BMI + 0.23 * 年龄 - 0.54 - 10.8 * 性别（男1.女0）/ 100

name = input("请输入姓名 ")
age = input("请输入年龄 ")
height = input("请输入身高(m) ")
weight = input("请输入体重(kg) ")
gender = input("请输入性别 ")


def getBodyFatRate(name, age, height, weight, gender):

    try:
        if isinstance(age, str):
            age = int(age)

        if isinstance(height, str):
            height = float(height)
            if height > 10:
                height = height / 100

        if isinstance(weight, str):
            weight = float(weight)

        if gender in ("男", "女"):
            gender = 1 if gender == "男" else 0

    except Exception:
        return "请正确输入"


    bmi = weight / (height * height)
    body_fat = (1.2 * bmi + 0.23 * age - 0.54 - 10.8 * gender) / 100

    body_fat_scop = ((0.25, 0.28), (0.15, 0.18))
    min_fat, max_fat = body_fat_scop[gender]

    result = "正常"
    if body_fat < min_fat:
        result = "偏瘦"
    elif body_fat > max_fat:
        result = "偏胖"
    print("BMI = %f" % bmi, "体脂率 = %f" % body_fat)

    resultStr = "{} 您好，您的体脂率是{}, 正常体脂率的范围是{} - {}, 您的体型属于{}".format(name, body_fat, min_fat, max_fat, result)

    return resultStr


result = getBodyFatRate(name, age, height, weight, gender)

print(result)
