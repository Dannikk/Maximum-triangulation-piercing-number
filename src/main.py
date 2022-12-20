import argparse
from collections import defaultdict
from typing import Tuple
from bfs import bfs


def get_triangles(file_path: str) -> Tuple[dict, defaultdict]:
    opposite_nodes = defaultdict(list)
    
    with open(file_path, 'r') as file:
        n = int(file.readline())
        triangles = {}
        for string in file:
            v1, v2, v3 = list(map(int, string.split()))
            triangles[tuple(sorted([v1, v2, v3]))] = set()
            
            opposite_nodes[tuple(sorted([v1, v2]))].append(v3)
            opposite_nodes[tuple(sorted([v2, v3]))].append(v1)
            opposite_nodes[tuple(sorted([v1, v3]))].append(v2)
            

    return triangles, opposite_nodes
    

def get_dual_graph(triangles: dict, opposite_nodes: defaultdict) -> dict:
    for triangle in triangles:
        for i in range(3):
            v, u = triangle[i], triangle[(i+1) % 3]
            edge = tuple(sorted([v, u]))
            for opposite in opposite_nodes[edge]:
                if opposite not in triangle:
                    other_triangle = tuple(sorted([v, u, opposite]))
                    triangles[triangle].add(other_triangle)
                    triangles[other_triangle].add(triangle)
    return triangles


def get_graph_diameter(graph: dict) -> int:
    start = list(graph.keys())[0]
    last_node = None
    
    for node, depth in bfs(graph, start): 
        last_node = node
    for node, depth in bfs(graph, last_node):
        last_depth = depth

    return last_depth


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Maximum triangulation piercing number")
    parser.add_argument('input', type=str, help='direction to input file')
    parser.add_argument('-out', type=str, help="direction to output file, default='output.txt'", default='output.txt')
    args = parser.parse_args()
    input_file = args.input
    output_file = args.out
    print(f"File to read triangulation:\t\t{args.input}")
    print(f"File to write triangulation piercing number:\t{args.out}")

    triangles, opposite_nodes = get_triangles(input_file)
    
    graph = get_dual_graph(triangles, opposite_nodes)
    
    max_piercing = get_graph_diameter(graph)
    print(max_piercing)
    
    with open(output_file, 'w') as file:
        file.write(str(max_piercing))
