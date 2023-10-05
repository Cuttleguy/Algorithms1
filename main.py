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

# g1 = AndGate("G1")
# g2 = AndGate("G2")
# g3 = OrGate("G3")
# g4 = NotGate("G4")
# g5 = NorGate("G5")
# g6 = NandGate("G6")
# c1 = Connector(g1, g3)
# c2 = Connector(g2, g3)
# c3 = Connector(g3, g4)
#
#
# print(g4.get_output())
# print(g5.get_output())
# print(g6.get_output())
#
# #
# g7=AndGate("G7")
# g8=AndGate("G8")
# g9=NorGate("G9")
# c4=Connector(g7,g9)
# c5=Connector(g8,g9)
# print(g9.get_output())
#
half_adder=Circuit("HalfAdder1")