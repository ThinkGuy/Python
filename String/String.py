helloword = "hello World"
# 输出 helloWorld
print(helloword)

# 字符串拼接
print(helloword + "!!!")

# 字符串数组化
print(helloword[1:helloword.__len__()])
print(helloword[:3])
print(helloword[1:])

# 重复输出字符串
print(helloword * 2)

# in $ not in
print("a" in helloword)
print("a" not in helloword)
print("hello" not in helloword)
print("e" in helloword)

# 原始字符串 r/R 忽略转义字符
print("hello \n world")
print(r"hello \n world")

''' 字符串格式化 %
%s 字符串
%d 整形
%f 浮点数，可指定精度
'''
print("My name is %s and weight is %d kg" % ("liuxinwei", 21))

# API

# 仅第一个字符大写，其余小写
print(helloword.capitalize())

# 统计出现次数
print(helloword.count("l"))

# 最后判断
print(helloword.endswith("l"))

# 开始判断
print(helloword.startswith("h"))

# 查找
print(helloword.find("e"))

# 查找，找不到抛异常，不建议使用
print(helloword.index("e"))

# 字符串全部替换
print(helloword.replace("l", "a"))

# 字符串分隔符
print(helloword.split(" "))