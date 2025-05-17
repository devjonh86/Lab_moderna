import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Dados experimentais
temperatura = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200,
                        1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                        2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000,
                        3100, 3200, 3300, 3400, 3500, 3655])
resistividade = np.array([5.64, 8.06, 10.74, 13.54, 16.46, 19.47, 22.58, 25.7,
                          28.85, 32.02, 35.24, 38.58, 41.85, 45.22, 48.63,
                          52.08, 55.57, 59.1, 62.65, 66.25, 69.9, 73.55, 77.25,
                          81.0, 84.7, 88.5, 92.3, 96.2, 100.0, 103.8, 107.8,
                          111.7, 115.7, 121.8])

# Normaliza a resistividade e calcula os logaritmos
ln_T = np.log(temperatura)
ln_R = np.log(resistividade / resistividade[0])

# Ajuste linear para obter beta
beta, coef_linear = np.polyfit(ln_T, ln_R, 1)
beta_err = np.sqrt(np.diag(np.polyfit(ln_T, ln_R, 1, cov=True)))[0]

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(ln_T, ln_R, color='b', label='Dados experimentais', marker='o')
plt.plot(ln_T, beta * ln_T + coef_linear, color='r', label='Ajuste linear')
plt.title("Gráfico Log-Log: Resistividade vs Temperatura", fontsize=14, fontweight='bold')
plt.xlabel(r"$\ln(\text{Temperatura})$ ($\ln(K)$)", fontsize=12)
plt.ylabel(r"$\ln(\text{Resistividade normalizada})$", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig("grafico_loglog_resistividade_temperatura_normalizada.png", dpi=300)
plt.show()

print(f"Coeficiente angular (beta): {beta:.4f} ± {beta_err:.4f}")
print(f"Coeficiente linear: {coef_linear:.4f}")
