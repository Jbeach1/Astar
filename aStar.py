import math
from p1Gui import Gui
from intersection import Intersect, if_intersect
from shape import Node


def gen_euclid(nodes, goal):
    for node in nodes:
        set_euclid(node, goal)


def gen_f(nodes):
    for node in nodes:
        node.f = node.g + node.h


def get_running_cost(node, goal):
    return math.sqrt(((node.cord[0] - goal.cord[0]) ** 2) + ((node.cord[1] - goal.cord[1]) ** 2))


def set_euclid(node, goal):
    x = math.sqrt(((node.cord[0] - goal.cord[0]) ** 2) + ((node.cord[1] - goal.cord[1]) ** 2))
    node.h = x
    return x


def generate_edges(shape):
    edges = []
    for i in range(len(shape)):
        edges.append((shape[i].cord, shape[(i + 1) % len(shape)].cord))
    return edges


def gen_neighbors(*args):
    for arg in args:
        set_neighbors(arg)


def set_neighbors(shape):
    i = 0
    for node in shape:
        i += 1
        node.l = shape[i - 2].cord
        node.r = shape[i % len(shape)].cord


def get_children(current_pt, nodes, edges):
    children = []
    node_list = []
    for node in nodes:
        add = True
        for edge in edges:
            if if_intersect((current_pt.cord, node.cord), edge):
                add = False
        if add:
            if not current_pt.shape == node.shape:
                children.append(node.cord)
    if current_pt.l not in children:
        children.append(current_pt.l)
    if current_pt.r not in children:
        children.append(current_pt.r)
    for child in children:
        search = child
        for node in nodes:
            if node.cord == search:
                node_list.append(node)
    return node_list


def get_lowest_f(open):
    lowest = open[0]
    #gen_f(open)
    for node in open:
        if node.f < lowest.f:
            lowest = node
    return lowest


def child_in_list(child, container):
    for node in container:
        if node == child:
            return True
    return False


def a_star(start, end, nodes, edges):
    start.g = 0
    start.f = start.h

    closed = []
    open = []
    open.append(start)
    while len(open) > 0:
        current_node = get_lowest_f(open)
        if current_node == end:
            return current_node
        open.remove(current_node)
        closed.append(current_node)

        for child in get_children(current_node, nodes, edges):
            if child in closed:
                continue
            temp = current_node.g + get_running_cost(current_node, child)
            if child not in open:
                open.append(child)
            elif temp >= child.g:
                continue
            child.parent = current_node
            child.g = temp
            child.f = child.g + child.h


def gen_path(node, start):
    path.append(node.cord)
    if node.parent == start:
        return
    gen_path(node.parent, start)


path = []


class Main:
    ####################################################################################################################
    goals = [Node((180, 420), 'start'), Node((900, 50), 'end')]
    pentagon = [Node((218, 130), 'pentagon'), Node((320, 50), 'pentagon'), Node((380, 135), 'pentagon'),
                Node((335, 275), 'pentagon'), Node((230, 260), 'pentagon')]
    rectangle1 = [Node((230, 480), 'rectangle1'), Node((230, 360), 'rectangle1'), Node((550, 360), 'rectangle1'),
                  Node((550, 480), 'rectangle1')]
    triangle1 = [Node((400, 300), 'triangle1'), Node((450, 125), 'triangle1'), Node((480, 300), 'triangle1')]
    ugly = [Node((490, 60), 'ugly'), Node((560, 45), 'ugly'), Node((620, 125), 'ugly'), Node((490, 200), 'ugly')]
    triangle2 = [Node((560, 250), 'triangle2'), Node((660, 340), 'triangle2'), Node((590, 425), 'triangle2')]
    rectangle2 = [Node((635, 270), 'rectangle2'), Node((635, 50), 'rectangle2'), Node((750, 50), 'rectangle2'),
                  Node((750, 270), 'rectangle2')]
    diamond = [Node((770, 70), 'diamond'), Node((830, 40), 'diamond'), Node((870, 85), 'diamond'),
               Node((840, 330), 'diamond')]
    stop_sign = [Node((775, 325), 'stop_sign'), Node((825, 370), 'stop_sign'), Node((825, 460), 'stop_sign'),
                 Node((755, 490), 'stop_sign'), Node((700, 450), 'stop_sign'), Node((700, 370), 'stop_sign')]
    nodes = pentagon + rectangle1 + triangle1 + ugly + triangle2 + rectangle2 + diamond + stop_sign + goals
    edges = generate_edges(pentagon) + generate_edges(rectangle1) + generate_edges(triangle1) + generate_edges(ugly) \
            + generate_edges(triangle2) + generate_edges(rectangle2) + generate_edges(diamond) \
            + generate_edges(stop_sign)
    gen_euclid(nodes, goals[1])
    gen_neighbors(pentagon, rectangle1, triangle1, ugly, triangle2, rectangle2, diamond, stop_sign)

    gen_path(a_star(goals[0], goals[1], nodes, edges), goals[0])
    path.append(goals[0].cord)
    Gui().run_it(path, goals[0].cord, goals[1].cord)
    ####################################################################################################################
