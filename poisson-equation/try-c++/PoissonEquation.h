#ifndef POISSON_POISSONEQUATION_H
#define POISSON_POISSONEQUATION_H

#include <iostream>
#include <math.h>
#include <fstream>
#include <vector>

class PoissonEquation {
public:
    PoissonEquation(double step);
    ~PoissonEquation();
    double getStep();
    void printU();
    void saveU();
    int run();
private:
    double **currU;
    double **prevU;
    unsigned int sizeX;
    unsigned int sizeY;
    double step = 0.1;
    double lengthX  = 1.0;
    double lengthY = 2.0;
    double getMaxNorm();
    double f(int i, int j);
};


#endif //POISSON_POISSONEQUATION_H
