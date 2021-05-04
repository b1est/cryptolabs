from collections import Counter  
from functools import partial
import math
variant = 15
variants = {2: "02.txt", 15: "15.txt"}

most_coommon_bigram_in_lang = ['ст', 'но', 'ен', 'то', 'на', 'ов', 'ни', 'ра', 'во', 'ко']
pos_keys=[]
m = 31
m2 = m*m
#1
def extended_euclid(a, b):                                  # Розширений алгоритм Евкліда
    if not b:
        return (1, 0, a)
    y, x, g = extended_euclid(b, a % b)
    return (x, y - (a // b) * x, g)
def linear_comparison(a, b, n):                             # Розв’язки лінійних порівнянь
    x, g = extended_euclid(a, n)[0], extended_euclid(a, n)[2]
    if g == 1:
        return (x * b) % n
    elif g > 1:
        if b % g != 0:
            return None
        else:
            a, b, n = a // g, b // g, n // g
            x0 = extended_euclid(a, n)[0]
            X = []
            for i in range(1, g):
                X.append(x0)
                x0 = x0 + i * n
            return X
    else:
        print('Bugs\nBugs everywhere!!!')
#2
def BigramFreq():
    f = {}
    with open(variants[variant], 'r', encoding = "utf-8") as r:
        for char in iter(partial(r.read, 2), ''):
            if not char in f.keys():
                f[char] = 1
            else:
                f[char] += 1
    return f
   
    
def MostCommon(A, n, func = True):
    most_coommon_bigram_in_cyphertext = {}
    if isinstance(A, dict):
        most_coommon_bigram_in_cyphertext= dict(Counter(A).most_common(n))
        most_coommon_bigram_in_cyphertext_key = list(most_coommon_bigram_in_cyphertext.keys()) 
        if func == True:
            print(f'{n} найчастіших біграм запропонованого шифртексту: {most_coommon_bigram_in_cyphertext_key}')
        return most_coommon_bigram_in_cyphertext_key
#3
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
    elif ch == 'ь':
        return 26
    elif ch == 'ы':
        return 27
    elif ch == 'э':
        return 28
    elif ch == 'ю':
        return 29
    elif ch == 'я':
        return 30
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
    elif i == 27:
        return 'ы'
    elif i == 26:
        return 'ь'
    elif i == 28:
        return 'э'
    elif i == 29:
        return 'ю'
    elif i == 30:
        return 'я'
    else:
        print('Нет буквы для введенного индекса.')
def BiValBigMacker(bigram):
    tmp = []
    for gr in bigram:
        tmp.append(m*getIndex(gr[0]) + getIndex(gr[1]))
    return tmp

def ValToBigram(bigram):
    big = ''
    second = bigram%m
    first = math.floor((bigram-second)/m)
    big += getChar(first)
    big += getChar(second)
    return big

def keys_find(lang, cypher, pos_keys):
    most_coommon_bigram_in_lang_list = []
    most_coommon_bigram_in_cyphertext_list = []
    for i in range(len(lang)):
        most_coommon_bigram_in_lang_list.append(m*getIndex(lang[i][0])+getIndex(lang[i][1]))
    for i in range(len(cypher)):
        most_coommon_bigram_in_cyphertext_list.append(m*getIndex(cypher[i][0])+getIndex(cypher[i][1]))
    for lang1 in range(0, len(lang)-1):
        for cypher1 in range(0, len(cypher)):
            for lang2 in range(lang1+1, len(lang)):
                for cypher2 in range(0, len(cypher)):
                    if cypher2 == cypher1:
                        continue
                    x = most_coommon_bigram_in_lang_list[lang1] - most_coommon_bigram_in_lang_list[lang2]
                    y = most_coommon_bigram_in_cyphertext_list[cypher1] - most_coommon_bigram_in_cyphertext_list[cypher2]
                    r = linear_comparison(x, y, m2)
                    if isinstance(r, int):
                        if r > 0 and r < m2 and extended_euclid(r, m)[2] == 1:
                            b = most_coommon_bigram_in_cyphertext_list[cypher1] - r * most_coommon_bigram_in_lang_list[lang1] % m2
                            key = (r, b)
                            if b >= 0 and b < m2:
                                pos_keys.append(key)
                    if isinstance(r, list):
                        for a in r:
                            if a > 0 and a < m2 and extended_euclid(a, m)[2] == 1:
                                b = most_coommon_bigram_in_cyphertext_list[cypher1] - a * most_coommon_bigram_in_lang_list[lang1] % m2
                                key = (a, b)
                                if b >= 0 and b < m2:
                                    pos_keys.append(key)
    pos_keys = list(set(pos_keys))
    return pos_keys
   

def decr(keys):
    impossible_russian_bigrams = ["аь", "оь", "еь", "иь", "уь", "оь", "щй", "щф", "щх", "щц", "щч", "щш", "щщ"]
    impossible_russian_bigrams_val = BiValBigMacker(impossible_russian_bigrams)
    bigramtext = []
    
    with open(variants[variant], 'r', encoding='utf-8') as v:
        for char in iter(partial(v.read, 2), ''):
                bigramtext.append(char)
    bigramtext_val = BiValBigMacker(bigramtext)
    with open('decryption.txt', 'w', encoding='utf-8') as w:
        for i in keys:
            w.write(f'\nKEY: {i}\n')
            a, b = i
            dtext = ''
            opp_a = extended_euclid(a, m*m)[0]
            for j in range(len(bigramtext_val)):
                bigram_value = opp_a * (bigramtext_val[j] - b ) % m2
                bigram = ValToBigram(bigram_value)
                if bigram_value in impossible_russian_bigrams_val:
                    w.write(f"Знайдено неможливу біграму: {bigram}\n")
                    dtext += bigram
                    break
                else:
                    dtext += bigram
                if j == len(bigramtext_val)-1:
                    if list(x[0] for x in Counter(dtext).most_common(3)) == ['о', 'а', 'е']:
                        w.write('Разшифрованый текст:\n'+ dtext)    
                    elif list(x[0] for x in Counter(dtext).most_common(2)) == ['о', 'а']:
                        w.write('Разшифрованый текст:\n'+ dtext)   
                    elif list(x[0] for x in Counter(dtext).most_common(1)) == ['о']:
                        w.write('Разшифрованый текст:\n'+ dtext)
                    else:
                        w.write(f'Помилка частотного аналізу: {list(x[0] for x in Counter(dtext).most_common(5))}')
            w.write(dtext)      
                    





                    
                
                         

def main(): 
    bigram_in_cyphertext = BigramFreq()
    most_coommon_bigram_in_cyphertext = MostCommon(bigram_in_cyphertext, 10)
    keys = keys_find(most_coommon_bigram_in_lang, most_coommon_bigram_in_cyphertext, pos_keys)
    decr(keys)
    
if __name__ == '__main__':
    main()