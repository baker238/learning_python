'''
names = ['Вася','Петя','Витя','Кирилл']
i=0
while names[i] !='Витя':
    i +=1
print(f'{names.pop(i)} нашелся')
'''


'''
names = ['Вася','Петя','Витя','Кирилл']
i=0 
person_ask = input('Индекс какого имени желаете найти?')
def find_name(name):
    for i in range(len(name)):
        if name[i] == person_ask:
            print(f'индекс имени {person_ask}: {i}')
        else:
            i = i+1
    if i==4:
        print('Такого имени в списке нет')

find_name(names)
'''


def ask_user(question):
    while question.lower() !='хорошо':
        question= input('Как дела?')

ask_user(input('Как дела?'))