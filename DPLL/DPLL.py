"""
Для использования алгоритма с произволными значениями.
передать в функция start() массив значений 
Пример:
    c = [['p','q','r'],['-p','-q','-r'],['-p','q','r'],['-q','r'],['q','-r']]
    start(c)

Дизъюнкция [['A','B']]
Конъюнкция [['A'],['B']]
Отрицание [["-A"]]
"""
def UnitPropagate(S,I):
    """
    Функция для удаления литералов из клоз
    Args:
        S - клозы
        I - литералы
    return:
        S - клозы без литералов 
        I - использованные литералы 
    """
    co=0
    for i in S:
        if len(i)==1:
            co+=1
    if co>0:
        while ([] not in S) and co>0:
            for j in S:
                if len(j)==1:
                    k=j[0]
                    break
            l=S[:]
            for h in l:
                if k in h:
                    S.remove(h)
                    
            if len(k)==2:
                I[k[1]]=0
                for h in S:
                    if k[1] in h:
                        h.remove(k[1])
            else:
                I[k]=1
                t='-'+k
                for h in S:
                    if t in h:
                        h.remove(t)
            co=0
            for i in S:
                if len(i)==1:
                    co+=1
    return S,I

def DPLL(S, I):
    """
    Рекурсивный алгоритм DPLL
    если S имеет набор дизъюнктов, то формула выполняет
    если S имеет хотя бы ожин пустой дизъюнкт, то формула не выполняется
    """
    if UnitPropagate(S, I):
        S, I = UnitPropagate(S, I)
    # прерываение рекурсии     
    if  [] in S:
        return "Невыполнима", {}
    if not S:
        return "Выполнима", I
    l=""
    for i in S:
        for x in i:
            if x not in I:
                l = x
                break
        if l:
            break
    # убираем использованные литералы      
    if l[0] != '-':
        lcomp = '-'+l
    elif l[0] == '-':
        lcomp = l[1]
    
    # создаем новый клоз,который не будет включать литерал
    new_S = []
    for i in S:
        new_clause = []
        for x in i:
            if lcomp != x:
                if l not in i:
                    new_clause.append(x)
        if new_clause not in new_S and new_clause:
            new_S.append(new_clause)

    if len(l)>1:
        I[lcomp] = 0
    else:
        I[l]=1
        
    # рекурсивный вызов
    res,II=DPLL(new_S,I)
    if res=="Выполнима":
        return "Выполнима", II
    
    else:
        new_Sv2 = []
        for i in S:
            new_clause = []
            for x in i:
                if l != x:
                    if lcomp not in i:
                        new_clause.append(x)
            if new_clause not in new_Sv2 and new_clause:
                new_Sv2.append(new_clause)
        if len(l)>1:
            I[lcomp] = 1
        else:
            I[l]=0
        return DPLL(new_Sv2, I)
def start(c):
    print(DPLL(c, {}))




# c = [['-B','A','-C'],['B','A','-C'],['-B','-A','-C'],['B'],['C']]
c = [['p','q','r'],['-p','-q','-r'],['-p','q','r'],['-q','r'],['q','-r']]
start(c)