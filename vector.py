#from math import sqrt
#from math import acos
#from math import degrees
from decimal import Decimal, getcontext
import math
getcontext().prec = 30

class Vector():
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'No unique orthogonal component'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Cross function is only defined for 2d and 3d'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(x) for x in coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def puls(self, v):
        new_coordinate = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinate)
        #other method
        #new_coordinate = []
        #for i in range(v.dimension):
        #    new_coordinate.append(self.coordinates[i] + v.coordinates[i])
        #return Vector(new_coordinate)


    def minus(self, v):
        new_coordinate = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinate)


    def scalar(self, c):
        new_coordinate = [x*Decimal(c) for x in self.coordinates]
        return Vector(new_coordinate)
        pass

    #my method
    #def magnitude(self):
    #    sum = 0
    #    for x in self.coordinates:
    #        sum += x ** 2
    #    result = sum ** 0.5
    #    return result
    #    pass

    #teater'code
    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sum(coordinates_squared).sqrt()


    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.scalar(Decimal('1.0') / magnitude)
            pass
        except Exception as e:
            #e.args += ('Cannot normalized the zero vector',)
            #raise
            raise Exception('Cannot normalized the zero vector')



    def dot(self, v):
        multiply = [x * y for x, y in zip(self.coordinates, v.coordinates)]
        return sum(multiply)


    #my method
    #def angle(self, v):
    #    try:
    #        result = self.dot_product(v)/(self.magnitude() * v.magnitude())
    #        return math.acos(result)
    #        pass
    #    except ZeroDivisionError:
    #        raise ZeroDivisionError('Cannot calculate the zero angle')


    #teacher's method
    def angle(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = math.acos(u1.dot(u2))
            if in_degrees == True:
                return math.degrees(angle_in_radians)
            else:
                return angle_in_radians
            pass
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e


    def parallesism(self, v):
        if self.normalized() == v.normalized():
            return True
        elif self.normalized() == v.normalized().scalar(-1):
            return True
        else:
            return False


    def is_orthogonal_to(self, v,tolerance=1e-10):
        return abs(self.dot(v))<tolerance


    def is_parallel_to(self, v):
        return(self.is_zero() or
               v.is_zero() or
               self.angle(v, in_degrees = False) == 0 or
               self.angle(v, in_degrees = False) == math.pi)


    def is_zero(self,tolerance=1e-10):
        return self.magnitude()< tolerance


    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            c = self.dot(u)
            return u.scalar(c)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


    def cross(self,v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinate = [  y_1*z_2 - y_2*z_1 ,
                              -(x_1*z_2 - x_2*z_1),
                                x_1*y_2 - x_2*y_1]
            return Vector(new_coordinate)
            pass
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif msg == 'too many values to unpack' or msg == 'need more than value to unpack':
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e


    def area_of_parallogram(self,v):
        cross_product = self.cross(v)
        return cross_product.magnitude()


    def area_of_triangle(self,v):
        return self.area_of_parallogram(v) / Decimal('2.0')


    def __getitem__(self, item):
        return self.coordinates[item]
