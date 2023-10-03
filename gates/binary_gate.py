from gates.logic_gate import *

class BinaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        return int(input(f"Enter pin A input for gate \
            {self.get_label()}: "))

    def get_pin_b(self):
        return int(input(f"Enter pin B input for gate \
            {self.get_label()}: "))

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")