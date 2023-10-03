from gates.logic_gate import *
class UnaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.pin = None

    def get_pin(self):
        return int(input(f"Enter pin input for gate \
            {self.get_label()}: "))
    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")