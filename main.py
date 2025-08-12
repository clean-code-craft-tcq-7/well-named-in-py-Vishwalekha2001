# color_pairing.py

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def color_pair_to_string(major_color, minor_color):
  """
  Converts a major and minor color into a formatted string.
  """
  return f'{major_color} {minor_color}'

def get_color_from_pair_number(pair_number):
  """
  Retrieves the major and minor color from a given pair number.

  Args:
    pair_number (int): The 1-based pair number.

  Returns:
    tuple: A tuple containing the major and minor color strings.

  Raises:
    Exception: If the pair number results in an out-of-range index for major or minor colors.
  """
  if not isinstance(pair_number, int) or pair_number <= 0:
      raise ValueError("Pair number must be a positive integer.")

  zero_based_pair_number = pair_number - 1
  num_minor_colors = len(MINOR_COLORS)
  num_major_colors = len(MAJOR_COLORS)

  major_index = zero_based_pair_number // num_minor_colors
  if major_index >= num_major_colors:
    raise Exception(f'Major color index out of range for pair number {pair_number}.')

  minor_index = zero_based_pair_number % num_minor_colors
  if minor_index >= num_minor_colors: # This check is redundant due to modulo, but good for clarity
    raise Exception(f'Minor color index out of range for pair number {pair_number}.')

  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
  """
  Calculates the 1-based pair number from given major and minor colors.

  Args:
    major_color (str): The major color string.
    minor_color (str): The minor color string.

  Returns:
    int: The 1-based pair number.

  Raises:
    ValueError: If major_color or minor_color is not found in the defined lists.
  """
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise ValueError(f"Major color '{major_color}' not found in defined MAJOR_COLORS.")
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise ValueError(f"Minor color '{minor_color}' not found in defined MINOR_COLORS.")

  return major_index * len(MINOR_COLORS) + minor_index + 1

def print_color_chart():
    """
    Prints the complete color code chart.
    """
    print("--- Color Code Chart ---")
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for i in range(1, total_pairs + 1):
        try:
            major, minor = get_color_from_pair_number(i)
            print(f"{i:2}: {major_color} {minor_color}")
        except Exception as e:
            print(f"Error getting pair {i}: {e}")
    print("------------------------")

# This block ensures print_color_chart() runs only when color_pairing.py is executed directly
if __name__ == '__main__':
    print_color_chart()
