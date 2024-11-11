import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
mu_B = 9.274009994e-24  # magneton de Bohr (J/T)
k_B = 1.380649e-23      # constante de Boltzmann (J/K)

# Definir a função de Brillouin para S = 5/2
def B_S(eta, S=5/2):
    coth = lambda x: 1 / np.tanh(x)
    term1 = (S + 1/2) * coth((S + 1/2) * eta)
    term2 = (1/2) * coth(eta / 2)
    return (1/S) * (term1 - term2)

# Função para calcular Sz em função de B e T
def Sz(B, T, g=2, S=5/2):
    # Calcular η
    eta = (g * mu_B * B) / (k_B * T)
    # Retornar ⟨Sz⟩
    return S * B_S(eta, S)

# Gerar valores de B (campo magnético) e diferentes temperaturas
B_vals = np.linspace(0, 20, 200)  # Campo de 0 a 20 Tesla
T_vals = [1, 5, 50, 100, 300]  # Diferentes temperaturas em Kelvin

# Plotar ⟨Sz⟩ para diferentes temperaturas, com valores positivos e negativos
plt.figure(figsize=(10, 6))
for T in T_vals:
    Sz_vals = Sz(B_vals, T)
    plt.plot(B_vals, Sz_vals, label=f'T = {T} K')  # Valores positivos de ⟨Sz⟩


# Configurações do gráfico
plt.title('⟨Sz⟩ vs B para diferentes Temperaturas (S = 5/2)')
plt.xlabel('Magnetic Field B (T)')
plt.ylabel('⟨Sz⟩')
plt.legend(title="Temperaturas (K)")
plt.grid(True)
plt.show()
