import unittest
from unittest.mock import patch
from io import StringIO
from level import Rectangle, Level

class TestRectangle(unittest.TestCase):
    def test_choose_split_spot(self):
        # Test case 1: Rectangle with small dimensions
        rectangle_small = Rectangle(0, 0, 2, 2)
        result_small = rectangle_small.choose_split_spot()
        self.assertEqual(result_small, (-1, -1), "Expected no split for a small rectangle")

        # Test case 2: Rectangle with rows <= 3
        rectangle_rows = Rectangle(0, 0, 4, 2)
        with unittest.mock.patch('random.randint', side_effect=[2, 3, 1]):
            result_rows = rectangle_rows.choose_split_spot()
        self.assertEqual(result_rows[0], 1, "Expected split on columns for a rectangle with rows <= 3")

        # Test case 3: Rectangle with cols <= 3
        rectangle_cols = Rectangle(0, 0, 2, 4)
        with unittest.mock.patch('random.randint', side_effect=[2, 3, 1]):
            result_cols = rectangle_cols.choose_split_spot()
        self.assertEqual(result_cols[0], 1, "Expected split on rows for a rectangle with cols <= 3")

        # Test case 4: Rectangle with rows > 3 and cols > 3
        rectangle_large = Rectangle(0, 0, 4, 4)
        with unittest.mock.patch('random.random', return_value=0.6), \
             unittest.mock.patch('random.randint', side_effect=[2, 3, 1]):
            result_large = rectangle_large.choose_split_spot()
        self.assertIn(result_large[0], [0, 1], "Expected split on either rows or columns for a larger rectangle")

    def test_split_room(self):
        # Test case 1: Split on center rows
        rectangle_rows = Rectangle(0, 0, 7, 7)
        with unittest.mock.patch.object(rectangle_rows, 'choose_split_spot', return_value=(0, 2)):
            result_rows = rectangle_rows.split_room((0, 2))
        self.assertIsInstance(result_rows, list, "Expected a list of rectangles")
        self.assertEqual(len(result_rows), 2, "Expected two rectangles after split")
        self.assertEqual(result_rows[0].height, 1, "Expected height of the first rectangle after split")
        self.assertEqual(result_rows[1].height, 2, "Expected height of the second rectangle after split")


        # Test case 1: Split on edge rows
        rectangle_rows = Rectangle(0, 0, 7, 7)
        with unittest.mock.patch.object(rectangle_rows, 'choose_split_spot', return_value=(0, 2)):
            result_rows = rectangle_rows.split_room((0, 0))
        self.assertIsInstance(result_rows, list, "Expected a list of rectangles")
        self.assertEqual(len(result_rows), 2, "Expected two rectangles after split")
        self.assertEqual(result_rows[0].height, 0, "Expected height of the first rectangle after split")
        self.assertEqual(result_rows[1].height, 3, "Expected height of the second rectangle after split")

        # Test case 3: Do not split
        rectangle_no_split = Rectangle(0, 0, 2, 2)
        with unittest.mock.patch.object(rectangle_no_split, 'choose_split_spot', return_value=(-1, -1)):
            result_no_split = rectangle_no_split.split_room()
        self.assertIsInstance(result_no_split, list, "Expected a list with the original rectangle when no split")
        self.assertEqual(len(result_no_split), 1, "Expected one rectangle when no split")
        self.assertEqual(result_no_split[0], rectangle_no_split, "Expected the original rectangle when no split")

class TestLevel(unittest.TestCase):
    def test_add_room_to_grid(self):
        pass

    def test_draw_grid(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_render(self, mock_stdout):
        pass

if __name__ == '__main__':
    unittest.main()
