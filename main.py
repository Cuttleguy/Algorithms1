from fraction import *
from gates import *
x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
print(x + y)
print(y - x)
print(x * y)
print(y/x)
print(x == y)
print(x > y)
print(x < y)
g1 = AndGate("G1")
g1.get_output()
g2 = OrGate("G2")
g2.get_output()


g2.get_output()

g3 = NotGate("G3")
g3.get_output()