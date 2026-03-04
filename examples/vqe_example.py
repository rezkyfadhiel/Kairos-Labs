"""
Variational Quantum Eigensolver (VQE) example.
Finds ground state energy of molecular Hamiltonian.
"""

from src.quantum.algorithms import VQE
from src.quantum.circuits import ParametrizedCircuit

def example_h2_molecule():
    """
    VQE for H2 molecule ground state.
    """
    # Define molecular Hamiltonian (H2)
    h2_hamiltonian = [
        (0.398, "II"),
        (-0.398, "ZZ"),
        (-0.0100, "ZI"),
        (-0.0100, "IZ")
    ]
    
    # Create VQE solver
    vqe = VQE(
        hamiltonian=h2_hamiltonian,
        ansatz="UCCSD",
        optimizer="COBYLA"
    )
    
    # Find ground state
    result = vqe.solve()
    print(f"Ground state energy: {result['energy']}")
    print(f"Optimal parameters: {result['params']}")

if __name__ == "__main__":
    example_h2_molecule()
  
