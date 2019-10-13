
#BMI = 体重kg / 身高 * 身高（m）
#体脂率 = 1.2 * BMI + 0.23 * 年龄 - 0.54 - 10.8 * 性别（男1.女0）/ 100


class Person:
    def __init__(self, name, age, height, weight, gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

        try:
            if isinstance(age, str):
                self.age = int(age)

            if isinstance(height, str):
                self.height = float(height)
                if self.height > 10:
                    self.height = self.height / 100

            if isinstance(weight, str):
                self.weight = float(weight)

            if gender in ("男", "女"):
                self.gender = 1 if gender == "男" else 0

        except Exception:
            raise Exception("请输入正确格式")

    @property
    def get_body_fat(self):
        bmi = self.weight / (self.height * self.height)
        body_fat = (1.2 * bmi + 0.23 * self.age - 0.54 - 10.8 * self.gender) / 100

        body_fat_scop = ((0.25, 0.28), (0.15, 0.18))
        min_fat, max_fat = body_fat_scop[self.gender]

        result = "正常"
        if body_fat < min_fat:
            result = "偏瘦"
        elif body_fat > max_fat:
            result = "偏胖"
        print("BMI = %f" % bmi, "体脂率 = %f" % body_fat)

        result_str = "{} 您好，您的体脂率是{}, 正常体脂率的范围是{} - {}, 您的体型属于{}".format(self.name, body_fat, min_fat, max_fat, result)

        return result_str


name = input("请输入姓名 ")
age = input("请输入年龄 ")
height = input("请输入身高(m) ")
weight = input("请输入体重(kg) ")
gender = input("请输入性别 ")

p = Person(name, age, height, weight, gender)
print(p.age)
print(p.name)
print(p.get_body_fat())

