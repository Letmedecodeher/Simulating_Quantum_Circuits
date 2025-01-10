from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.primitives import sampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2,2)

qc.h(0)

qc.cx(0,1)

qc.measure([0,1],[0,1])

simulator = AerSimulator()
result = simulator.run(qc, shots = 1024).result()
counts = result.get_counts(qc)

print("measurement result : ",counts)
plot_histogram(counts)
plt.show()

