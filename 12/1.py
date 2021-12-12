from pprint import pprint
from copy import deepcopy

class Node:
    def __init__(self, name, neighbour):
        self.name = name
        self.is_visited = False
        self.is_big_cave = True if self.name.isupper() else False
        self.neighbours = [neighbour]

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
    
    def __repr__(self):
        return f'{self.name}, {self.is_visited}, {self.is_big_cave}'

def get_input(filename):
    graph = {}
    lines = [line.strip().split('-') for line in open(filename).readlines()]
    for line in lines:
        if line[0] not in graph:
            graph[line[0]] = Node(line[0], line[1])
        else:
            graph[line[0]].add_neighbour(line[1])
            
        if line[1] not in graph:
            graph[line[1]] = Node(line[1], line[0])
        else:
            graph[line[1]].add_neighbour(line[0])
    return graph

def find_paths(graph, current_name, path=[]):
    graph_local = deepcopy(graph)
    path_local = path[:]
    neighbours = graph_local[current_name].neighbours[:]
    paths = []
    
    path_local.append(current_name)
    graph_local[current_name].is_visited = True
    
    if current_name == 'end':
        graph_local[current_name].is_visited = False
        return [path_local]
    
    for neighbour in neighbours:
        if not graph_local[neighbour].is_big_cave and graph_local[neighbour].is_visited:
            continue
        
        paths.extend(find_paths(graph_local, neighbour, path_local))
    return paths

graph = get_input('12/input.txt')
all_paths = find_paths(graph, 'start')
pprint(len(all_paths))
#5228
