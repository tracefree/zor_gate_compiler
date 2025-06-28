Short Python script to generate figures of a certain quantum circuit with Qiskit for a university assignment. The circuit is a subroutine of Grover's algorithm, the [phase query gate of the OR function](https://learning.quantum.ibm.com/course/fundamentals-of-quantum-algorithms/grovers-algorithm#phase-query-gates).

## Installation

In a Unix terminal, execute:

```
git clone bla
cd bla
python -m venv venv
chmod +x ./venv/bin/activate
./venv/bin/activate
./venv/bin/pip install -r requirements.txt
```

## Usage

```
./venv/bin/python main.py [NUMBER_OF_QUBITS]
```

Replace `[NUMBER_OF_QUBITS]` by an integer number greater than one. Defaults to 4 if omitted. The program then generates two png images in the working directory, one showing the virtual circuit in abstract terms and the other the same circuit in terms of the [native gate set of IBM's Heron architecture](https://docs.quantum.ibm.com/guides/native-gates#heron).

## License
The included generated images and the code are licensed under [CC0](https://creativecommons.org/public-domain/cc0/).
