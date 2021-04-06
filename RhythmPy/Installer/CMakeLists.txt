cmake_minimum_required(VERSION 3.20)

# sets compiler
set(CMAKE_C_COMPILER "gcc")
set(CMAKE_CXX_COMPILER "g++")

# sets language standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# sets project name
project(RhythmPy_Installer)
add_executable(Installer src/main.cpp)