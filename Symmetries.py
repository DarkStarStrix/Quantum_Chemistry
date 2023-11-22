import qiskit.chemistry
import qiskit.chemistry.drivers
import qiskit.chemistry.symmetry.cg_symmetry

# Define the molecule
molecule = 'H .0 .0 .0; H .0 .0 0.74'
driver = qiskit.chemistry.drivers.PySCFDriver(atom=molecule)
qmolecule = driver.run()

# Compute the symmetry group
symmetry = qiskit.chemistry.symmetry.cg_symmetry.CGSymmetry()

# Print the symmetry group
print(symmetry.compute_group(qmolecule))
