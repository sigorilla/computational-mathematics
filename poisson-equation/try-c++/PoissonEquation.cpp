#include "PoissonEquation.h"

PoissonEquation::PoissonEquation(double step) : step(step) {
    sizeX = (unsigned int) (lengthX / this->step);
    sizeY = (unsigned int) (lengthY / this->step);

    currU = new double *[sizeY];
    prevU = new double *[sizeY];
    for (int i = 0; i <= sizeY; ++i) {
        currU[i] = new double [sizeX];
        prevU[i] = new double [sizeX];
    }

    for (int i = 0; i <= sizeY; ++i) {
        for (int j = 0; j <= sizeX; ++j) {
            currU[i][j] = 0.0;
        }
    }
}

PoissonEquation::~PoissonEquation() {
    delete [] prevU;
    delete [] currU;
}

double PoissonEquation::getStep() {
    return step;
}

int PoissonEquation::run() {
    double maxNorm;
    unsigned int countIterations = 0;
    do {
        maxNorm = getMaxNorm();
        for (int i = 0; i <= sizeY; ++i) {
            for (int j = 0; j <= sizeX; ++j) {
                prevU[i][j] = currU[i][j];
            }
        }
        for (int i = 1; i < sizeY; ++i) {
            for (int j = 1; j < sizeX; ++j) {
                currU[i][j] = (prevU[i - 1][j] + prevU[i + 1][j] + prevU[i][j - 1] + prevU[i][j + 1] - step * step * f(i, j)) / 4;
            }
        }
        countIterations++;
    } while (fabs(maxNorm - getMaxNorm()) > step);

    return countIterations;
}

double PoissonEquation::getMaxNorm() {
    double _maxNorm = 0.0;
    for (int i = 0; i <= sizeY; ++i) {
        for (int j = 0; j <= sizeX; ++j) {
            _maxNorm += fabs(currU[i][j]) * fabs(currU[i][j]);
        }
    }
    return sqrt(_maxNorm);
}

double PoissonEquation::f(int i, int j) {
    double x = i * step;
    double y = j * step;
    return 2 * (x * x + y * y) - 2 * (x + y);
}

void PoissonEquation::printU() {
    for (int i = 0; i <= sizeY; ++i) {
        for (int j = 0; j <= sizeX; ++j) {
            std::cout << currU[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

void PoissonEquation::saveU() {
    std::ofstream file;
    file.open("data.txt");

    for (int i = 0; i <= sizeY; ++i) {
        for (int j = 0; j <= sizeX; ++j) {
            file << currU[i][j] << " ";
        }
        file << "\n";
    }

    file.close();

}