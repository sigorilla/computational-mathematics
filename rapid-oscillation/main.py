from math import *

# function f(x)
def f(x):
    return log(x)

# function derivative 2-th of f(x)
def df2(x):
    return 0 - 1 / pow(x, 2)

# function derivative 4-th of f(x)
def df4(x):
    return 0 - 6 / pow(x, 4)

# oscillating function
def F(x, w):
    return f(x) * sin(w * x)

# imaginary polynomial
def iD(index, p):
    if (index == 1):
        return pow(p, -3) * (p * p * cos(p) - p * sin(p))
        pass
    elif (index == 2):
        return 0
        pass
    elif (index == 3):
        return pow(p, -3) * (p * sin(p) - p * p * cos(p))
        pass
    else:
        return 0

# real polynomial
def rD(index, p):
    if (index == 1):
        return pow(p, -3) * (2 * p * cos(p) - sin(p) * (1 - p * p))
        pass
    elif (index == 2):
        return pow(p, -3) * (4 * sin(p) - 4 * p * cos(p))
        pass
    elif (index == 3):
        return pow(p, -3) * (2 * p * cos(p) + sin(p) * (p * p - 2))
        pass
    else:
        return 0

# Filon method
def filon(a, b, w):
    dots = [0, a, (a + b) / 2, b]

    arg = w * (b - a) / 2

    S1 = 0
    S2 = 0
    for i in range(1, 4):
        S1 += iD(i, arg) * f(dots[i])
        S2 += rD(i, arg) * f(dots[i])

    I = (b - a) / 2 * (cos(w * (b + a) / 2) * S1 + sin(w * (b + a) / 2) * S2)

    #R = fR(a, b)

    return I#(I, R)

# Trapeze method
def trapeze(a, b, w, N):
    tau = (b - a) / N
    I = 0

    for i in range(N):
        I += tau / 2 * (F(a + tau * i, w) + F( a + tau * (i + 1), w))

    #R = tR(a, b, N)

    return I#(I, R)

# max[a, b] |f(4)| * (b-a)^5 / 2880
# deviation of Filon method
def fR(a, b):
    return df4(b) * pow(b - a, 5) / 2880
    pass

# max[a,b] |f''| / 12 * tau^2 * (b-a)
# deviation of Trapeze method
def tR(a, b, N):
    tau = (b - a) / N
    return df2(b) * pow(tau, 2) * (b - a) / 12
    pass

if __name__ == '__main__':
    '''
    syms x;
    for i = [50:50:1000]:
        data(int16(i/50)) = double(int(x^5 * sin( i * x), 1, 5));
    end;
    '''
    # matlab = [0, -0.00772226343944976, 0.0142671735386616, 0.00719505867024575, -0.00449954722468904, -0.00602441424775869, 0.000600460621072647, 0.00456545519290168, 0.00148498107456028, -0.00290762654830805, -0.00244443903230872, 0.00131067350475818, 0.00261716113779507, 5.52072083920198e-05, -0.00221947055566741, -0.00104766593437450, 0.00146689415212271, 0.00158791136852555, -0.000582969780263734, -0.00168864270105518, -0.000249953111732823]
    a = 1
    b = 5
    N = 100
    Num = 21
    L = (b - a) / (Num - 1)
    print("Filon")
    for w in list(range(50, 1050, 50)):
        fil = 0
        for nu in list(range(0, (Num - 1))):
            a0 = a + L * nu
            b0 = a0 + L
            fil += filon(a0, b0, w)
        # st = "{0:.0f} & {1} & {2:.6f} & {3:.6f} & {4:.6f} \\\\\n" \
        #          "\\hline".format(
        #         (w / 50), w, filon(a, b, w), trapeze(a, b, w, N), matlab[int(w/50)])
        # print(st)
        # print("{0: .4f} \t {1: .4f}".format(filon(a0, b0, w), trapeze(a0, b0, w, N)))
        print("Omega: {0}".format(w))
        print("\t fl : {0: .6f}".format(fil))
        print("\t tr : {0: .6f}".format(trapeze(a, b, w, N)))

    # print("Error: \n \t Filon: {0} \n \t Trapeze: {1} \n".format(fR(a, b), tR(a, b, N)))