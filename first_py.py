#Главнаяg ветка
# Задание 6.1
print("№1")
s = "Hello, World!"
print("Первый символ:", s[0])
print("Последний символ:", s[-1])
print("Подстрока 'World':", s[7:12])
print()

# Задание 6.2
print("№2")
text = input("Введите строку: ")
if len(text) % 2 == 0:
    print(text.upper())
else:
    print(text.lower())
print()

# Задание 6.3
print("№3")
text = input("Введите строку: ")
lw = "aeiou"
up = "AEIOU"
cl = 0
cu = 0
for r in text:
    if r in lw:
        cl += 1
    elif r in up:
        cu += 1
print("Строчных гласных:", cl)
print("Заглавных гласных:", cu)
print()

# Задание 6.4
print("№4")
text = input("Введите строку: ")
if len(text) > 0:
    result = text[0]
    for r in text[1:]:
        if r != result[-1]:
            result += r
else:
    result = ""
print(result)
print()

# Задание 6.5
print("№5")
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
if sorted(word1.lower()) == sorted(word2.lower()):
    print(True)
else:
    print(False)