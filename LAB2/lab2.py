from functools import partial
from collections import Counter, OrderedDict
from re import findall, compile, sub

freq_lang = { 'а': 0.05688278772138105, 'б': 0.014859120359571217, 'в': 0.030532916015332607, 'г': 0.016335284144120932, 'д': 0.023005873321472962, 'е': 0.0616890238170671,  'ж': 0.008106715500764193, 'з': 0.020988333431976352, 'и': 0.0002715584320633915, 'й': 0.015726018431158197, 'к': 0.03521729896842611, 'л': 0.0266040225463129, 'м': 0.03507629747485473, 'н': 0.05343956606355164, 'о': 0.09688369291615459, 'п': 0.015903575867507336, 'р': 0.04320216132659776, 'с': 0.05857828716259735, 'т': 0.05697504795791541, 'у': 0.03338427955199822, 'ф': 0.000738081892274859, 'х': 0.006888184074838719, 'ц': 0.001808648787909383, 'ч': 0.01609331861811573, 'ш': 0.0064860687042833124, 'щ': 0.0031455518380676182, 'ъ': 0.0003620779094178553, 'ы': 0.021373041210732826, 'ь': 0.02371958458522931, 'э': 0.0043327495987550094, 'ю': 0.008096270945684832, 'я': 0.03439914215387615}
amount_of_letters = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0}
AllComplianceIndex = {}
comp_indexx = {}
varints = {1: 'CryptedTextVariant1', 2: 'CryptedTextVariant2', 15: 'CryptedTextVariant15'}
varints_keys = {1: 'вшекспирбуря', 2: 'последнийдозор', 15: 'посняковандрей'}
m = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0}

def reSetAmountOfLetters():
    for k in amount_of_letters.keys():
        amount_of_letters[k] = 0

def SpliceText(length, file):  
    parts = []
    buff = ''
    with open(file, 'r', encoding='utf-8') as f:
        for ch in iter(partial(f.read, 1), ''):
            buff += ch
    for i in range(0, length):
        part = buff[i::length]
        parts.append(part)
    return parts

def count_let(file):
    with open(file, 'r', encoding='utf-8') as f:
        for char in iter(partial(f.read, 1), ''):
            amount_of_letters[char] += 1  

def comp_index(amount):
    sum = 0
    for k in amount_of_letters.keys():
        sum += amount_of_letters[k] * (amount_of_letters[k] - 1)
    ComplianceIndex = sum * (1/(amount - 1)) * (1/amount)
    return ComplianceIndex

def AllKeys(file):
    file += '.txt'
    part = []
    for kleng in range(2, 32):
        s = 0
        part = SpliceText(kleng, file)
        for i in part:
            AmountOfLetterInParts = 0
            reSetAmountOfLetters()
            for let in i:
                AmountOfLetterInParts += 1  
                amount_of_letters[let] += 1
                
            s += comp_index(AmountOfLetterInParts)
            
        AllComplianceIndex[kleng] = s/len(part)
    print(AllComplianceIndex)

def FindLengthOfKey():
    keys = []
    for leng, val in AllComplianceIndex.items():
        if val > 0.05:
            keys.append(leng)
    tval = 0.05
    while keys == []:
        for leng, val in AllComplianceIndex.items():
            if val > tval:
                keys.append(leng)
        tval -= 0.001
    return keys

def FindKeyByCommonLet(file, keyslen):
    file += '.txt'
    
    freq_lang_t = OrderedDict(sorted(freq_lang.items(), key=lambda t: t[1], reverse=True))
    freq_langg = {}
    for el in freq_lang_t:
        freq_langg[el] = freq_lang_t[el]
    pos_keys = []
    MostCommonLettersInParts = []
    for key in keyslen:
        part = SpliceText(key, file)
        key_letter = ''
        for i in range(0, key):
                
            freq_of_let = Counter(part[i])
            freq_of_let = OrderedDict(sorted(freq_of_let.items(), key=lambda t: t[1], reverse=True))
            freq_of_lets = {}
            for el in freq_of_let:
                freq_of_lets[el] = freq_of_let[el] / len(part[i])
                
            MostCommonLettersInParts.append(max(freq_of_lets, key=freq_of_lets.get))
            
        for let in freq_langg.keys():
            key = ''
            for mcl in MostCommonLettersInParts:
                key += getChar((getIndex(mcl)-getIndex(let)) % 32)
                
            pos_keys.append(key)
    return pos_keys


                

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
        print(f'Нет индекса для {ch}.')
    
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

