from gates import UnoOutputGate
from gates.logic_gate import *
class UnaryGate(UnoOutputGate):

    def __init__(self, lbl):
        UnoOutputGate.__init__(self, lbl)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
    def set_next_output(self,source):
        if self.output == None:
            self.output = source