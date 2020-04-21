from itertools import groupby
def gener_conway(num):
    yield ''.join(str(len(list(group))) + key for key, group in groupby(num,None))

'''
Si num='13112221'

for key, group in groupby(num,None)  => key='1'  list(group)=['1']
                                     => key='3'  list(group)=['3']
                                     => key='1'  list(group)=['1','1']
                                     => key='2'  list(group)=['2','2','2']
                                     => key='1'  list(group)=['1']

La fonction retourne '1113213211'
'''

def get_sequence(num):
    try:
        num=int(num)
    except ValueError: 
        # Si n ne peut pas etre transforme dans un entier. Par exemple n='a'.
        return "n n'est pas un entier"
    seed='1'#Le premier chiffre
    generator=gener_conway(seed) #creer un generateur
    if num<=0 :
        return 'n<=0'
    elif num==1:
        return '1'
    else:
        for _ in range(num-1):
            result=next(generator) # obtenir la valeur d'un generateur
            generator=gener_conway(result)
        return result









