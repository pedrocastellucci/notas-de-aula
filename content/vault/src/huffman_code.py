
class PriorityQueue:
    '''Min-Priority Queue with Heap'''

    def __init__(self):
        self.queue = []
        
    def insert(self, x):
        self.queue.append(x)
        last_idx = len(self.queue) - 1
        self._upheap(last_idx)

    def update(self, pos, new_x):
        self.queue[pos] = new_x
        self._upheap(pos)
        self._downheap(pos)

    def remove(self):
        first_idx, last_idx = 0, -1
        self.swap(first_idx, last_idx)
        res = self.queue.pop(-1)
        self._downheap(first_idx)
        return res

    def _downheap(self, pos):
        if self.has_left(pos):
            small_child = self.left(pos)
            small_child_pos = self.left_pos(pos)
            if self.has_right(pos):
                r_child = self.right(pos)
                if r_child.freq < small_child.freq:
                    small_child = r_child
                    small_child_pos = self.right_pos(pos)
            if small_child.freq < self.get_priority(pos):
                self.swap(pos, small_child_pos)
                self._downheap(small_child_pos)

    def _upheap(self, p):
        parent = self.get_parent(p)
        not_root = (not self.is_root(p))
        wrong_prior = self.get_priority(p) < self.get_priority(parent)
        if not_root and wrong_prior:
            self.swap(p, parent)
            self._upheap(parent)

    def get_parent(self, p):
        return (p-1)//2

    def is_root(self, pos):
        return pos == 0

    def get_priority(self, pos):
        return self.queue[pos].freq
    
    def swap(self, p1, p2):
        # a, b = b, a
        self.queue[p1], self.queue[p2] = self.queue[p2], self.queue[p1]

    def left_pos(self, pos):
        return 2*pos + 1

    def right_pos(self, pos):
        return 2*pos + 2

    def has_left(self, pos):
        return 2*pos + 1 < len(self.queue)

    def has_right(self, pos):
        return 2*pos + 2 < len(self.queue)
    
    def left(self, pos):
        return self.queue[2*pos + 1]

    def right(self, pos):
        return self.queue[2*pos + 2]

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


class Tree():

    def __init__(self, val=None, freq=None, _left=None, _right=None):
        self.value = val
        self.freq = freq
        self.left = _left
        self.right = _right

def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        print(tree.value)
        inorder(tree.right)

def search(tree, char, code):
    if tree is None:
        return False
    elif tree.value == char:
        return True
    elif search(tree.left, char, code):
        code.insert(0, '0')
        return True
    elif search(tree.right, char, code):
        code.insert(0, '1')
        return True
    return False


frequencies = [
    ('a', 45),
    ('b', 13),
    ('c', 12),
    ('d', 16),
    ('e', 9),
    ('f', 5),
]

Q = PriorityQueue()
for f in frequencies:
    Q.insert(Tree(val=f[0], freq=f[1]))

n = len(Q)
for i in range(n-1):
    x = Q.remove()
    y = Q.remove()
    z = Tree(val=None, freq=x.freq + y.freq)
    z.left = x
    z.right = y
    Q.insert(z)

tree = z
print("Inorder traversal of the tree")
inorder(tree)

print()
print("The code for each character is:")
for f in frequencies:
    code = []
    search(tree, f[0], code)
    print(f[0] + ": ", "".join(c for c in code))