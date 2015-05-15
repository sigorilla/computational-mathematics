# 4.4
from math import pow, copysign

decisions = list()
extrapolation = list()
epsy = 1e-6
epsx = 1e-10

sign = lambda x: copysign(1, x)

def func(x):
    return 1e-3 * pow(x, 5) + pow(x, 2) - 1

def func_diff(x):
    return 5e-3 * pow(x, 4) + 2 * x

def func_diff2(x):
    return 20e-3 * pow(x, 3) + 2

def func_diff3(x):
    return 60e-3 * pow(x, 2)

def func_diff4(x):
    return 120e-3 * x

def func_diff5(x):
    return 120e-3

def bisection(a, b):
    if func(a) == 0:
        decisions.append(a)
    if func(b) == 0:
        decisions.append(b)
    x_from = a
    x_to = b
    dx = x_to - x_from
    x = x_from + dx
    while abs(func(x)) > epsy and dx > epsx:
        dx /= 2
        x = x_from + dx
        if sign(func(x_from)) != sign(func(x)):
            x_to = x
        else:
            x_from = x
    if abs(func(x)) <= epsy:
        decisions.append(x)
    pass

# @param {zero} int(zero)
# if zero = 0 its standart newton method
# if zero = 1 its newtown method with f'(x0)
def newton(zero = 0):
    print("\n\nNewton's method",
          " with zero condition." if zero == 1 else ".")
    for i in list(range(len(decisions))):
        count = 0
        x = decisions[i]
        x_next = extrapolation[i]
        x_zero =  x_next
        while abs(x_next - x) > epsy:
            print("Debug:", x, x_next)
            x = x_next
            x_next = x_next - func(x_next) / func_diff(x_zero)
            count += 1
            x_zero = x_next if zero == 0 else x_zero

        print("Extrapolation: ",
              extrapolation[i],
              " \n\tby ",
              count,
              " iterations. \n\tx = ",
              x_next)
        x = x_next
        '''if func_diff(x) == 0.0:
            if func_diff2(x) == 0.0:
                if func_diff3(x) == 0.0:
                    if func_diff4(x) == 0.0:
                        print("\tOrder of convergence: ", 5)
                        # print(func_diff5(x))
                    else:
                        print("\tOrder of convergence: ", 4)
                        # print(func_diff4(x))
                else:
                    print("\tOrder of convergence: ", 3)
                    # print(func_diff3(x))
            else:
                print("\tOrder of convergence: ", 2)
                # print(func_diff2(x))
        else:
            print("\tOrder of convergence: ", 1)
            # print(func_diff(x))
'''
        # print(func(x))
    pass

step = 2
for i in list(range(-10, 10, step)):
    bisection(i, i + step)
    pass

print("Decisions: ", decisions)
extrapolation = [-10.0, -1.0, 1.0]
print("Interpolation: ", extrapolation)
newton()
newton(zero=1)
