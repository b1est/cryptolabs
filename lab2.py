from functools import partial

def getIndex(ch):
    if ch == 'а':
        return 0
    elif ch == 'б': 
        return 1
    elif ch == 'в':
        return 2
    elif ch == 'г':
        return 3
    elif ch == 'д':
        return 4
    elif ch == 'е':
        return 5
    elif ch == 'ж':
        return 6
    elif ch == 'з':
        return 7
    elif ch == 'и':
        return 8
    elif ch == 'й': 
        return 9
    elif ch == 'к':
        return 10
    elif ch == 'л':
        return 11
    elif ch == 'м':
        return 12
    elif ch == 'н':
        return 13
    elif ch == 'о':
        return 14
    elif ch == 'п': 
        return 15
    elif ch == 'р':
        return 16
    elif ch == 'с':
        return 17
    elif ch == 'т':
        return 18 
    elif ch == 'у':
        return 19
    elif ch == 'ф':
        return 20
    elif ch == 'х': 
        return 21
    elif ch == 'ц':
        return 22
    elif ch == 'ч':
        return 23
    elif ch == 'ш':
        return 24
    elif ch == 'щ': 
        return 25
    elif ch == 'ъ':
        return 26
    elif ch == 'ы':
        return 27
    elif ch == 'ь':
        return 28
    elif ch == 'э':
        return 29
    elif ch == 'ю':
        return 30
    elif ch == 'я':
        return 31
    else:
        print('Нет индекса для введенной буквы.')
    
def getChar(i):
    if i == 0:
        return 'а'
    elif i == 1: 
        return 'б'
    elif i == 2:
        return 'в'
    elif i == 3:
        return 'г'
    elif i == 4:
        return 'д'
    elif i == 5:
        return 'е'
    elif i == 6:
        return 'ж'
    elif i == 7:
        return 'з'
    elif i == 8:
        return 'и'
    elif i == 9: 
        return 'й'
    elif i == 10:
        return 'к'
    elif i == 11:
        return 'л'
    elif i == 12:
        return 'м'
    elif i == 13:
        return 'н'
    elif i == 14:
        return 'о'
    elif i == 15: 
        return 'п'
    elif i == 16:
        return 'р'
    elif i == 17:
        return 'с'
    elif i == 18:
        return 'т'
    elif i == 19:
        return 'у'
    elif i == 20:
        return 'ф'
    elif i == 21: 
        return 'х'
    elif i == 22:
        return 'ц'
    elif i == 23:
        return 'ч'
    elif i == 24:
        return 'ш'
    elif i == 25: 
        return 'щ'
    elif i == 26:
        return 'ъ'
    elif i == 27:
        return 'ы'
    elif i == 28:
        return 'ь'
    elif i == 29:
        return 'э'
    elif i == 30:
        return 'ю'
    elif i == 31:
        return 'я'
    else:
        print('Нет буквы для введенного индекса.')

def encrypt():
    try:
        intLenOfKey = int(input('Введите длину ключа: '))
        print('Введите ключ: ', end = '')
        listKey = list(map(str.lower, input()[:intLenOfKey]))
    except:
        print('Ошибка №1\nПроверьте введенные данные.')
    try:
        with open('text2.txt', 'r', encoding = 'utf-8') as f:
            try:
                with open('ModText2.txt', 'w', encoding = 'utf-8') as fw:
                    for char in iter(partial(f.read, 10), ''):
                        for i in char:
                            if i.lower() >= 'a' and i.lower() <= 'я':
                                fw.write(i.lower())
                            else:
                                fw.write('')
            except:
                print('Ошибка №2\nНе удалось записать данные в ModText2.txt.')
            try:
                with open('ModText2.txt', 'r', encoding = 'utf-8') as mtf:
                    try:
                        with open('EncText2.txt', 'w', encoding = 'utf-8') as etf:
                            for char in iter(partial(mtf.read, intLenOfKey), ''):
                                if char == intLenOfKey:
                                    for i in range(intLenOfKey):
                                        if char[i] >= 'a' and char[i] <= 'я':
                                            newChar = getChar((getIndex(char[i]) + getIndex(listKey[i])) % 32)
                                            print(f'{char[i]} ==> {newChar}')
                                            etf.write(newChar)
                                else:
                                    for i in range(len(char)):
                                        if char[i] >= 'a' and char[i] <= 'я':
                                            newChar = getChar((getIndex(char[i]) + getIndex(listKey[i])) % 32)
                                            print(f'{char[i]} ==> {newChar}')
                                            etf.write(newChar)  
                    except:
                        print('Ошибка №3\nНе удалось записать данные в EncText2.txt.')
            except:
                print('Ошибка №4\nНе удалось считать с ModText2.txt.')            
    except:
        print('Ошибка №5\nНе удалось считать с text2.txt.')

def main():
    encrypt()
    
if __name__ == "__main__":
    main()
    