'''Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
Завдання включає створення графа, використання піраміди для оптимізації вибору вершин
 та обчислення найкоротших шляхів від початкової вершини до всіх інших.
'''

import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Ініціалізація черги з початковою вершиною
    priority_queue = [(0, start)]  # (відстань, вершина)
    
    while priority_queue:
        # Вибір вершини з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо вже знайшли коротший шлях, пропускаємо вершину
        if current_distance > distances[current_vertex]:
            continue
        
        # Перевірка суміжних вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусідньої вершини
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад графа
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Виклик функції для вершини A
print(dijkstra(graph, 'A'))
