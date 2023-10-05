from gates import *

class ExtenderGate(UnaryGate):
    def __init__(self,llbl):
        super().__init__(llbl)
    def perform_gate_logic(self):
        a = self.get_pin()
        if a==1:
            return 1
        else:
            return 0
