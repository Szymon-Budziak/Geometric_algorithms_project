def create_lines(points):
    lines = []
    for p in range(len(points) - 1):
        lines.append((points[p], points[p + 1]))
    lines.append((points[-1], points[0]))
    return lines


def orientation(a, b, c, epsilon=10 ** (-12)):
    a_x, a_y = a
    b_x, b_y = b
    c_x, c_y = c
    first = (a_x - c_x) * (b_y - c_y)
    second = (a_y - c_y) * (b_x - c_x)
    determinant = first - second

    # -1 - on the left side
    # 0 - on the line
    # 1 - on the right side

    if determinant > epsilon:
        return -1
    elif determinant < -epsilon:
        return 1
    else:
        return 0


def det(a, b, c):
    a_x, a_y = a
    b_x, b_y = b
    c_x, c_y = c
    first = (a_x - c_x) * (b_y - c_y)
    second = (a_y - c_y) * (b_x - c_x)
    return first - second
