from gates.binary_gate import *

class XorGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 ^ b == 1:
            return 1
        else:
            return 0
