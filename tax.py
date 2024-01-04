import math


def revenue(tax):
    return 100 * (math.log(tax + 1) - (tax - 0.2) ** 2 + 0.04)


def revenue_derivative(tax):
    return 100 * (1 / (tax + 1) - 2 * (tax - 0.2))


current_rate = 0.7
step_size = 0.001
threshold = 0.0001
maximum_iterations = 100000
keep_going = True
iterations = 0

while keep_going:
    rate_change = step_size * revenue_derivative(current_rate)
    current_rate += rate_change

    if abs(rate_change) < threshold:
        keep_going = False

    if iterations >= maximum_iterations:
        keep_going = False

    iterations += 1
