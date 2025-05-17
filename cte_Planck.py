import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dados fornecidos
dados = {
    "Tf (V)": [0.201, 0.403, 0.644, 0.841, 1.028, 1.225, 1.432, 1.603, 1.879, 2.039,
               2.233, 2.439, 2.683, 2.8, 3.137, 3.204, 3.485, 3.623, 3.878, 4.074,
               4.285, 4.407, 4.657, 4.841, 5.091, 5.203, 5.453, 5.6, 5.81, 6.015,
               6.22, 6.47, 6.64, 6.88, 7.06, 7.217, 7.4, 7.66, 7.81, 8.03,
               8.23, 8.454, 8.59, 8.85, 9.14, 9.2, 9.44, 9.692, 9.81, 10.21,
               10.4, 10.61, 10.886, 11.1, 11.23, 11.39, 11.67, 11.8, 11.941],
    "R (Ohm)": [0.25605, 0.34592, 0.46802, 0.56179, 0.64130, 0.71345, 1.20437, 0.84191,
                 0.92380, 0.96727, 1.01592, 1.06182, 1.11978, 1.14613, 1.21448, 1.22524,
                 1.27283, 1.30371, 1.35405, 1.38807, 1.42123, 1.44208, 1.48123, 1.50529,
                 1.54601, 1.56387, 1.59865, 1.62319, 1.65057, 1.67269, 1.70411, 1.73925,
                 1.80926, 1.78701, 1.81491, 1.82616, 1.85464, 1.88206, 1.90024, 1.92566,
                 1.95024, 1.97523, 1.98843, 2.01595, 2.04933, 2.05357, 2.07930, 2.10147,
                 2.11879, 2.15401, 2.17573, 2.19669, 2.21711, 2.24242, 2.25050, 2.26441,
                 2.29724, 2.30019, 2.31325]
}

df = pd.DataFrame(dados)

# Constantes
R0 = min(df["R (Ohm)"])  # Menor resistência (temperatura ambiente)
T0 = 293  # Temperatura ambiente (em Kelvin)
beta = 1.22  # Valor típico para tungstênio

# Calcula a temperatura para cada resistência
df["T (K)"] = T0 * (df["R (Ohm)"] / R0)**(1/beta)

# Usa a tensão no sensor (Tf) como intensidade (aproximada)
df["ln(Tf)"] = np.log(df["Tf (V)"])
df["1/T"] = 1 / df["T (K)"]

# Ajuste linear
slope, intercept, r_value, p_value, std_err = linregress(df["1/T"], df["ln(Tf)"])

# Constantes
kB = 1.380649e-23  # Constante de Boltzmann (J/K)
c = 3e8  # Velocidade da luz (m/s)
lambda_ = 1000e-9  # Comprimento de onda (1000 nm)

# Calcula a constante de Planck
h = (-slope * lambda_ * kB / c)

# Resultados
print(f"Inclinação: {slope:.4e}")
print(f"Constante de Planck (h): {h:.4e} J.s")
print(f"R² do ajuste: {r_value**2:.4f}")

# Plot do ajuste
plt.figure(figsize=(10, 6))
plt.scatter(df["1/T"], df["ln(Tf)"], color="blue", label="Dados experimentais")
plt.plot(df["1/T"], slope * df["1/T"] + intercept, color="red",
         label=f"Ajuste linear\nInclinação: {slope:.4e}")
plt.xlabel("1/T (1/K)")
plt.ylabel("ln(Tf) (V)")
plt.title("Aproximação de Wien para Determinação da Constante de Planck")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("ajuste_constante_planck.png", dpi=300)
plt.show()
