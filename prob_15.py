from typing import List, Tuple

SIZE = 20


def path_amount(coords: Tuple) -> int:
    if coords[1] < SIZE - 1 and coords[0] == SIZE:
        return 1
    if coords[1] == 0:
        return 1
    if coords[0] == coords[1]:
        return 2 * path_amount((coords[0], coords[1] - 1))
    return path_amount((coords[0], coords[1] - 1)) + path_amount(
        (coords[0] - 1, coords[1])
    )


print(path_amount((SIZE, SIZE)))
