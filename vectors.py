import math

class Vector2D():
    def __init__(self, x:float, y:float) -> None:
        self._x, self._y = x, y
    def __repr__(self) -> str:
        return f'Vector2D:(x: {self._x}, y:{self._y})'

    @property
    def xy(self) -> tuple[int|float]: return (self._x, self._y)
    @property
    def x(self) -> int|float: return self._x
    @property
    def y(self) -> int|float: return self._y
    @property
    def size(self) -> int|float: return math.hypot(*self.xy)

    def dot_product(self, other_vector:"Vector2D") -> int|float:
        return (self._x*other_vector._x) + (self._y*other_vector._y)

    def __add__(self, other):
        if isinstance(other, Vector2D): return Vector2D(self._x+other._x, self._y+other._y)
        elif isinstance(other,(tuple, list)): return Vector2D(self._x+other[0], self._y+other[1])
        return NotImplemented
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector2D): return Vector2D(self._x-other._x, self._y-other._y)
        elif isinstance(other,(tuple, list)): return Vector2D(self._x-other[0], self._y-other[1])
        return NotImplemented
    def __rsub__(self, other):
        if isinstance(other, Vector2D): return Vector2D(other._x-self._x, other._y-self._y)
        elif isinstance(other,(tuple, list)): return Vector2D(other[0]-self._x, other[1]-self._y)
        return NotImplemented
    def __isub__(self, other):
        return self.__sub__(other)

    def __pow__(self, other):
        if isinstance(other, Vector2D): return Vector2D(self._x**other._x, self._y**other._y)
        elif isinstance(other, (tuple, list)): return Vector2D(self._x**other[0], self._y**other[1])
        elif isinstance(other, (int, float)): return Vector2D(self._x**other, self._y**other)
        return NotImplemented
    def __rpow__(self, other):
        if isinstance(other, Vector2D): return Vector2D(other._x**self._x, other._y**self._y)
        elif isinstance(other, (tuple, list)): return Vector2D(other[0]**self._x, other[1]**self._y)
        elif isinstance(other, (int, float)): return Vector2D(other**self._x, other**self._y)
        return NotImplemented
    def __ipow__(self, other):
        return self.__pow__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector2D): return Vector2D(self._x/other._x, self._y/other._y)
        elif isinstance(other, (tuple, list)): return Vector2D(self._x/other[0], self._y/other[1])
        elif isinstance(other, (int, float)): return Vector2D(self._x/other, self._y/other)
        return NotImplemented
    def __rtruediv__(self, other):
        if isinstance(other, Vector2D): return Vector2D(other._x/self._x, other._y/self._y)
        elif isinstance(other, (tuple, list)): return Vector2D(other[0]/self._x, other[1]/self._y)
        elif isinstance(other, (int, float)): return Vector2D(other/self._x, other/self._y)
        return NotImplemented
    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        if isinstance(other, Vector2D): return Vector2D(self._x//other._x, self._y//other._y)
        elif isinstance(other, (tuple, list)): return Vector2D(self._x//other[0], self._y//other[1])
        elif isinstance(other, (int, float)): return Vector2D(self._x//other, self._y//other)
        return NotImplemented
    def __rfloordiv__(self, other):
        if isinstance(other, Vector2D): return Vector2D(other._x//self._x, other._y//self._y)
        elif isinstance(other, (tuple, list)): return Vector2D(other[0]//self._x, other[1]//self._y)
        elif isinstance(other, (int, float)): return Vector2D(other//self._x, other//self._y)
        return NotImplemented
    def __ifloorediv__(self, other):
        return self.__floordiv__(other)

    def __mul__(self, other):
        if isinstance(other, Vector2D): return Vector2D(self._x*other._x, self._y*other._y)
        elif isinstance(other, (tuple, list)): return Vector2D(self._x*other[0], self._y*other[1])
        elif isinstance(other, (int, float)): return Vector2D(self._x*other, self._y*other)
        return NotImplemented
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        for a in [self.x, self._y]: yield a

    def __int__(self): return int(self.size)
    def __float__(self): return float(self.size)
    def __reversed__(self): return Vector2D(self._y, self._x)
    def __neg__(self): return Vector2D(-self._x,-self._y)

# Vetores adicionais apenas para facilitar o entendimento a longo prazo.

class Pos2D(Vector2D):
    def __init__(self, x, y):
        super().__init__(x, y)

class Velo2D(Vector2D):
    def __init__(self, x, y):
        super().__init__(x, y)

class Force2D(Vector2D):
    def __init__(self, x, y):
        super().__init__(x, y)

class Accel2D(Vector2D):
    def __init__(self, x, y):
        super().__init__(x, y)

class Scale2D(Vector2D):
    def __init__(self, x, y):
        super().__init__(x, y)