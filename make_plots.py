# make_plots.py
# Создание графиков для статьи (сохраняются как PNG)

from predictions import delta_f, tau_echo
import numpy as np
import matplotlib.pyplot as plt

# Настройка качества и размера
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 150
plt.rcParams['font.size'] = 11

print("\n" + "="*70)
print("Создание графиков...")
print("="*70 + "\n")

# ГРАФИК 1: Δf vs M (для k=2 и k=3)
print("График 1: Δf vs M (зависимость шага частот от массы)...")

M_range = np.linspace(10, 150, 200)
df_k2 = [delta_f(M, k=2) for M in M_range]
df_k3 = [delta_f(M, k=3) for M in M_range]

# Точки реальных событий
events_M = [62, 142, 26, 54, 45]
events_names = ['GW150914', 'GW190521', 'GW190814', 'GW170814', 'GW190412']

plt.figure(figsize=(11, 6))
plt.plot(M_range, df_k2, 'b-', linewidth=2.5, label='k=2 (битовая гипотеза)')
plt.plot(M_range, df_k3, 'r--', linewidth=2, label='k=3', alpha=0.7)

# Отметки событий
for i, M in enumerate(events_M):
    df = delta_f(M, k=2)
    plt.plot(M, df, 'ko', markersize=8)
    plt.text(M+3, df, events_names[i], fontsize=9, va='center')

plt.xlabel('Масса чёрной дыры M (M☉)', fontsize=13, fontweight='bold')
plt.ylabel('Шаг частот Δf (Гц)', fontsize=13, fontweight='bold')
plt.title('Предсказание: частотная гребёнка в ringdown', 
          fontsize=15, fontweight='bold')
plt.legend(fontsize=12, loc='upper right')
plt.grid(alpha=0.3, linestyle='--')
plt.xlim(5, 155)
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig('figure1_deltaf_vs_mass.png', bbox_inches='tight')
plt.close()

print("  ✓ Сохранён: figure1_deltaf_vs_mass.png")

# ГРАФИК 2: τ_echo vs ε (задержка эхо)
print("График 2: τ_echo vs ε (задержка эхо от отступа)...")

epsilon_range = np.logspace(-6, -2, 100)
tau_30 = [tau_echo(30, e)*1000 for e in epsilon_range]
tau_100 = [tau_echo(100, e)*1000 for e in epsilon_range]

plt.figure(figsize=(11, 6))
plt.semilogx(epsilon_range, tau_30, 'b-', linewidth=2.5, label='M = 30 M☉')
plt.semilogx(epsilon_range, tau_100, 'g-', linewidth=2.5, label='M = 100 M☉')

# Типичные диапазоны
plt.axvspan(1e-3, 1e-2, alpha=0.1, color='yellow', label='Реалистичный диапазон ε')

plt.xlabel('ε (относительный отступ от горизонта)', fontsize=13, fontweight='bold')
plt.ylabel('Задержка эхо τ (мс)', fontsize=13, fontweight='bold')
plt.title('Предсказание: эхо от квази-горизонта', 
          fontsize=15, fontweight='bold')
plt.legend(fontsize=12, loc='upper right')
plt.grid(alpha=0.3, which='both', linestyle='--')
plt.xlim(1e-6, 1e-2)
plt.tight_layout()
plt.savefig('figure2_tau_echo_vs_epsilon.png', bbox_inches='tight')
plt.close()

print("  ✓ Сохранён: figure2_tau_echo_vs_epsilon.png")

# ГРАФИК 3: Δf scaling (проверка 1/M)
print("График 3: Проверка масштабирования Δf ∝ 1/M...")

plt.figure(figsize=(10, 6))
plt.plot(1/M_range, df_k2, 'b-', linewidth=2.5)
plt.xlabel('1/M (M☉⁻¹)', fontsize=13, fontweight='bold')
plt.ylabel('Δf (Гц)', fontsize=13, fontweight='bold')
plt.title('Линейное масштабирование: Δf ∝ 1/M', 
          fontsize=15, fontweight='bold')
plt.grid(alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('figure3_scaling_check.png', bbox_inches='tight')
plt.close()

print("  ✓ Сохранён: figure3_scaling_check.png")

print("\n" + "="*70)
print("✓ Все графики готовы! (3 PNG-файла в папке)")
print("="*70 + "\n")