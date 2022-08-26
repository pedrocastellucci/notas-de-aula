class Queue:
    def __init__(self, max_size):
        self.__items = [None]*(max_size + 1)
        self.__first = 0
        self.__last = 0

    def is_empty(self):
        return self.__first == self.__last

    def is_full(self):
        return (self.__last + 1) % len(self.__items) == self.__first

    def push(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.__items[self.__last] = item
        self.__last = (self.__last + 1) % len(self.__items)

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.__items[self.__first]
        self.__first = (self.__first + 1) % len(self.__items)
        return item


def get_distances(A, x):
    '''Compute distances between x and every city
    in the distance matrix A'''
    n = len(A)
    dist = [-1]*n
    q = Queue(n)
    dist[x] = 0
    q.push(x)
    while(not q.is_empty()):
        y = q.pop()
        for i in range(n):
            if A[y][i] == 1 and dist[i] == -1:
                dist[i] = dist[y] + 1
                q.push(i)
    return dist

A = [
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0]
]

start_node = 0
dist = get_distances(A, start_node)
print(dist)