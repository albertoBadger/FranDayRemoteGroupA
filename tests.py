import unittest

from cell import Cell


class TestCell(unittest.TestCase):

    def test_when_creating_a_new_cell_then_the_status_of_it_is_stored(self):
        cell = Cell(False)

        result = cell.is_alive()

        self.assertFalse(result)


    def test_when_calculating_next_generation_then_if_there_are_less_than_two_neighbours_then_it_wont_survive(self):
        neighbours = []
        cell = Cell(False)

        will_live = cell.calculate_next_generation(neighbours)

        self.assertFalse(will_live)

