from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService

def transpile_remote(circuits, optimization_level, backend_name):
    service = QiskitRuntimeService(channel="ibm_quantum")
    backend = service.get_backend(backend_name)
    
    results = []
    pass_manager = generate_preset_pass_manager(optimization_level=optimization_level, backend=backend)
    
    for circuit in circuits:
        transpiled_circuit = pass_manager.run(circuit)
        reduced_depth = transpiled_circuit.depth()  # Get the depth of the transpiled circuit
        results.append((transpiled_circuit, reduced_depth))  # Store both circuit and its depth
    
    return results

if __name__ == "__main__":
    from qiskit_serverless import get_arguments, save_result
    
    arguments = get_arguments()
    circuits = arguments.get("circuits")
    backend_name = arguments.get("backend_name")
    optimization_level = arguments.get("optimization_level")

    results = transpile_remote(circuits, optimization_level, backend_name)
    save_result({"transpiled_circuits": results})