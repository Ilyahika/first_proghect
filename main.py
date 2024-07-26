# Функциональный стиль програмирования
#
# # map() --- Заменя циклу For
lst = ["1", "2", "3"] # [1, 2, 3]
int_lst = []
for number in lst:
    int_lst.append(int(number))
# print(lst)
# print(int_lst)
# # ------------------------------------------------------
gen_lst = [int(number) for number in lst]
# ------------------------------------------------------
# 1. Создаем переменную
# 2. Вызвать фуекцию map() внутри переменной
# 3. Внутри функции map() Указываем с какими переменными мы работем
# 3. Внутри функции map() Указываем что применить к элементам списка
# ------------------------------------------------------
map_lst = map(int ,lst)
print(list(map_lst))
# ----------------------------------------------------
names = ["dior", "muhammad", "sanjar"]
map_names = map(str.capitalize, names)
print(list(map_names))
# # ----------------------------------------------------
def double_number(number: int):
    return number ** 2
lst = [23, 42, 55, 52, 63]
map_lst = map(double_number, lst)
print(list(map_lst))
# -------------------------------------------------------


# filter() --- фильтрует


les_5 = []
more_5 = []
for i in words:
    if len(i) <= 5:
        les_5.append(i)
    else:
        more_5.append(i)
print(les_5)
print(more_5)
words = ["purole", "yellow", "prange", "windows", "nokia", "apple", "transformer"
         "not", "code", "ban"]
# # ------------------------------------------------------------
def check(word):
    return len(word) <= 5
filter_lst = filter(check, words)
print(list(filter_lst))

words = ["apple", "align", "alive", "after", "assembler", "byd", "banana", "braziliya", "brabus", "brain", "bentley"]
def oper(word):
    return word.startswith("a")

filtered = filter(oper, words)
print(list(filtered))

# Git, Github

