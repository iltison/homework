from Bron_Kerbosch import *

class test:
    def first_test():
        way = 4
        neighbors = {
                'A': ['B', 'C', 'E'],
                'B': ['A', 'C', 'D', 'F'],
                'C': ['A', 'B', 'D', 'F'],
                'D':['C', 'B', 'E', 'F'], 
                'E': ['A', 'D'],
                'F': ['B', 'C', 'D']
            }
        print('\nМаксимальное количество кликов должно быть ', way)
        cliques = max_cliques(neighbors)
        cliques.start()
        if cliques.max == way:
            print('Первый тест пройден')
        else:
            print('Первый тест завален')
    def second_test():
        way = 3
        neighbors = {
                '1': ['2', '3'],
                '2': ['1', '3'],
                '3': ['1', '2', '4'],
                '4':['3']
            }
        print('\nМаксимальное количество кликов должно быть ', way)
        cliques = max_cliques(neighbors)
        cliques.start()
        if cliques.max == way:
            print('Второй тест пройден')
        else:
            print('Второй тест завален')
            
    def three_test():
        way = 3
        neighbors = {
                'Коля': ['Антон', 'Илья'],
                'Антон': ['Коля', 'Илья'],
                'Илья': ['Коля', 'Антон', 'Дмитрий'],
                'Дмитрий':['Илья']
            }
        print('\nМаксимальное количество кликов должно быть ', way)
        cliques = max_cliques(neighbors)
        cliques.start()
        if cliques.max == way:
            print('Третий тест пройден')
        else:
            print('Третий тест завален')
    def four_test():
        way = 4
        neighbors = {
                1: [2, 3, 4],
                2: [1, 3, 4],
                3: [1, 2, 4],
                4:[1,2,3]
            }
        print('\nМаксимальное количество кликов должно быть ', way)
        cliques = max_cliques(neighbors)
        cliques.start()
        if cliques.max == way:
            print('Четвертый тест пройден')
        else:
            print('Четвертый тест завален')
   
    
    if  __name__ == '__main__':
        first_test()
        second_test()
        three_test()
        four_test()

test()