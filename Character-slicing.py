
name = "abcdabcdabcd"

print(len(name))
print(name[1:5:2])
print(name[-1])
print(name[::-1])
print(name[-4:-1:2])
print(name[::2])
print(name[-5:-1:1])
print("-"*20)

result = name.find("d")
print(result)
result1 = name.rfind("d")
print(result1)

result2 = name.index("d")
print(result2)
result3 = name.rindex("d")
print(result3)
print("-"*20)

new_str = name.replace("a", "w", 4)
print(new_str)