def encrypt(ef = '', keyy = None, convertShow = True):
    try:
        ef += '.txt'
        if keyy == None:
            intLenOfKey = int(input('Введите длину ключа: '))
            print('Введите ключ: ', end = '')
            strKey = input()[:intLenOfKey]
        else:
            intLenOfKey = len(keyy)
            strKey = keyy
        listKey = list(map(str.lower, strKey))  
        intTextLen = 0 
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
                                intTextLen += 1
                            else:
                                fw.write('')
            except:
                print('Ошибка №2\nНе удалось записать данные в ModText2.txt.')
            try:
                with open('ModText2.txt', 'r', encoding = 'utf-8') as mtf:
                    count_let('ModText2.txt')
                    CompIndex = comp_index(intTextLen)
                    reSetAmountOfLetters()
                    comp_indexx['ModText2.txt'] = CompIndex
                    try:
                        with open(ef, 'w', encoding = 'utf-8') as etf:
                            for char in iter(partial(mtf.read, intLenOfKey), ''):
                                if len(char) == intLenOfKey:
                                    for i in range(intLenOfKey):
                                        if char[i] >= 'a' and char[i] <= 'я':
                                            newChar = getChar((getIndex(char[i]) + getIndex(listKey[i])) % 32)
                                            if convertShow:
                                                print(f'{char[i]} ==> {newChar}')
                                            etf.write(newChar)
                                else:
                                    for i in range(len(char)):
                                        if char[i] >= 'a' and char[i] <= 'я':
                                            newChar = getChar((getIndex(char[i]) + getIndex(listKey[i])) % 32)
                                            if convertShow:
                                                print(f'{char[i]} ==> {newChar}')
                                            etf.write(newChar)
                        
                        count_let(ef)    
                        CompIndex = comp_index(intTextLen)
                        reSetAmountOfLetters()
                        print('KEY =', strKey)
                        print('N =', intTextLen)
                        print('Compliance Index =', CompIndex)
                        comp_indexx[ef] = CompIndex

                    except:
                        print('Ошибка №3\nНе удалось записать данные в EncText2.txt.')
            except:
                print('Ошибка №4\nНе удалось считать данные с ModText2.txt.')            
    except:
        print('Ошибка №5\nНе удалось считать данные с text2.txt.')

def M(g):
    sum = 0
    for let in freq_lang.keys():
        sum += freq_lang[let] * amount_of_letters[getChar((getIndex(g)+getIndex(let)) % 32)]
    m[g] = sum
    
def FindKeyByM(file, keyslen):
    file += '.txt'
    for key in keyslen:
        part = SpliceText(key, file)
        key_letter = ''
        for i in range(0, key):
            reSetAmountOfLetters()
            for j in part[i]:
                amount_of_letters[j] += 1
            for k in freq_lang.keys():
                M(k)  
            maxx = m['о']
            letindex = 0
            for i in m.keys():
                if maxx < m[i]:
                    maxx = m[i]
                    letindex = getIndex(i)
            key_letter += getChar(letindex)
        return key_letter

def decrypt(key, variant, convertShow = True):
    print('KEY =', key)
    key = list(key)
    variant += '.txt'
    with open(variant, 'r', encoding='utf-8') as f:
        with open('decrtext.txt', 'w',  encoding='utf-8') as w:
            for char in iter(partial(f.read, len(key)), ''):
                if len(char) == len(key):
                    for i in range(len(key)):
                        if char[i] >= 'a' and char[i] <= 'я':
                            newChar = getChar((getIndex(char[i]) + 32 - getIndex(key[i])) % 32)
                            if convertShow:
                                print(f'{newChar} <== {char[i]}')
                            w.write(newChar)
                else:
                    for i in range(len(char)):
                        if char[i] >= 'a' and char[i] <= 'я':
                            newChar = getChar((getIndex(char[i]) + 32 - getIndex(key[i])) % 32)
                            if convertShow:
                                print(f'{newChar} <== {char[i]}')
                            w.write(newChar)

def main(): 
    encrypt('Enc2Text2',  'да', False)
    encrypt('Enc3Text2',  'нет', False)
    encrypt('Enc4Text2',  'пока', False)
    encrypt('Enc5Text2',  'тесла', False)
    encrypt('Enc10Text2', 'абитуриент', False)
    encrypt('Enc11Text2', 'абонентский', False)
    encrypt('Enc12Text2', 'абонементный', False)
    encrypt('Enc13Text2', 'млекопитающие', False)
    encrypt('Enc14Text2', 'безобразничать', False)
    encrypt('Enc15Text2', 'безостановочный', False)
    encrypt('Enc16Text2', 'времяпровождение', False)
    encrypt('Enc17Text2', 'контрреволюционер', False)
    encrypt('Enc18Text2', 'сверхъестественный', False)
    encrypt('Enc19Text2', 'усовершенствоваться', False)
    encrypt('Enc20Text2', 'женоненавистничество', False)
    print(comp_indexx)
    var = 15
    AllKeys(varints[var])
    lengg = FindLengthOfKey()
  
    print(lengg)
    key = FindKeyByCommonLet(varints[var], lengg)
    print(key)
    key = FindKeyByM(varints[var], lengg)
    print(key)
    key = varints_keys[var]

    #decrypt(key, varints[var], False)

if __name__ == "__main__":
    main()
    