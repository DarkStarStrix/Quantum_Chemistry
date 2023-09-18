# find the ground state of a lithium hydride molecule

import matplotlib.pyplot as plt
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import VQE
from qiskit.aqua.components.optimizers import L_BFGS_B
from qiskit.chemistry.components.initial_states import HartreeFock
from qiskit.chemistry.core import Hamiltonian, QubitMappingType
from qiskit.chemistry.drivers import PySCFDriver
from qiskit_aer import Aer


class LithiumHydride:
    def __init__(self, molecule):
        self.results = None
        self.molecule = molecule

    def find_ground_state(self):
        # Set up the PySCF driver and get the molecular information
        driver = PySCFDriver(atom=self.molecule)
        qmolecule = driver.run()

        # Set up the Hamiltonian and choose the mapping type
        operator = Hamiltonian(qubit_mapping=QubitMappingType.PARITY, two_qubit_reduction=True)
        qubit_op, aux_ops = operator.run(qmolecule)

        # Set up the VQE algorithm and run it on a simulator backend
        L_BFGS_B()
        HartreeFock(qubit_op.num_qubits, operator.molecule_info['num_orbitals'],
                    operator.molecule_info['num_particles'])
        algorithm = VQE(qubit_op, aux_operators=aux_ops)
        backend = Aer.get_backend('statevector_simulator')
        quantum_instance = QuantumInstance(backend=backend)
        result = algorithm.run(quantum_instance)

        # Print the ground state energy and corresponding wave function
        print('Ground state energy: ', result.eigenvalue.real)
        print('Ground state wave function: ', result.eigenstate)

    def plot_results(self):
        # Plot the results
        energies = [result['energy'] for result in self.results]
        iterations = [result['optimizer_evals'] for result in self.results]

        plt.plot(iterations, energies, marker='o')
        plt.xlabel('Iterations')
        plt.ylabel('Energy')
        plt.title('Energy Convergence')
        plt.show()


# Define the molecule
molecule = 'Li .0 H .0 0.0 1.6;'

# Create an instance of LithiumHydride and find the ground state
lih = LithiumHydride(molecule)
lih.find_ground_state()

# Plot the results
lih.plot_results()
