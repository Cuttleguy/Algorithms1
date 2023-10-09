from gates import *
from gates.logic_gate import *
class UnoOutputGate(LogicGate):
    def __init__(self, lbl):

        super().__init__(lbl)
        self.output = None
    def get_output(self):
        return self.perform_gate_logic()
