'''
Программа должна считывать одну строку со стандартного ввода и выводить
для каждого уникального слова в этой строке число его повторений (без учёта регистра)
 в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово
должно выводиться только один раз.

 Sample Input 1:
a aa abC aa ac abc bcd a

Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2

'''

input_str = list(input().lower().split())

dict_ ={}
for el in input_str:
    if input_str.count(el) > 1:
        if el not in dict_:
            count = input_str.count(el)
            dict_.update({el: count})
        else:
            pass
    elif el in dict_:
        pass
    else:
        dict_.update({el: 1})

for v, k in dict_.items():
    print(v, k)