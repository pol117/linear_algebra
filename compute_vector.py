import vector
import math


v1 = vector.Vector([7.887, 4.138])
v2 = vector.Vector([-8.802, 6.776])
v3 = vector.Vector([-5.955, -4.904, -1.874])
v4 = vector.Vector([-4.496, -8.755, 7.103])
v5 = vector.Vector([3.183, -7.627])
v6 = vector.Vector([-2.668, 5.319])
v7 = vector.Vector([7.35, 0.221, 5.188])
v8 = vector.Vector([2.751, 8.259, 3.985])
v0 = vector.Vector([0, 0, 0])
v = vector.Vector([-7.579, -7.88])
w = vector.Vector([22.737, 23.64])
#v = vector.Vector([-2.029, 9.97, 4.172])
#w = vector.Vector([-9.231, -6.639, -7.245])
#v = vector.Vector([-2.328, -7.284, -1.214])
#w = vector.Vector([-1.821, 1.072, -2.94])
#v = vector.Vector([2.118, 4.827])
#w = vector.Vector([0, 0])
#v12 = vector.Vector([-9.88, -3.264, -8.159])
#b = vector.Vector([-2.155, -9.353, -9.473])
v12 = vector.Vector([3.009, -6.172, 3.692, -2.51])
b = vector.Vector([6.404, -9.144, 2.759, 8.718])
v14_1 = vector.Vector([8.462, 7.893, -8.187])
w14_1 = vector.Vector([6.984, -5.975, 4.778])
v14_2 = vector.Vector([-8.987, -9.838, 5.031])
w14_2 = vector.Vector([-4.268, -1.861, -8.866])
v14_3 = vector.Vector([1.5, 9.547, 3.691])
w14_3 = vector.Vector([-6.007, 0.124, 5.772])

#print v0.normalized()
print 'v1 + v2'
print v1.puls(v2)
print 'v3 - v4'
print v3.minus(v4)
print 'v5 * 7.41'
print v5.scalar(7.41)
print 'lesson6 answer'
print v1.magnitude()
print v2.magnitude()
print v3.normalized()
#print v0.normalized()
print "lesson8 answer is:"
print v1.dot(v2)
print v3.dot(v4)
print v5.angle(v6, in_degrees=False)
#print math.degrees(v7.angle(v8))
print v7.angle(v8, in_degrees=True)
print "lesson10 answer is:"
#print v.dot(w)
print v.dot(w)
print v.normalized()
print w.normalized()
print v.normalized().dot(w.normalized())
print v.angle(w)
print v.is_parallel_to(w)
print v.is_orthogonal_to(w)

print "lesson12 answer is:"
print v12.component_parallel_to(b)
print v12.component_orthogonal_to(b)

print "lesson14 answer is:"
print v14_1.cross(w14_1)
print v14_2.area_of_parallogram(w14_2)
print v14_3.area_of_triangle(w14_3)
