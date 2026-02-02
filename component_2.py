single_quoted_str = 'Привет, мир!'
double_quoted_str = "Hello, world!"

large_str = """привет как
твои дела
чем ты занят?"""

single_str = "Привет \n как твои дела" # В месте \n будет перенос на новую строку

text = Python
slice1 = text[1:4]
print(slice1)  # Вывод: "yth"

slice2 = text[:3]
print(slice2)  # Вывод: "Pyt"

slice3 = text[3:]
print(slice3)  # Вывод: "hon"

slice4 = text[::-1]
print(slice4)  # Вывод: "nohtyP"

slice5 = text[::2]
print(slice5)  # Вывод: "Pto"

text = "Python"
length = len(text)  # Получаем длину строки, в данном случае length = 6

str1 = "Hello, "
str2 = "world!"
result = str1 + str2  # Получаем "Hello, world!"

