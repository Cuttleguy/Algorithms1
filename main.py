from fraction import *
from gates import *
from gates.cicuit import Circuit
from gates.two_split_gate import TwoWaySplitGate
import time
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

#
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
#
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
# #
# split=TwoWaySplitGate("Split")
# andGate=AndGate("And")
# c1=Connector(split,andGate)
# c2=Connector(split,andGate)
#
# print(andGate.get_output())
print(sum_of_n(10))
for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n_2(100000))
print("Other Algorithm")
for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n_3(10**100))

coll=[0,5,6,7,7,100,-4500,-10000,100000]
print("Min is %d required %10.7f seconds" % findMinLin(coll))
print("Min is %d required %10.7f seconds" % findMinQuad(coll))

print(anagram_solution_1("apple", "pleap"))  # expected: True
print(anagram_solution_1("abcd", "dcba"))  # expected: True
print(anagram_solution_1("abcd", "dcda"))  # expected: False


print(anagram_solution_2("apple", "pleap"))  # expected: True
print(anagram_solution_2("abcd", "dcba"))  # expected: True
print(anagram_solution_2("abcd", "dcda"))  # expected: False

print(anagram_solution_4("apple", "pleap"))  # expected: True
print(anagram_solution_4("abcd", "dcba"))  # expected: True
print(anagram_solution_4("abcd", "dcda"))  # expected: False