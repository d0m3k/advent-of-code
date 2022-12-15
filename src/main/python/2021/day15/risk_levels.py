import queue

day_15_input_path = '../../../resources/y2021/day-15-input-example'


values_f = open(day_15_input_path, 'r')
values = [x.strip() for x in values_f.readlines()]

WIDTH = len(values[0])
HEIGHT = len(values)

print(f"{values}")


# it is either Djikstra or A* (with heuristics on manhattan distance maybe)

# but let's start with queue based BFS!
to_visit_coordinates = queue.Queue()
to_visit_coordinates.put((0, 0))


def add_all_neighbors(current_coordinates, q):
    x, y = current_coordinates

    pass


while not to_visit_coordinates.empty():
    current = to_visit_coordinates.get()
    add_all_neighbors(current, to_visit_coordinates)
