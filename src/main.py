x0 = 1.0
xk = 2.0
y0 = 4.718282
z0 = 1.0
h = 0.1


def f(x, y, z):
    return (y - z * (x + 1)) / (x ** 2)


def value(x):
    return x + 1 + x * 2.718282 ** (1 / x)


def print_value(x0, xk, h):
    x = x0
    result = [(x0, value(x0))]
    while x < xk:
        x = round(x + h, 1)
        result.append((x, value(x)))
    return result


def euler(x0, y0, z0, xk, h):
    x = x0
    y = y0
    z = z0
    result = [(x, y)]
    while x < xk:
        yn = y + h * z
        zn = z + h * f(x, y, z)
        y = yn
        z = zn
        x = round(x + h, 1)
        result.append((x, y))
    return result


def euler_cauchy(x0, y0, z0, xk, h):
    x = x0
    y = y0
    z = z0
    result = [(x, y)]
    while x < xk:
        zn = z + h * f(x, y, z)
        yn = y + (h / 2) * (z + zn)
        y = yn
        z = zn
        x = round(x + h, 1)
        result.append((x, y))
    return result


def runge_kutta(x0, y0, z0, xk, h):
    x = x0
    y = y0
    z = z0
    result = [(x, y)]
    while x < xk:
        k1 = z
        l1 = f(x, y, z)
        k2 = z + h * l1
        l2 = f(x + h, y + h * k1, z + h * l1)
        yn = y + (h / 2) * (k1 + k2)
        zn = z + (h / 2) * (l1 + l2)
        y = yn
        z = zn
        x = round(x + h, 1)
        result.append((x, y))
    return result


def calculate_difference(euler_result, value_result):
    differences = []
    for i in range(len(euler_result)):
        x_euler, y_euler = euler_result[i]
        x_value, y_value = value_result[i]
        diff = abs(y_value - y_euler)
        differences.append((x_euler, diff))
    return differences


print("Метод Ейлера\n")
euler_result = euler(x0, y0, z0, xk, h)
value_result = print_value(x0, xk, h)
differences = calculate_difference(euler_result, value_result)

for i in range(len(euler_result)):
    x_euler, y_euler = euler_result[i]
    x_value, y_value = value_result[i]
    x_diff, y_diff = differences[i]
    print("x={:.1f}\ty={:.7f}\t\tТочне значення={:.7f}\tПохибка={:.7f}".format(x_euler, y_euler, y_value, y_diff))


print("\nМетод Ейлера-Коші\n")
euler_cauchy_result = euler_cauchy(x0, y0, z0, xk, h)
differences = calculate_difference(euler_cauchy_result, value_result)

for i in range(len(euler_cauchy_result)):
    x_euler_cauchy, y_euler_cauchy = euler_cauchy_result[i]
    x_value, y_value = value_result[i]
    x_diff, y_diff = differences[i]
    print("x={:.1f}\ty={:.7f}\t\tТочне значення={:.7f}\tПохибка={:.7f}".format(x_euler_cauchy, y_euler_cauchy, y_value, y_diff))


print("\nМетод Рунге-Кутта\n")
runge_kutta_result = runge_kutta(x0, y0, z0, xk, h)
differences = calculate_difference(runge_kutta_result, value_result)

for i in range(len(runge_kutta_result)):
    x_runge_kutta, y_runge_kutta = runge_kutta_result[i]
    x_value, y_value = value_result[i]
    x_diff, y_diff = differences[i]
    print("x={:.1f}\ty={:.7f}\t\tТочне значення={:.7f}\tПохибка={:.7f}".format(x_runge_kutta, y_runge_kutta, y_value, y_diff))
