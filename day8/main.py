#/usr/bin/env python3

def p1(tree):
    result = 0
    for n in tree[2]:
        result += p1(n)
    for d in tree[3]:
        result += d
    return result

def p2(tree):
    result = 0
    for d in tree[3]:
        if tree[0]:
            if d != 0 and d <= tree[0]:
                result += p2(tree[2][d-1])
        else:
            result += d
    return result

def process_node(ints_list):
    nb_child = ints_list.pop(0)
    nb_data = ints_list.pop(0)
    child = []
    for n in range(nb_child):
        child.append(process_node(ints_list))
    data = []
    for n in range(nb_data):
        data.append(ints_list.pop(0))
    return (nb_child, nb_data, child, data)

if __name__ == "__main__":
    f = open('input.txt', 'r')
    ints_list = list(map(int, f.readline().split()))
    tree = process_node(ints_list)
    print("part1: {}".format(p1(tree)))
    print("part2: {}".format(p2(tree)))
