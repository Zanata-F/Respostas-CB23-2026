import random as r
import time as t
import AulasPraticas.AP_03_ordenacao as ord
import sys as s

s.setrecursionlimit(10000)
r.seed(1001)

dicionario = {
    'selection':{
        'medio':[],
        'pior':[]
    },
    'divide':{
        'medio':[],
        'pior':[]
    },
    'Quick':{
        'medio':[],
        'pior':[]
    }

}

for situacao in ['medio', 'pior']:
    for n in {100, 500, 1000, 5000}:
        key_2 = 'z'

        for funcao in [ord.selection_sort, ord.divide_and_conquer_sort, ord.quick_sort]:
            tempo=0
            for i in range(50):
                if situacao == 'medio':
                    key_2 = 'medio'
                    lista = r.sample(range(-10000, 10000), k=n)
                else:
                    key_2 = 'pior'
                    lista = [i for i in range(int(n/2), int(-n/2), -1)]
                key = 'z'
                if funcao == ord.selection_sort:
                    key='selection'
                elif funcao == ord.divide_and_conquer_sort:
                    key = 'divide'
                else:
                    key = 'Quick'

                start=t.time()
                funcao(lista)
                tempo+=(t.time()-start)
            dicionario[key][key_2].append(tempo/50)

print('_'*107)
print(f"|{'Funções':30}|{'Caso':20}|{'n=100(s)':15}|{'n=500(s)':15}|{'n=1000(s)':15}|{'n=5000(s)':15}|")
print('_'*107)

print(f"|{'Selection.sort':30}|{'Caso médio':20}|{dicionario['selection']['medio'][0]:15}|{dicionario['selection']['medio'][1]:15}|{dicionario['selection']['medio'][2]:15}|{dicionario['selection']['medio'][3]:15}|")
print(f"|{'':30}{'_'*76}")
print(f"|{'':30}|{'Pior caso':20}|{dicionario['selection']['pior'][0]:15}|{dicionario['selection']['pior'][1]:15}|{dicionario['selection']['pior'][2]:15}|{dicionario['selection']['pior'][3]:15}|")


print('_'*107)
print(f"|{'Divide_and_conquer.sort':30}|{'Caso médio':20}|{dicionario['divide']['medio'][0]:15}|{dicionario['divide']['medio'][1]:15}|{dicionario['divide']['medio'][2]:15}|{dicionario['divide']['medio'][3]:15}|")
print(f"|{'':30}{'_'*76}")
print(f"|{'':30}|{'Pior caso':20}|{dicionario['divide']['pior'][0]:15}|{dicionario['divide']['pior'][1]:15}|{dicionario['divide']['pior'][2]:15}|{dicionario['divide']['pior'][3]:15}|")

print('_'*107)
print(f"|{'Quick.sort':30}|{'Caso médio':20}|{dicionario['Quick']['medio'][0]:15}|{dicionario['Quick']['medio'][1]:15}|{dicionario['Quick']['medio'][2]:15}|{dicionario['Quick']['medio'][3]:15}|")
print(f"|{'':30}{'_'*76}")