import numpy as np
from qiskit.quantum_info import Operator, Pauli
from scipy.linalg import expm

# Creating the Hamiltonian components (XX, YY, ZZ)
XX = Operator(Pauli('XX'))
YY = Operator(Pauli('YY'))
ZZ = Operator(Pauli('ZZ'))
H2 = XX + YY + ZZ

# Calculating the unitary matrix: exp(i * pi/2 * H2)
# Result: U = exp(i * (pi/2) * (XX + YY + ZZ))
U = expm(1j * (np.pi / 2) * H2.data)

# Printing the result cleanly (Reset small values)
print("Result Matrix (U):")
print(np.round(U, 10))

# Identity matrix check
is_identity = np.allclose(np.abs(U), np.eye(4))
print(f"\nIs this a Unit Matrix (excluding Global Phase)? {is_identity}")

