'''
Напишите программу, которая считывает текст из файла
(в файле может быть больше одной строки) и выводит самое частое слово в этом тексте
и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое
'''

with open('E:/dataset_3363_3.txt', 'r') as input_info:
    text_string = ' '.join([x.lower() for x in input_info])
    print(text_string)
    list_text = list(text_string.split())
    max_count = 0
    find_word = ''
    for word in list_text:
        if list_text.count(word) > max_count:
            max_count = list_text.count(word)
            find_word = word

    print(find_word, max_count)
