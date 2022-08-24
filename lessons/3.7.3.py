'''
На вход программе первой строкой передаётся количество d известных нам слов,
после чего на d строках указываются эти слова.
Затем передаётся количество l строк текста для проверки,
после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке.
Работу производите без учёта регистра.


Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the

'''

a, a1 = [], []
for i in range(int(input())):
    a.append(input().lower())
for i in range(int(input())):
    a1 += input().lower().split()
for i in set(a1):
    if i not in a:
        print(i)
