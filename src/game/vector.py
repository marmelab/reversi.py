from itertools import product
import operator


def get_directionnal_vectors():
    """ Return an iterator of directinnal vectors (N, NE, E, SE, ..)"""

    directionnal_vectors = product((-1, 0, 1), (-1, 0, 1))
    return (vectors for vectors in directionnal_vectors if not vectors == (0, 0))


def vector_add(v1, v2):
    return tuple(map(operator.add, v1, v2))
