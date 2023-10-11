from gates import *
from gates import LogicGate
from gates.pin import Pin


class TwoWaySplitGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None
        self.outputA = Pin()
        self.outputB = Pin()

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

    def set_next_output(self, source):
        if self.outputA is None:
            self.outputA=source
        elif self.outputB is None:
            self.outputB=source
    def perform_gate_logic(self):
        a=self.get_pin()
        return a

    def get_output(self):
        if self.outputA.get_output() is not None:
            self.outputA.get_to().set_next_pin(self.perform_gate_logic())

        if self.outputB.get_output() is not None:
            self.outputB.get_to().set_next_pin(self.perform_gate_logic())
        return self.perform_gate_logic()
