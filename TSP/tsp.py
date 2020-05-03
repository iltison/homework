
"""
Для использования алгоритма с произволными значениями расстояний.
Требуется передать в класс tsp переменную matrix (матрицу расстояний).
По диагонали могут находиться любые значения, алгоритм изменит на бесконечность .
Пример:
    
    matrix = [[999,0,1],
              [0,999,1],
              [1,1,999]]
    test = tsp()
    test.start(matrix)
    
Для проверки алгоритма присутсвует тестируемая оболочка.

За основу взят материал из источника: https://habr.com/ru/post/246437/
Для проверки маршрута использовал онлайн калькулятор: http://habr.x1site.ru
"""

import copy

class tsp():
    def __init__(self):
        """
        Функция для инициализации переменных.
        """
        self.matrix = []
        self.full_way = []
        self.way_price = 0
        
    def change_diagonal(self,matrix):
        """
        Функция для замены главной диагонали на значения бесконечности.
        
        Args:
            matrix - матрица.
        Returns:
            matrix - матрица c измененной диагональю. 
        """
        n=len(matrix)
        m=len(matrix[0])
        return [[float('inf') if i==j else matrix[i][j] for j in range(m)] for i in range(n)]
    
    def find_min(self,list_number):
        """
        Функция для нахождения минимума.
        
        Args:
            list_number - массив значений. 
        Returns:
            min_el - минимальный элемент.
        """
        min_el = float('inf')
        for i in range(len(list_number)):
            if list_number[i] == '_': continue
            if list_number[i] < min_el:
                min_el = list_number[i]
        if min_el == float('inf'): min_el = 0
        return min_el

    def reduction(self,matrix_list,element):
        """
        Функция для вычитания элементов из массива.
        
        Args:
            matrix_list - массив значений матрицы.
            element - элемент, который надо вычесть. 
        Returns:
            matrix_list - массив значений с вычтенным значением. 
        """
        for i in range(len(matrix_list)):
            if matrix_list[i] == '_': continue
            if matrix_list[i] == float('inf'): continue
            matrix_list[i] -= element
        return matrix_list
    
    def find_low_price_way(self,matrix):
        
        """
        Функция для вычисления нижней оценки стоимости маршрута.
        
        Args:
            matrix - матрица. 
        Returns:
            subtract_Sum - сумма констант.
            matrix - матрица.
        """
        subtract_Sum = 0
        # Поиск констант строк
        for row in range(len(matrix)):
            min_element = self.find_min(matrix[row])
            subtract_Sum += min_element
            matrix[row] = self.reduction(matrix[row],min_element)
        matrix_2 = [] 
        
        # Поиск констант столбцов
        for i in range(len(matrix)):
            column = [x[i] for x in matrix]
            min_element = self.find_min(column)
            subtract_Sum += min_element
            matrix_2.append(self.reduction(column,min_element))
        # транспонирование матрицы
        matrix = [list(i) for i in zip(*matrix_2)]
        return subtract_Sum, matrix 
    
    def find_sum_zero_ways(self,matrix):
        """
        Функция для вычисления штрафа за неиспользование для каждого нулевого элемента.
        
        Args:
            matrix - матрица.
        Returns:
            ways - пути и сумма штрафа.
        """
        # Нахождение нулевых элементов
        zero_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_list.append((i,j))
        ways = {}
        # Нахождение штрафа нулевых элементов
        for zero in zero_list:
            orig = matrix[zero[0]][zero[1]]
            matrix[zero[0]][zero[1]] = float('inf')
            row = matrix[zero[0]]
            column = [row[zero[1]] for row in matrix]
            ways[zero] = self.find_min(row) + self.find_min(column)
            matrix[zero[0]][zero[1]] = orig
        return ways
    
    def find_max_way(self,matrix):
        """
        Функция для нахождения максимального штрафа.
        
        Args:
            matrix - матрица.
        Returns:
            max_way - максимальный штраф.
        """
        zero_list = self.find_sum_zero_ways(matrix) 
        if len(zero_list) == 0:
            max_way = None
        else:
            max_way = max(zero_list, key=zero_list.get)
        return max_way
    
    def delete_tree(self,matrix,max_way):
        """
        Функция для удаления импользованного маршрута (строки и столбца).
        
        Args:
            matrix - матрица.
            max_way - путь с максимальным штрафом.
        Returns:
            matrix - матрица.
        """
        for j in range(len(matrix[max_way[0]])):
            matrix[max_way[0]][j] = '_'
        for j in range(len(self.matrix[max_way[1]])):
            matrix[j][max_way[1]] = '_'
        return matrix
    
    def Reverse(self,tuples):
        """
        Функция для отражения кортежа.
        
        Args:
            tuples - кортеж.
        Returns:
            new_tup - перевернутый кортеж.
        """
        new_tup = tuples[::-1] 
        return new_tup 

    def change_zero(self,matrix,way):
        """
        Функция для замены посещенных городов на бесконечность.
        
        Args:
            matrix - матрица.
            way - путь.
        Returns:
            matrix - матрица.
        """
        if matrix[way[0]][way[1]] == '_':
            return matrix
        else:
            matrix[way[0]][way[1]] = float('inf')
            return matrix

    
    def find_min_tree(self,matrix):
        """
        Функция выбора минимальной ветви графа.
        
        Args:
            matrix - матрица.
        Returns:
            idx - индекс ответвления графа.
        """
        min_el = float('inf')
        idx = None
        for i in matrix:
            if i[2] == True:
                if i[0] < min_el:
                    min_el = i[0]
                    idx = matrix.index(i) 
        return idx

    def find_ways(self,matrix,idx = -2):
        """
        Функция прохождения конечного графа для нахождения путей.
        
        Args:
            matrix - матрица.
            idx - индекс ответвления графа. Если не переадется, то равен -2, что говорит об последнем элементе. 
        Returns:
            idx - индекс ответвления графа.
        """
        way = matrix[idx][4]
        if (way == None):
            pass # выход из рекурсии
        else:
            if matrix[idx][5]:
                self.full_way.append(way)
            idx = matrix[idx][3]
            self.find_ways(matrix,idx)
            
    def sort_way(self,ways):
        """
        Функция сортировки полного пути.
        
        Args:
            ways - список путей.
        Returns:
            sorted_ways - отсортированный список путей.
        """
        sorted_ways = []
        second_element = ways[0][1]
        for i in range(len(ways)):
            for j in ways:
                if second_element == j[0]:
                    sorted_ways.append(j)
                    second_element = j[1]
                    break
        return sorted_ways  
              
    def check_inf(self,matrix):
        """
        Функция проверки на бесконечность, чтобы путь не зациклился.
        Если в матрице в строке отсутсвует бесконечный путь, то в определенный стобец
        записывается конечный путь.
        По главной ОТСОРТИРОВАННОЙ диагонали должны быть бесконечности. Порядок стобцов неважен.
        
        Args:
            matrix - матрица.
        Returns:
            matrix - матрица с добавленной бесконечностью.
        """
        not_inf = []
        for i in range(len(matrix)):
            count = 0
            count_null = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] == '_': count_null +=1
                if matrix[i][j] == float('inf'):
                    count += 1
            if count == 0 and count_null != len(matrix):
                not_inf.append(i)

        for i in range(len(matrix)):
            count = 0
            count_null = 0
            for j in range(len(matrix[0])):
                if matrix[j][i] == '_': count_null +=1
                if matrix[j][i] == float('inf'):
                    count += 1
            if count == 0 and count_null != len(matrix):
                not_inf.append(i)
        if len(not_inf) != 0:
            matrix = self.change_zero(matrix, tuple(not_inf))
        return matrix
    
    def find_last_way(self,matrix):
        """
        Функция для поиска последнего пути и добавления в общий список.
        
        Args:
            matrix - матрица.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == float('inf'):
                    self.full_way.append(tuple([i,j]))
                    break
                    
    def start(self,matrix):
        """
        Функция для нахождения ветвей графа и записи в список.
        
        Args:
            matrix - матрица.
        """
        # главная диагональ заменяется на бесконечности. 
        self.matrix = self.change_diagonal(matrix)
        # Список хранения овтетвлений графа.
        all_matrix = []
        # Копия матрицы для нахождения первого пути и нижней границы.
        matrix_find_low = copy.deepcopy(self.matrix)
        # Нахождение нижней границы.
        coef,matrix_find_low = self.find_low_price_way(matrix_find_low)
        #  Запись в список.
        all_matrix.append([coef,matrix_find_low, True,0,None,False])
        # Цмкл для создания графа и прерывания, когда не будет путей.
        while True:
            # индекс минимального ответвления. 
            idx = self.find_min_tree(all_matrix)
            # коэффицент нижней границы.
            coef_bot = all_matrix[idx][0]
            # копии матриц для поиска пути содержащего путь и не содержащего
            matrix_copy1 = copy.deepcopy(all_matrix[idx][1])
            matrix_copy2 = copy.deepcopy(all_matrix[idx][1])
            # путь с максимальным штрафом
            max_way = self.find_max_way(all_matrix[idx][1])
            
            if max_way == None:
                break
            # поиск ответвления содержпщего путь.
            matrix_copy1 = self.change_zero(matrix_copy1, max_way)
            coef1,matrix_copy1 = self.find_low_price_way(matrix_copy1)
            # поиск ответвления не содержпщего путь.
            matrix_copy2 = self.change_zero(matrix_copy2, self.Reverse(max_way))
            matrix_copy2 = self.delete_tree(matrix_copy2,max_way)
            matrix_copy2 = self.check_inf(matrix_copy2)
            coef2,matrix_copy2 = self.find_low_price_way(matrix_copy2)
            # запись в список ответвлений.
            all_matrix.append([coef_bot + coef2,matrix_copy2, True,idx,max_way, True])
            all_matrix.append([coef_bot + coef1,matrix_copy1, True,idx,max_way, False])
            # Добавления условия, что маршрут посещен.
            all_matrix[idx][2] = False
        # обратное прохождения графа для получения путей.
        self.find_ways(all_matrix)
        self.find_last_way(all_matrix[-2][1])
        sorted_way = self.sort_way(self.full_way)
        # получение суммы всего пути 
        self.way_price = all_matrix[-2][0]
        print('Сумма пути = {}, путь = {}'.format(self.way_price,sorted_way))
