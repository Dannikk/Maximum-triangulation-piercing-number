from queue import Queue

def bfs(graph: dict, start: tuple):
    """
    Non-recursive realization of breadth-first search
    algorithm using `~queue.Queue`
    Parameters
    ----------
    graph : dict
        any graph
    start : object
        any hashable object
    nodes_queue_class : class `~queue.Queue`
        abstract data type used to implement a breadth-first search)
    Returns
    -------
    generator :
        yielding node by node of bfs path, on None in error case
    """
    if start not in graph:
        print("The graph does not contain such a node\n"
                         "\t\t\tSet the correct node")
    
    depth = 0
    nodes_queue = Queue()
    nodes_queue.put((start, depth))
    visited = set()
    while not nodes_queue.empty():
        current, depth = nodes_queue.get()
        if current in visited:
            continue
        visited.add(current)
        yield current, depth

        for neighbor in graph[current]:
            if neighbor not in visited:
                nodes_queue.put((neighbor, depth+1))