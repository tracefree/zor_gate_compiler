import sys
from qiskit_aer import AerSimulator
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import OrGate
from qiskit import transpile

DEFAULT_NUMBER_QUBITS = 4

if __name__ == "__main__":
    number_qubits = DEFAULT_NUMBER_QUBITS
    if len(sys.argv) == 2:
        try:
            number_qubits = int(sys.argv[1])
            if number_qubits < 2:
                number_qubits = DEFAULT_NUMBER_QUBITS
        except:
            number_qubits = DEFAULT_NUMBER_QUBITS

    qc = QuantumCircuit(number_qubits)
    or_gate = OrGate(number_qubits - 1)

    qc.append(or_gate, reversed(range(0, number_qubits)))
    for i in range(1, number_qubits):
        qc.cz(0,i)

    qc.draw("mpl", filename="ZOr_virtual_{number_qubits:d}.png".format(number_qubits = number_qubits))

    backend = AerSimulator()
    basis_gates = ["cz", "rz", "sx", "x", "id", "reset"]
    qc_compiled = transpile(qc, basis_gates=basis_gates)
    qc_compiled.draw("mpl", filename="ZOr_compiled_{number_qubits:d}.png".format(number_qubits = number_qubits))
