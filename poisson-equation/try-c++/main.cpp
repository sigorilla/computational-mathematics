#include <iostream>
#include <typeinfo>
#include <limits>

#include "PoissonEquation.h"

int main(int argc, char **argv) {
//    std::cout << std::numeric_limits<std::ptrdiff_t>::max() << std::endl;
    std::cout << "Start!" << std::endl;

    PoissonEquation poissonEquation(0.01);
    poissonEquation.printU();

    int N = poissonEquation.run();
    double step = poissonEquation.getStep();

    std::cout << "Count of iterations: " << N << std::endl;
    std::cout << "Step: " << step << std::endl;

//    poissonEquation.printU();
    poissonEquation.saveU();

    std::cout << "End!" << std::endl;

    return 0;
}