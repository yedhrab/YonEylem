# Yunus Emre Ak
# 1306150001
# Değiştirilmesi gereken alanlara "Değiştirilebilir" yazısı eklenmişti

import matplotlib.pyplot as plt
import numpy as np

X_MIN = 0
X_MAX = 5
MAX_POINTS = 1000  # Değiştirilebilir herhanbir bir sayı


def Z(point: tuple) -> float:  # Değiştirilebilir herhanbir bir sayı
    return point[0] + 2 * point[1]


def initialize_X():
    return np.linspace(X_MIN, X_MAX, MAX_POINTS)


def initialize_Y(X: np.ndarray) -> dict:
    Y = []
    # Değiştirilebilir label ve value alanına denklem yazılır
    # x1 + 3x2 <= 3
    Y.append({"type": "leq", "label": '$y_1\leq1-x/2$', "value": 1 - X / 3.0})

    # Değiştirilebilir label ve value alanına denklem yazılır
    # 2x1 + x2 <= 2
    Y.append({"type": "leq", "label": '$y_2\leq2-2x$', "value": 2 - 2 * X})

    # Değiştirilebilir label ve value alanına denklem yazılır
    # 3x1 + x2 <= 3
    Y.append({"type": "leq", "label": '$y_3\leq-3x$', "value": 3 - 3 * X})

    return Y


def generate_lines(Y: dict) -> tuple:
    Y_max, Y_min = np.full_like(X, np.Inf), np.full_like(X, 0)
    points = set()
    for line_info in Y:
        plt.plot(X, line_info['value'], label=line_info['label'])

        if line_info['type'] == "leq":
            Y_max = np.minimum(Y_max, line_info['value'])
        elif line_info['type'] == "geq":
            Y_min = np.maximum(Y_min, line_info['value'])

    return Y_max, Y_min


def generate_points(Y: dict, Y_min: np.ndarray, Y_max: np.ndarray) -> set:
    points = set()
    for line_info in Y:
        for i in range(MAX_POINTS):
            if round(Y_max[i], 2) == round(Y_min[i], 2):
                points.add((X[i], Y_max[i]))
                break

            value = line_info['value'][i]
            if value in (Y_max[i], Y_min[i]):
                points.add((X[i], value))
                break

    points.add((X[0], Y_max[0]))
    points.add((X[0], Y_min[0]))

    return points


def draw_lines(X: np.ndarray, Y_min: np.ndarray, Y_max: np.ndarray):
    # Koordinat Sınırları
    plt.xlim((0, X.max()))
    plt.ylim((0, Y_max.max() * 2))

    # Etiketler
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')

    # Kesişim alanını çizdirme
    plt.fill_between(X, Y_min, Y_max, color='grey', where=Y_max >= Y_min, alpha=0.5)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


def print_results(points: set):
    value = [Z(point) for point in points]

    print("Points: ", points)
    print("Max " + str(max(value)))
    print("Min: " + str(min(value)))


X = initialize_X()
Y = initialize_Y(X)
Y_max, Y_min = generate_lines(Y)
points = generate_points(Y, Y_min, Y_max)

draw_lines(X, Y_min, Y_max)
print_results(points)
