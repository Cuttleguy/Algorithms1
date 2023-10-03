from logic_gate import *

class BinaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(self, lbl)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        return int(input(f"Enter pin A input for gate \
            {self.get_label()}: "))

    def get_pin_b(self):
        return int(input(f"Enter pin B input for gate \
            {self.get_label()}: "))