tree = [
    None,
    'E',
    'T',
    'I',
    'A',
    'N',
    'M',
    'S',
    'U',
    'R',
    'W',
    'D',
    'K',
    'G',
    'O',
    'H',
    'V',
    'F',
    None,
    'L',
    None,
    'P',
    'J',
    'B',
    'X',
    'C',
    'Y',
    'Z',
    'Q',
]


def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def search(char, idx, code):
    if idx > len(tree):
        return False
    elif tree[idx] == char:
        return True
    elif search(char, left_child(idx), code):
        code.insert(0, '.')
        return True
    elif search(char, right_child(idx), code):
        code.insert(0, '-')
        return True
    return False

message = "Morse code testing"
for m in message:
    if m == ' ':
        continue
    code = []
    search(m.upper(), 0, code)
    print("".join(x for x in code))