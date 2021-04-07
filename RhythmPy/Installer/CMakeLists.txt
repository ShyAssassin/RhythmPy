cmake_minimum_required(VERSION 3.20)

# sets project name and version
project(RhythmPy_Installer VERSION 1.0.0 LANGUAGES CXX)

# sets compiler
set(CMAKE_C_COMPILER "gcc")
set(CMAKE_CXX_COMPILER "g++")

# sets language standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find includes in the build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# sets path for qt5
set(CMAKE_PREFIX_PATH "C:/Qt/6.1.0/mingw81_64")

# found this on the qt5 docs
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# find needed libraries
find_package(Qt6 COMPONENTS Widgets REQUIRED)

# adds "main" sourcefiles
add_executable(Installer src/main.cpp)
target_link_libraries(Installer PRIVATE Qt6::Widgets)
