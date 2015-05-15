from math import sqrt, fabs, ceil
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np


class PoissonEquation(object):

    def __init__(self, step=0.1):
        try:
            self.step = float(step)
        except Exception:
            self.step = 0.1
        self.eps = self.step
        self.count_iterations = 0
        self.length_x = 1
        self.length_y = self.length_x
        self.size_x = ceil(self.length_x / self.step)
        self.size_y = ceil(self.length_y / self.step)

        self.curr_u = [[0 for x in range(self.size_y)]
                       for x in range(self.size_x)]
        self.prev_u = self.curr_u.copy()

    def __f(self, i=0, j=0):
        x = i * self.step
        y = j * self.step
        return 2 * (x ** 2 + y ** 2) - 2 * (x + y)

    def __exact(self, i=0, j=0):
        x = i * self.step
        y = j * self.step
        return x * y * (1 - x) * (1 - y)

    @property
    def get_norm(self):
        _max_norm = 0.0
        for i in range(self.size_y):
            for j in range(self.size_x):
                tmp = fabs(self.curr_u[i][j] - self.__exact(i, j))
                _max_norm = tmp if (tmp > _max_norm) else _max_norm
        return _max_norm

    def run(self):
        self.count_iterations = 0

        while True:
            self.prev_u = self.curr_u.copy()

            for i in range(1, self.size_y - 1):
                for j in range(1, self.size_x - 1):
                    self.curr_u[i][j] = (self.prev_u[i - 1][j] +
                                         self.prev_u[i + 1][j] +
                                         self.prev_u[i][j - 1] +
                                         self.prev_u[i][j + 1] -
                                         self.step ** 2 * self.__f(i, j)
                                         ) / 4

            self.count_iterations += 1
            if not (self.get_norm > self.eps):
                break

        return self.count_iterations

    def print_u(self):
        print('\n'.join([' '.join(['%.4f' % item for item in row])
                         for row in self.curr_u]))

    def save_u(self, filename='data.txt'):
        file = open(filename, 'w+')
        for row in self.curr_u:
            file.write(' '.join(str(item) for item in row) + '\n')
        file.close()
        print('Data was written to file `%s`.' % filename)

    def plot_u(self):
        if self.step < 0.001:
            print(
                'Graph will not be built. There will be saved to `data.txt`.')
            self.save_u()
            return

        X = np.arange(0, self.length_x, self.step)
        Y = np.arange(0, self.length_y, self.step)
        X, Y = np.meshgrid(X, Y)
        Z = np.array(self.curr_u)

        levels = MaxNLocator(nbins=15).tick_values(Z.min(), Z.max())
        cmap = plt.get_cmap('PiYG')

        plt.figure(1)
        plt.contourf(X, Y, Z, levels=levels, cmap=cmap)
        plt.colorbar()
        # plt.title('Poisson Equation Solution (h = %.4f)' % self.step)
        plt.xlabel('X')
        plt.ylabel('Y')
        self.__plot_exact()
        print('Approximate graph was built.')

    def __plot_exact(self):
        if self.step < 0.001:
            return

        X = np.arange(0, self.length_x, self.step)
        Y = np.arange(0, self.length_y, self.step)
        X, Y = np.meshgrid(X, Y)
        exact = [[self.__exact(x, y) for y in range(self.size_y)]
                 for x in range(self.size_x)]
        Z = np.array(exact)

        levels = MaxNLocator(nbins=15).tick_values(Z.min(), Z.max())
        cmap = plt.get_cmap('PiYG')

        plt.figure(2)
        plt.contourf(X, Y, Z, levels=levels, cmap=cmap)
        plt.colorbar()
        # plt.title('Exact solution xy(1-x)(1-y)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
        print('Exact graph was built.')


def main():
    step = input('Please, choose step for this method (by default: 0.1): ')
    poissonEquation = PoissonEquation(step=step)

    print('Step:', poissonEquation.step)
    print('Count of iterations:', poissonEquation.run())
    print('Error:', poissonEquation.get_norm)

    # poissonEquation.print_u()
    # poissonEquation.save_u()
    poissonEquation.plot_u()


if __name__ == '__main__':
    main()
