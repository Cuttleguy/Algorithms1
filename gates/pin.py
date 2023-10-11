class Pin:
    def __init__(self):
        self.value=None

    def set_value(self,value):
        self.value=value
    def get_output(self):
        return self.value
    def __int__(self):
        return self.value