class Color:
  """Color
  
  The responsibility of color is to hold and provide information about itself.
  Color has a few convenience methods for comparing them and converting to a tuple.
  
  Attributes:
    _red (int): Red value
    _green (int): Green value
    _blue (int): Blue value
    _alpha (int): Alpha or opacity
  """
  def __init__(self, red, green, blue, alpha = 255):
    """Constructs a new color using the specified red, green, blue, and alpha values
    The alpha value is the color's opacity
    
    Args:
      red (int): Red value
      green (int): Green value
      blue (int): Blue value
      alpha (int): Alpha or opacity
    """
    self._red = red
    self._green = green
    self._blue = blue
    self._alpha = alpha
    
  def to_tuple(self):
    """Gets the color as a tuple of four values
    (red, green, blue, alpha)
    
    Returns:
      Tuple (int, int, int, int): Color as a tuple
    """
    return (self._red, self._green, self._blue, self._alpha)