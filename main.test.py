# test_color_pairing.py

import unittest
from color_pairing import get_color_from_pair_number, get_pair_number_from_color, MAJOR_COLORS, MINOR_COLORS

class TestColorPairing(unittest.TestCase):
  """
  Unit tests for the color_pairing module.
  """

  def test_number_to_pair(self):
    """Tests the conversion from pair number to colors."""
    self.assertEqual(get_color_from_pair_number(1), ('White', 'Blue'))
    self.assertEqual(get_color_from_pair_number(4), ('White', 'Brown'))
    self.assertEqual(get_color_from_pair_number(5), ('White', 'Slate'))
    self.assertEqual(get_color_from_pair_number(6), ('Red', 'Blue'))
    self.assertEqual(get_color_from_pair_number(10), ('Red', 'Slate'))
    self.assertEqual(get_color_from_pair_number(11), ('Black', 'Blue'))
    self.assertEqual(get_color_from_pair_number(15), ('Black', 'Slate'))
    self.assertEqual(get_color_from_pair_number(21), ('Violet', 'Blue'))
    self.assertEqual(get_color_from_pair_number(25), ('Violet', 'Slate'))

  def test_pair_to_number(self):
    """Tests the conversion from colors to pair number."""
    self.assertEqual(get_pair_number_from_color('White', 'Blue'), 1)
    self.assertEqual(get_pair_number_from_color('White', 'Brown'), 4)
    self.assertEqual(get_pair_number_from_color('White', 'Slate'), 5)
    self.assertEqual(get_pair_number_from_color('Red', 'Blue'), 6)
    self.assertEqual(get_pair_number_from_color('Red', 'Orange'), 7)
    self.assertEqual(get_pair_number_from_color('Black', 'Orange'), 12)
    self.assertEqual(get_pair_number_from_color('Violet', 'Slate'), 25)

  def test_invalid_pair_number(self):
    """Tests handling of invalid pair numbers."""
    # Test out of range high
    with self.assertRaises(Exception) as cm:
      get_color_from_pair_number(len(MAJOR_COLORS) * len(MINOR_COLORS) + 1)
    self.assertIn("Major color index out of range", str(cm.exception))

    # Test zero
    with self.assertRaises(ValueError) as cm:
      get_color_from_pair_number(0)
    self.assertIn("Pair number must be a positive integer", str(cm.exception))

    # Test negative
    with self.assertRaises(ValueError) as cm:
      get_color_from_pair_number(-1)
    self.assertIn("Pair number must be a positive integer", str(cm.exception))

  def test_invalid_colors(self):
    """Tests handling of invalid color names."""
    with self.assertRaises(ValueError) as cm:
      get_pair_number_from_color('NonExistentMajor', 'Blue')
    self.assertIn("Major color 'NonExistentMajor' not found", str(cm.exception))

    with self.assertRaises(ValueError) as cm:
      get_pair_number_from_color('White', 'NonExistentMinor')
    self.assertIn("Minor color 'NonExistentMinor' not found", str(cm.exception))

if __name__ == '__main__':
  unittest.main()
