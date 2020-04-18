"""
Для использования алгоритма с произволными значениями расстояний.
Требуется передать в класс tsp переменную matrix (матрицу расстояний)
По диагонали должны присутвствовать псевдобесконечное значение( Например: 999)
Пример:
    matrix = [[999,0,1],
              [0,999,1],
              [1,1,999]]

Для проверки алгоритма присутсвует тестируемая оболочка

За основу взят материал из источника: https://math.semestr.ru/kom/komm.php
Для проверки маршрута использовал онлайн калькулятор: https://math.semestr.ru/kom/index.php
"""
import copy

class tsp:
    def __init__(self):
        """
        Функция для инициализации переменных
        """
        self.price = 0
        
    def make_true(self, matrix):
        """
        Функция для перевода числовой матррицы в булевую


        Args:
            matrix - матрица
        Returns:
            matrix_bool - булевая матрица 
        """
        matrix_bool = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix_bool[i][j] = True
        return matrix_bool

    def min_row(self,matrix,matrix_bool):
        """
        Функция для поиска минимальных значений в строках

        Args:
            matrix - матрица 
            matrix_bool - матрица булевых значений 

        Returns:
            row - список минимальных значений в строке
        """
        row = []
        for i in range(len(matrix)):
            min_el = 9999
            for j in range(len(matrix[0])):
                if matrix_bool[i][j]:
                    if matrix[i][j] < min_el:
                        min_el = matrix[i][j]
            row.append(min_el)
        return row

    def min_row_without_way(self,matrix,matrix_bool):
        """
        Функция для поиска минимальных значений в строках без учета конкретного города.
        С проверкой на нулевое расстояние

        Args:
            matrix - матрица 
            matrix_bool - матрица булевых значений 

        Returns:
            row - список минимальных значений в строке
        """
        row = []
        for i in range(len(matrix)):
            min_el = 9999
            count_zero = 0
            for j in range(len(matrix[0])):
                if matrix_bool[i][j]:
                    if matrix[i][j] < min_el:
                        if matrix[i][j] == 0:
                            count_zero +=1
                        else:
                            min_el = matrix[i][j]
                        if count_zero >1:
                            min_el = 0 
            row.append(min_el)
        return row

    def min_column(self,matrix,matrix_bool):
        """
        Функция для поиска минимальных значений в колонках

        Args:
            matrix - матрица 
            matrix_bool - матрица булевых значений 

        Returns:
            column - список минимальных значений в колонке 
        """
        column = []
        for i in range(len(matrix)):
            min_el = 9999
            for j in range(len(matrix[0])):
                if matrix_bool[j][i]:
                    if matrix[j][i] < min_el:
                        min_el = matrix[j][i]
            column.append(min_el)
        return column

    def min_column_without_way(self,matrix,matrix_bool):
        """
        Функция для поиска минимальных значений в колонках без учета конкретного города.
        С проверкой на нулевое расстояние

        Args:
            matrix - матрица 
            matrix_bool - матрица булевых значений 

        Returns:
            column - список минимальных значений в колонке 
        """
        column = []
        for i in range(len(matrix)):
            min_el = 9999
            count_zero = 0
            for j in range(len(matrix[0])):
                if matrix_bool[j][i]:
                    if matrix[j][i] < min_el:
                        if matrix[j][i] == 0:
                            count_zero +=1
                        else:
                            min_el = matrix[j][i]
                        if count_zero > 1:
                            min_el = 0
            column.append(min_el)
        return column 

    def reduction_matrix_row(self,matrix,row,matrix_bool):
        """
        Функция для редукции матрицы по строкам путём вычитания минимального значения

        Args:
            matrix - матрица 
            row - список минимальных значений в строках
            matrix_bool - матрица булевых значений 

        Returns:
            matrix - сокращенная матрица по строкам
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix_bool[i][j]:
                    matrix[i][j] -= row[i]
        return matrix

    def reduction_matrix_column(self,matrix,column,matrix_bool):
        """
        Функция для редукции матрицы по столбцам путём вычитания минимального значения

        Args:
            matrix - матрица 
            column - список минимальных значений в столбцах
            matrix_bool - матрица булевых значений 

        Returns:
            matrix - сокращенная матрица по столбцам 
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix_bool[j][i]:
                    matrix[j][i] -= column[i]
        return matrix

    def find_zero(self,matrix,matrix_bool):
        """
        Функция для поиска всех клеток матрицы с нулевыми элементами

        Args:
            matrix - матрица
            matrix_bool - матрица булевых значений  
        Returns:
            zero_list - список координат клеток с нулевыми элементами
        """
        zero_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix_bool[i][j]:
                    if matrix[i][j] == 0:
                        zero_list.append((i,j))
        return zero_list

    def find_max_tree(self,matrix,row,column,zero_list):
        """
        Функция для поиска самой большой цены маршрута

        Args:
            matrix - матрица
            matrix_bool - матрица булевых значений 
            zero_list - список координат клеток с нулевыми элементами
            row - список минимальных значений в строках
            column - список минимальных значений в столбцах
        Returns:
            max_way - координата клетки, где максимальная цена 
        """
        count_const = {}
        for i in zero_list:
            count_const[i] = row[i[0]] + column[i[1]]
        max_way = max(count_const, key=count_const.get)
        return max_way

    def delete_tree(self,matrix_bool,max_way):
        """
        Функция для замены на значение False в булевой матрице удаленные(использованные) строки и столбцы  

        Args:
            matrix_bool - булевая матрица
            max_way - координата клетки, у которой нужно удалить столбец и строку
        Returns:
             matrix_bool - булевая матрица
        """
        for j in range(len(self.matrix[max_way[0]])):
            matrix_bool[max_way[0]][j] = False
        for j in range(len(self.matrix[max_way[1]])):
            matrix_bool[j][max_way[1]] = False

        return matrix_bool

    def change_zero(self,matrix,way):
        """
        Функция для замены использованного пути на псевдобесконечное число 

        Args:
            matrix - матрица
            way - координата клетки
        Returns:
             matrix - матрица с измененным значеним 
        """
        matrix[way[0]][way[1]] = 999
        return matrix

    def Reverse(self,tuples): 
        """
        Функция для разворота кортежи

        Args:
            tuples - кортеж
        Returns:
             new_tup - новый кортеж
        """
        new_tup = tuples[::-1] 
        return new_tup 

    def sort_way(self,way):
        """
        Функция для сортировки пути

        Args:
            way - неотсортированный путь 
        Returns:
             sorted_way - отсортированный путь 
        """
        sorted_way = []
        second_element = way[0][1]
        for i in range(len(way)):
            for j in way:
                if second_element == j[0]:
                    sorted_way.append(j)
                    second_element = j[1]
                    break
        return sorted_way

    def find_price_ways(self,matrix,way):
        """
        Функция для нахождения суммы пути
        Args:
            matrix - матрица
            way - путь 
        Returns:
            price - сумма пути 
        """
        price = 0
        for i in way:
            price += matrix[i[0]][i[1]]
        return price
    
    
    def start(self,matrix):
        """
        Функция для старта алгоритма, печатает путь и длину маршрута
        Args:
            matrix - матрица 
        """
        matrix = matrix
        matrix_clear = copy.deepcopy(matrix)
        # создается булевая матрица, для запрета на использования удаленныйх элементов 
        matrix_bool = self.make_true(matrix)
        way_full = []
        for i in range(len(matrix_clear)):
            # Найдём минимальные значения по строкам
            row = self.min_row(matrix,matrix_bool)
            # Производим редукцию по строкам путём вычитания минимального значения
            self.matrix = self.reduction_matrix_row(matrix,row,matrix_bool)
            #Найдём минимальные значения по столбцам 
            column = self.min_column(matrix,matrix_bool)
            # Аналогично производим редукцию по столбцам.
            self.matrix = self.reduction_matrix_column(matrix,column,matrix_bool)
            # В получившейся матрице таблице находим нулевые значения
            zero_list = self.find_zero(matrix,matrix_bool)
            # находим минимальные элементы в строках и столбац без учета использованных маршрутов
            row = self.min_row_without_way(matrix,matrix_bool)
            column = self.min_column_without_way(matrix,matrix_bool)
            # Вычисляем оценку для нулевых значений
            max_way = self.find_max_tree(matrix,row,column,zero_list)

            #Сократим матрицу потерь за счёт исключения строки и столбца с наибольшей оценкой
            matrix_bool = self.delete_tree(matrix_bool,max_way)
            # необходимо вместо нуля (минимального значения) поставить псевдобесконечное число 
            self.matrix = self.change_zero(matrix,self.Reverse(max_way))
            # Добавляем все пути
            way_full.append(max_way)
        # Находим отсортированный путь
        way = self.sort_way(way_full)   
        # Находим сумму процденного расстояния 
        self.price = self.find_price_ways(matrix_clear,way)
        print('Путь {} Пройденное расстояние = {}'.format(way,self.price))

