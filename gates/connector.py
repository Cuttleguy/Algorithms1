class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


    def get_pin_a(self):
        if self.pin_a == None:
            return input(
                f"Enter pin A input for gate \
                {self.get_label()}: "
            )
        else:
            return self.pin_a.get_from().get_output()