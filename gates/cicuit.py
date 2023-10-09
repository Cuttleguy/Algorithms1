from gates import *
from gates import Connector


class Circuit(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.gates = []
        self.connectors = []
        self.gatesAutomatedOutput=[]
    def add_gate(self,gate):
        self.gates.append(gate)
    def add_connecter(self,fgate,tgate):
        self.connectors.append(Connector(fgate, tgate))
        self.gatesAutomatedOutput.append(fgate)
    def perform_gate_logic(self):
        for gate in self.gates:
            if gate not in self.gatesAutomatedOutput:
                gate.getOutput()