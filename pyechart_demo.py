from pyecharts.charts import Bar

list = [('深圳', 117), ('广州', 191), ('', 163), ('湛江', 88), ('郑州', 11), ('杭州', 7), ('东莞', 7), ('佛山', 14), ('长沙', 6), ('西安', 14), ('成都', 7), ('武汉', 5)]
city = []
count = []

list.sort(key=lambda x: x[1])
list.reverse()
print(list)

for i, j in list:
    if len(i):
        city.append(i)
        count.append(j)

# print(city, count)

bar = Bar()
bar.add_xaxis(city)
bar.add_yaxis("微信好友地区数量统计", count)

bar.render()
