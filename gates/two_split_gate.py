from gates import *


class TwoWaySplitGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None
        self.outputA = None
        self.outputB = None

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
        if self.outputA is not None:
            source = self.outputB
        else:
            if self.outputB is not None:
                source = self.outputB
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

    def perform_gate_logic(self):
        self.outputA, self.outputB = self.pin

    def get_output(self):
        self.perform_gate_logic()
        return [self.outputA, self.outputB]
