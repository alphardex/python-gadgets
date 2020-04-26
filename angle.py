"""
人性化的度分秒制角度计算

Test cases are from: https://wenku.baidu.com/view/ff78bc144a35eefdc8d376eeaeaad1f34693118b.html

Test positive::
    >>> a = Angle(-1, -1, -1)
    Traceback (most recent call last):
      ...
    ValueError: value must be >= 0

Test convertion::

    >>> a = Angle(1, 0, 0)
    >>> a.to_minute()
    Angle(0.0°, 60.0', 0.0'')

    >>> a = Angle(0, 1, 0)
    >>> a.to_second()
    Angle(0.0°, 0.0', 60.0'')

    >>> a = Angle(0.75, 0, 0)
    >>> a.to_minute()
    Angle(0.0°, 45.0', 0.0'')
    >>> a.to_second()
    Angle(0.0°, 0.0', 2700.0'')

    >>> a = Angle(34.37, 0, 0)
    >>> a.to_dms()
    Angle(34.0°, 22.0', 12.0'')

    >>> a = Angle(0, 0, 30)
    >>> a.to_minute()
    Angle(0.0°, 0.5', 0.0'')

    >>> a = Angle(0, 120, 0)
    >>> a.to_degree()
    Angle(2.0°, 0.0', 0.0'')

    >>> a = Angle(72, 25, 12)
    >>> a.to_degree()
    Angle(72.42°, 0.0', 0.0'')

Test operator::

    >>> a1 = Angle(12,36,56)
    >>> a2 = Angle(45,24,35)
    >>> a1 + a2
    Angle(58.0°, 1.0', 31.0'')

    >>> a1 = Angle(79, 45, 00)
    >>> a2 = Angle(61, 48, 49)
    >>> a1 - a2
    Angle(17.0°, 56.0', 11.0'')

    >>> a = Angle(21, 31, 27)
    >>> a * 3
    Angle(64.0°, 34.0', 21.0'')

    >>> a = Angle(63, 21, 39)
    >>> a / 3
    Angle(21.0°, 7.0', 13.0'')

    >>> a = Angle(106, 6, 25)
    >>> a / 5
    Angle(21.0°, 13.0', 17.0'')
"""
import abc
from math import modf


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = f'_{prefix}#{index}'
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name) if instance else self

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):
    @abc.abstractmethod
    def validate(self, instance, value):
        """Return validated values or raise ValueError"""

    def __set__(self, instance, value):
        self.validate(instance, value)
        super().__set__(instance, value)


class Unit(Validated):
    """A unit whose number is >= 0"""

    def validate(self, instance, value):
        if value < 0:
            raise ValueError('value must be >= 0')
        return value


class EntityMeta(type):
    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = f'_{type_name}#{key}'
                cls._field_names.append(key)


class Entity(metaclass=EntityMeta):
    @classmethod
    def field_names(cls):
        yield from (name for name in cls._field_names)


class Angle(Entity):
    degree = Unit()
    minute = Unit()
    second = Unit()

    def __init__(self, degree: float, minute: float, second: float):
        self.degree = float(degree)
        self.minute = float(minute)
        self.second = float(second)

    def __repr__(self):
        return fr"{type(self).__name__}({self.degree}°, {self.minute}', {self.second}'')"

    def to_degree(self):
        return Angle(self.degree + self.minute / 60.0 + self.second / 3600.0, 0.0, 0.0)

    def to_minute(self):
        return Angle(0.0, self.degree * 60.0 + self.minute + self.second / 60.0, 0.0)

    def to_second(self):
        return Angle(0.0, 0.0, self.degree * 3600.0 + self.minute * 60.0 + self.second)

    def to_dms(self):
        d_frac, d_int = modf(self.degree)
        m_frac, m_int = modf(d_frac * 60.0)
        s_int = round(m_frac * 60.0)
        return Angle(d_int, m_int, s_int)

    def __add__(self, other):
        d = self.degree + other.degree
        m = self.minute + other.minute
        s = self.second + other.second
        if s > 60.0:
            s -= 60.0
            m += 1.0
        if m > 60.0:
            m -= 60.0
            d += 1.0
        return Angle(d, m, s)

    def __sub__(self, other):
        if other.second > self.second:
            self.second += 60.0
            self.minute -= 1.0
        if other.minute > self.minute:
            self.minute += 60.0
            self.degree -= 1.0
        d = self.degree - other.degree
        m = self.minute - other.minute
        s = self.second - other.second
        return Angle(d, m, s)

    def __mul__(self, scalar: float):
        d = self.degree * scalar
        m = self.minute * scalar
        s = self.second * scalar
        if s > 60.0:
            s -= 60.0
            m += 1.0
        if m > 60.0:
            m -= 60.0
            d += 1.0
        return Angle(d, m, s)

    def __truediv__(self, scalar: float):
        d, remainder = divmod(self.degree, scalar)
        self.minute += remainder * 60
        m, remainder = divmod(self.minute, scalar)
        self.second += remainder * 60
        s = self.second / scalar
        return Angle(d, m, s)
