# find the ground state of a lithium hydride molecule

import matplotlib.pyplot as plt
from qiskit.chemistry.core import Hamiltonian, QubitMappingType
from qiskit.chemistry.drivers import PySCFDriver
from qiskit_aer import Aer


def plot_results(results):
    energies = [result ['energy'] for result in results]
    iterations = [result ['optimizer_evals'] for result in results]
    plt.plot (iterations, energies, marker='o')
    plt.xlabel ('Iterations')
    plt.ylabel ('Energy')
    plt.title ('Energy Convergence')
    plt.show ()


class LithiumHydride:
    def __init__(self, molecule):
        self.molecule = molecule

    def find_ground_state(self):
        driver = PySCFDriver (atom=self.molecule)
        qmolecule = driver.run ()
        operator = Hamiltonian (qubit_mapping=QubitMappingType.PARITY, two_qubit_reduction=True)
        qubit_op, aux_ops = operator.run (qmolecule)
        algorithm = VQE (qubit_op, aux_operators=aux_ops)
        backend = Aer.get_backend ('statevector_simulator')
        quantum_instance = QuantumInstance (backend=backend)
        result = algorithm.run (quantum_instance)
        print ('Ground state energy: ', result.eigenvalue.real)
        print ('Ground state wave function: ', result.eigenstate)


molecule = 'Li .0 H .0 0.0 1.6;'
lih = LithiumHydride (molecule)
lih.find_ground_state ()
plot_results (results)
