cmake_minimum_required(VERSION 3.2)
project(poisson)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp PoissonEquation.cpp PoissonEquation.h)
add_executable(poisson ${SOURCE_FILES})
