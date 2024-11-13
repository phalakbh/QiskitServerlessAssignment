from qiskit.circuit.random import random_circuit

def generate_random_circuits(depths):
    circuits = []
    for depth in depths:
        # Generate a random circuit with 5 qubits and the specified depth
        circuit = random_circuit(num_qubits=5, depth=depth, measure=True)
        circuits.append(circuit)
    return circuits