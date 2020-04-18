from tsp import *

class test:
    def first_test():
        way = 172
        matrix = [[999,41,40,48,40,42],
                  [48,999,41,49,42,46],
                  [22,22,999,23,24,19],
                  [15,17,11,999,10,14],
                  [47,43,18,42,999,52],
                  [34,39,30,39,32,999]]
        print('\nДлина пути должна быть равна ', way)
        class_tsp = tsp()
        class_tsp.start(matrix)
        if class_tsp.price == way:
            print('Первый тест пройден')
        else:
            print('Первый тест завален')
    def second_test():
        way = 180
        matrix = [[999,90,80,40,100],
          [60,999,40,50,70],
          [50,30,999,60,20],
          [10,70,20,999,50],
          [20,40,50,20,999]]
        print('\nДлина пути должна быть равна ', way)
        class_tsp = tsp()
        class_tsp.start(matrix)
        if class_tsp.price == way:
            print('Второй тест пройден')
        else:
            print('Второй тест завален')
    def three_test():
        way = 85
        matrix = [[999,10,15,11,2,55],
                  [17,999,16,18,21,13],
                  [10,50,999,39,22,3],
                  [28,29,24,999,28,25],
                  [27,9,32,9,999,2],
                  [43,48,40,43,21,999]]
        print('\nДлина пути должна быть равна ', way)
        class_tsp = tsp()
        class_tsp.start(matrix)
        if class_tsp.price == way:
            print('Третий тест пройден')
        else:
            print('Третий тест завален')
    def four_test():
        way = 77
        matrix = [[999,0,15,11,2,55],
                  [17,999,16,18,21,13],
                  [10,50,999,39,22,3],
                  [28,29,24,999,28,25],
                  [27,9,32,9,999,2],
                  [43,48,40,43,21,999]]
        print('\nДлина пути должна быть равна ', way)
        class_tsp = tsp()
        class_tsp.start(matrix)
        if class_tsp.price == way:
            print('Четвертый тест пройден')
        else:
            print('Четвертый тест завален')
    def five_test():
        way = 2
        matrix = [[999,0,1],
                  [0,999,1],
                  [1,1,999]]
        print('\nДлина пути должна быть равна ', way)
        class_tsp = tsp()
        class_tsp.start(matrix)
        if class_tsp.price == way:
            print('Пятый тест пройден')
        else:
            print('Пятый тест завален')
    def six_test():
        way = 30
        matrix = [[999,5,11,9],
                  [20,999,8,7],
                  [7,14,999,8],
                 [12,6,15,999]]
        print('\nДлина пути должна быть равна ', way)
        class_tsp = tsp()
        class_tsp.start(matrix)
        if class_tsp.price == way:
            print('Шестой тест пройден')
        else:
            print('Шестой тест завален')
    def seven_test():
        way = 1
        matrix = [[999,0,0],
                  [1,999,1],
                  [1,0,999]]
        print('\nДлина пути должна быть равна ', way)
        class_tsp = tsp()
        class_tsp.start(matrix)
        if class_tsp.price == way:
            print('Седьмой тест пройден')
        else:
            print('Седьмой тест завален \n')
    def eight_test():
        way = 0
        matrix = [[999,0,0],
                  [0,999,0],
                  [0,0,999]]
        print('\nДлина пути должна быть равна ', way)
        class_tsp = tsp()
        class_tsp.start(matrix)
        if class_tsp.price == way:
            print('Восьмой тест пройден')
        else:
            print('Восьмой тест завален \n')
    
    
    if  __name__ == '__main__':
        first_test()
        second_test()
        three_test()
        four_test()
        five_test()
        six_test()
        seven_test()
        eight_test()
test()