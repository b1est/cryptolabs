import math
from collections import Counter, OrderedDict
import pandas as pd
import numpy as np
import re
import os
def TableMacker(data):  
    data =  dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    table = {}
    for key, val in data.items():
        table[key] = [val]
    keysData = data.keys()
    table = pd.DataFrame(data = table, dtype = np.float64, columns = keysData)
    print(f"Таблица частот: \n {table}")
    if os.stat("table1.csv").st_size == 0:
        table.to_csv("table1.csv", encoding='utf-8')
    elif os.stat("table2.csv").st_size == 0:
        table.to_csv("table2.csv",  encoding='utf-8')
    elif os.stat("table3.csv").st_size == 0:
        table.to_csv("table3.csv",  encoding='utf-8')
    elif os.stat("table4.csv").st_size == 0:
        table.to_csv("table4.csv",  encoding='utf-8')
    elif os.stat("table5.csv").st_size == 0:
        table.to_csv("table5.csv",  encoding='utf-8')
    elif os.stat("table6.csv").st_size == 0:
        table.to_csv("table6.csv",  encoding='utf-8')

    
class Text:
    def __init__(self):
        self.tlen = 0
        self.sp = False
        self.change_text()
        
    def change_text(self):
        with open('text.txt', 'r', encoding = "utf-8") as f:
            self.file_wth_space = f.read().lower()   
            self.file_wth_space = re.sub(r'[^а-я ]', '', self.file_wth_space)
            self.file_with0ut_space = re.sub(r'\W', '', self.file_wth_space)
    
    
    @staticmethod
    def counter(file):
        gr = Counter(file)
        gr = OrderedDict(sorted(gr.items(), key=lambda x: x[0]))
          
        freq = {} 
        for el in gr:
            freq[el] = gr[el] / len(file)  
            #print(f'{el} = {freq[el]:.5f}')  
        TableMacker(freq)
        entr = 0  

        for el in freq:
            e = freq[el] * math.log(freq[el], 2)  
            entr -= e  

        return entr/2

    
    def mono(self):
        entr = self.counter(self.file_wth_space)
        print(f'Энтропия с пробелами: {entr*2}')
        print(f"R = {1 - (entr / math.log(33, 2))}")
        entr = self.counter(self.file_with0ut_space)
        print(f'Энтропия без пробелов: {entr*2}')
        print(f"R = {1 - (entr / math.log(33, 2))}")
        
    def bigram(self):
        
        entr = self.counter(re.findall(r'..?', self.file_with0ut_space))
        print(f"Энтропия без пробелов: {entr}")  
        print(f"R = {1 - (entr / math.log(33, 2))}")
        entr = self.counter(re.findall(r'..?', self.file_wth_space))
        print(f"Энтропия с пробелами: {entr}")  
        print(f"R = {1 - (entr / math.log(33, 2))}") 
        entr = self.counter(list(map(''.join, zip(self.file_wth_space, self.file_wth_space[1:]))))
        print(f"Энтропия с пробелами (скрещенные): {entr}")  
        print(f"R = {1 - (entr / math.log(33, 2))}")
        
        entr = self.counter(list(map(''.join, zip(self.file_with0ut_space, self.file_with0ut_space[1:])))  )
        print(f"Энтропия без пробелов (скрещенные): {entr}")  
        print(f"R = {1 - (entr / math.log(33, 2))}")  

           
def main():
    tt = Text()
    tt.mono()
    tt.bigram()

if __name__ == "__main__":
    main()


