import unittest
import parity


class ParityTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None
        self.grid_1 = [
            ["X","O","X","X","X"],
            ["X","X","O","O","O"],
            ["X","O","X","O","X"],
            ["O","X","X","X","X"],
            ["X","O","O","X","X"]
        ]
        self.grid_2 = [
            ["X","O","X"],
            ["X","X","O"],
            ["X","O","X"]
        ]
    
    def test_increase_grid_size_small_grid(self):
        result_grid = parity.increase_grid_size(self.grid_2)
        expected_grid = [
            ["X","O","X","O"],
            ["X","X","O","O"],
            ["X","O","X","O"],
            ["X","X","O","O"]
        ]
        self.assertListEqual(result_grid, expected_grid)

    def test_add_row_small_grid(self):
        result_grid = parity.add_row(self.grid_2)
        expected_grid = [
            ["X","O","X"],
            ["X","X","O"],
            ["X","O","X"],
            ["X","X","O"]
        ]
        self.assertListEqual(result_grid, expected_grid)

    def test_add_column_small_grid(self):
        result_grid = parity.add_column(self.grid_2)
        expected_grid = [
            ["X","O","X","O"],
            ["X","X","O","O"],
            ["X","O","X","O"]
        ]
        self.assertListEqual(result_grid, expected_grid)

    def test_increase_grid_size(self):
        result_grid = parity.increase_grid_size(self.grid_1)
        expected_grid = [
            ["X","O","X","X","X","O"],
            ["X","X","O","O","O","O"],
            ["X","O","X","O","X","X"],
            ["O","X","X","X","X","O"],
            ["X","O","O","X","X","X"],
            ["O","O","X","X","O","O"]
        ]
        self.assertListEqual(result_grid, expected_grid)

    def test_add_row(self):
        result_grid = parity.add_row(self.grid_1)
        expected_grid = [
            ["X","O","X","X","X"],
            ["X","X","O","O","O"],
            ["X","O","X","O","X"],
            ["O","X","X","X","X"],
            ["X","O","O","X","X"],
            ["O","O","X","X","O"]
        ]
        self.assertListEqual(result_grid, expected_grid)

    def test_add_column(self):
        result_grid = parity.add_column(self.grid_1)
        expected_grid = [
            ["X","O","X","X","X","O"],
            ["X","X","O","O","O","O"],
            ["X","O","X","O","X","X"],
            ["O","X","X","X","X","O"],
            ["X","O","O","X","X","X"],
        ]
        self.assertListEqual(result_grid, expected_grid)

    def test_flip_card_small_grid(self):
        result_grid = parity.flip_card(0, 1, self.grid_2)
        expected_grid = [
            ["X","O","X"],
            ["O","X","O"],
            ["X","O","X"]
        ]
        self.assertListEqual(result_grid, expected_grid)
    
    def test_flip_card(self):
        result_grid = parity.flip_card(4, 3, self.grid_1)
        expected_grid = [
            ["X","O","X","X","X"],
            ["X","X","O","O","X"],
            ["X","O","X","O","X"],
            ["O","X","X","X","X"],
            ["X","O","O","X","X"]
        ]
        self.assertListEqual(result_grid, expected_grid)

    def test_find_flipped_card_small_grid(self):
        grid = [
            ["X","X","X","O"],
            ["X","X","O","O"],
            ["X","O","X","O"],
            ["X","X","O","O"]
        ]
        result_coordinates = parity.find_flipped_card(grid)
        expected_coordinates = [1, 3]
        self.assertListEqual(result_coordinates, expected_coordinates)
    
    def test_find_flipped_card(self):
        grid = [
            ["X","O","X","X","X","O"],
            ["X","X","O","O","O","O"],
            ["X","O","X","O","X","X"],
            ["O","X","X","X","X","O"],
            ["X","O","O","O","X","X"],
            ["O","O","X","X","O","O"]
        ]
        result_coordinates = parity.find_flipped_card(grid)
        expected_coordinates = [3, 1]
        self.assertListEqual(result_coordinates, expected_coordinates)

runner = unittest.TextTestRunner()
print('Running Tests...\n')
runner.run(unittest.TestSuite((unittest.makeSuite(ParityTests))))
