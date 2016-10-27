import unittest
from ..vector import get_directionnal_vectors, vector_add, get_vector_add_generator


class TestVector(unittest.TestCase):

    def test_get_directionnal_vectors_should_return_a_list_of_directionnal_vectors(self):
        self.assertEqual(
            list(get_directionnal_vectors()),
            [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        )

    def test_vector_add_should_add_vectors(self):
        self.assertEqual(vector_add((24, 48), (-11, -11)), (13, 37))

    def test_get_vector_add_generator_should_return_a_vector_generator(self):
        vector_generator = get_vector_add_generator((0, 0), (1, 1))
        self.assertEqual(next(vector_generator), (1, 1))
        self.assertEqual(next(vector_generator), (2, 2))
