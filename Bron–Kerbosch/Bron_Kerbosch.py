"""
Для использования алгоритма с произволными значениями расстояний.
Требуется передать в класс max_cliques переменную neighbors (граф в виде словаря)
и вызвать методом .start()
По диагонали должны присутвствовать псевдобесконечное значение( Например: 999)
Пример:
    neighbors = {
                'Коля': ['Антон', 'Илья'],
                'Антон': ['Коля', 'Илья'],
                'Илья': ['Коля', 'Антон', 'Дмитрий'],
                'Дмитрий':['Илья']
            }

Для проверки алгоритма присутсвует тестируемая оболочка

За основу взят материал из источника: https://ru.wikipedia.org/wiki/Алгоритм_Брона_—_Кербоша 
"""
class max_cliques:
    def __init__(self,neighbors):
        """
        Функция для инициализации переменных
        """
        self.total_cliques = 0
        self.neighbors = neighbors
        self.max = 0
        self.max_cl = []
        
    def extend(self,compsub=[], candidates=[], not_v=[]):
        """
        Функция для получения максимального количества кликов

        args:
            compsub - множество, содержащее на каждом шаге рекурсии полный подграф для данного шага
            candidates — множество вершин
            not_v — множество вершин, которые уже использовались для расширения compsub
        returns: 
            found_cliques - максимальное количество кликов
        """
        # ЕСЛИ candidates и not пусты, ТО compsub – клика
        if len(candidates) == 0 and len(not_v) == 0:
            if len(compsub) > self.max:
                self.max = len(compsub)
                self.max_cl = compsub
            return 1

        # максимально количество кликов
        found_cliques = 0

        # Выбираем вершину v из candidates 
        for v in candidates:

            # добавляем v в compsub
            new_compsub = compsub + [v]

            # Формируем new_candidates и new_not_v, удаляя из candidates и not вершины, СОЕДИНЕННЫЕ с v
            new_candidates = [n for n in candidates if n in self.neighbors[v]]
            new_not_v = [n for n in not_v if n in self.neighbors[v]]

            # рекурсивно вызываем extend (new_compsub, new_candidates, new_not) и добавляем в
            # переменную found_cliques количество кликов
            found_cliques += self.extend(new_compsub, new_candidates, new_not_v)

            # Удаляем v из candidates, и помещаем в not
            candidates.remove(v)
            not_v.append(v)

        return found_cliques
    def start(self):
        """
        Функция для старта алгоритма, печатает максимальное количество клик
        Args:
            all_nodes - список вершин 
        """
        all_nodes = list(self.neighbors.keys())
        # Вызываем функция передавая передавая переменную содержащаю множество вершин
        self.total_cliques = self.extend(candidates=all_nodes)
        print('Максимальное количество кликов:', self.max)
        print('Клики:', self.max_cl)
        

