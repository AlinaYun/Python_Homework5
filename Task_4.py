#  Чисто для тренировки новый функций, ничего сложного. 
#   Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1. 
#   Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. 
#   Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
#   то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
#   Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
#  Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. 
#  С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

languages = ["python", "java", "C#", "javaScript", "PHP"]
numbers = [1, 2, 3, 4, 5]

def get_tuple (list1, list2):
    return list(zip(list1, map(str.upper,list2)))
    
def check_tuple(input_list):
    goals_list = []
    for i in input_list:
        summa = 0
        for j in i[1]:
            summa += ord(j)
        goals_list.append(summa)
    
    input_list = [list(x) for x in input_list]
    n = 0
    for i in input_list:
        if goals_list[n] % i[0] == 0:
            i[0] = goals_list[n]
            n += 1
        else:
            input_list.remove(i)
    input_list = [tuple(x) for x in input_list]
    return input_list

print(check_tuple(get_tuple(numbers, languages)))