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
#Logic Gates


# g1 = AndGate("G1")
# print(g1.get_output())
#
#
#
# g2 = OrGate("G2")
# print(g2.get_output())
#
#
#
# g3 = NotGate("G3")
# print(g3.get_output())

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)