cmake_minimum_required(VERSION 3.17)

# sets project name and version
project(Updater VERSION 1.0.0 LANGUAGES CXX)

# sets compilers
set(CMAKE_C_COMPILER "gcc")
set(CMAKE_CXX_COMPILER "g++")

# sets language standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find includes in the build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# header files
include_directories(${PROJECT_SOURCE_DIR}/src/include)

# source files
file(GLOB_RECURSE SOURCES ${PROJECT_SOURCE_DIR}/src/*.cpp)

# adds sourcefiles
add_executable(Updater ${SOURCES})
