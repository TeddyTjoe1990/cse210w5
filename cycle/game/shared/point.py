class Point:
  """A distance from a relative origin (0, 0)
  
  The responsibility of point is to hold and provide information about itself.
  Point has a few convenience methods for adding, scaling, and comparing them.
  
  Attributes:
    _x (integer): Horizontal distance from the origin
    _y (integer): Vertical distance from the origin
  """
  def __init__(self, x, y):
    """Constructs a new point using the specified x and y values
    
    Args:
      x (int): Specified x value
      y (int): Specified y value
    """
    self._x = x
    self._y = y
    
  def add(self, other):
    """Gets a new point that is the sum of this and the given one
    
    Args:
      other (Point): Point to add
      
    Returns:
      point: New point that is the sum
    """
    x = self._x + other.get_x()
    y = self._y + other.get_y()
    return Point(x, y)
  
  def equals(self, other):
    """Whether or not this point is equal to the given one
    
    Args:
      other (Point): Point to compare
      
    Returns:
      boolean: True if both x and y are equal, False is otherwise
    """
    return self._x == other.get_x() and self._y == other.get_y()
  
  def get_x(self):
    """Gets the horizontal distance
    
    Returns:
      integer: Horizontal distance
    """
    return self._x
  
  def get_y(self):
    """Gets the vertical distance
    
    Returns:
      integer: Vertical distance
    """
    return self._y
  
  def reverse(self):
    """Reverses the point by interventing both x and y values
    
    Returns:
      Point: New point that is reversed
    """
    new_x = self._x * -1
    new_y = self._y * -1
    return Point(new_x, new_y)
  
  def scale(self, factor):
    """Scales the point by the provided factor

    Args:
        factor (int): Amount to scale
        
    Returns:
      Point: New point that is scaled
    """
    return Point(self._x * factor, self._y * factor)
    
    
    