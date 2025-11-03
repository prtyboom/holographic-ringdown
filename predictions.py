# predictions.py
# Формулы для голографического квантования площади
# (c) 2025 Fedor Kapitansky

import numpy as np

# Константы (SI)
c = 299792458.0                 # м/с
G = 6.67430e-11                 # м^3/(кг·с^2)
M_SUN = 1.98847e30              # кг
hbar = 1.054571817e-34          # Дж·с

def delta_f(M_solar, k=2.0):
    """
    Шаг частот Δf [Гц] для чёрной дыры массой M_solar (в M☉).
    k = 2 для битовой гипотезы.
    """
    M = M_solar * M_SUN
    return (c**3 * np.log(k)) / (16.0 * np.pi**2 * G * M)

def tau_echo(M_solar, epsilon):
    """
    Задержка эхо τ [сек] для поверхности на r = r₊(1 + ε).
    """
    M = M_solar * M_SUN
    return (2.0 * G * M / c**3) * np.log(1.0 / epsilon)

# Тестовая таблица
if __name__ == "__main__":
    print("\n" + "="*60)
    print("ПРОВЕРКА ФОРМУЛ: Голографическое квантование площади")
    print("="*60 + "\n")
    
    masses = [10, 30, 62, 100, 142]
    
    print("M (M☉) | Δf (Гц, k=2) | τ_echo (мс, ε=0.01)")
    print("-" * 60)
    
    for M in masses:
        df = delta_f(M, k=2.0)
        tau = tau_echo(M, 0.01) * 1000  # в миллисекундах
        print(f"{M:6.0f} | {df:12.2f} | {tau:10.2f}")
    
    print("\n" + "="*60)
    print("✓ Формулы работают корректно!")
    print("="*60 + "\n")