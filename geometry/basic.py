from math import pi, atan


def len2d(p1, p2):
    """
    The length of 2d-vector

    :param p1:
    :param p2:
    :return: int, real
    """
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)


def len3d(p1, p2):
    """
    The length of 3d-vector

    :param p1:
    :param p2:
    :return:
    """
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2) ** (1 / 2)


def dot2d(v1, v2):
    """
    The scalar product of 2d-vectors

    :param v1:
    :param v2:
    :return:
    """
    return sum(c1 * c2 for c1, c2 in zip(v1, v2))


def dot3d(v1, v2):
    """
    The scalar product of 3d-vectors

    :param v1:
    :param v2:
    :return:
    """
    return sum(c1 * c2 for c1, c2 in zip(v1, v2))


def pseudo2d(v1, v2):
    """
    The pseudo-scalar product of 2d-vectors

    :param v1:
    :param v2:
    :return:
    """
    return v2[1] * v1[0] - v1[1] * v2[0]


def pseudo3d(v1, v2, v3):
    """
    The pseudo-scalar product of 3d-vectors

    :param v1:
    :param v2:
    :param v3:
    :return:
    """
    return v1[0] * (v2[1] * v3[2] - v2[2] * v3[1]) - v2[0] * (v1[1] * v3[2] - v1[2] * v3[1]) + v3[0] * (v1[1] * v2[2] -
                                                                                                        v1[2] * v2[1])

def angle(v):
    """
    The angle of 2d-vector in rad

    :param v:
    :return:
    """
    x, y = v
    if x == 0:
        if y > 0:
            return pi / 2
        else:
            return 3 * pi / 2
    elif x > 0:
        if y >= 0:
            return atan(y/x)
        else:
            return 2 * pi + atan(y/x)
    else:
        return pi + atan(y/x)


print(pseudo3d((1, 0, 0), (0, 2, 0), (0, 0, 5)))

