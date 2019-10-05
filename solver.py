import matplotlib.pyplot as plt
import numpy as np

# Denklemler (y* = x2)

# x > 0 (0 10 arası 1000 örnek)
x = np.linspace(0, 10, 1000)

y = []

# x1 + 3x2 <= 3
y.append({"type": "leq", "label": '$y_1\leq1-x/2$', "value": 1 - x / 3.0})

# 2x1 + x2 <= 2
y.append({"type": "leq", "label": '$y_2\leq2-2x$', "value": 2 - 2 * x})

# 3x1 + x2 <= 3
y.append({"type": "leq", "label": '$y_3\leq-3x$', "value": 3 - 3 * x})

# Doğruları oluşturma
y_min, y_max = np.inf, 0
for line_info in y:
    plt.plot(x, line_info['value'], label=line_info['label'])

    if line_info['type'] == "leq":
        y_min = np.minimum(y_min, line_info['value'])
    elif line_info['type'] == "geq":
        y_max = np.maximum(y_max, line_info['value'])

# Koordinat ekseni ayarları

# Koordinat Sınırları
plt.xlim((0, 5))
plt.ylim((0, 5))

# Etiketler
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# Fill feasible region
plt.fill_between(x, y_min, y_max, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
