cmake_minimum_required(VERSION 3.17)
project(part1_main)

set(CMAKE_CXX_STANDARD 14)

add_executable(part1_main main.cpp)
add_executable(part1_auxiliary auxiliary.cpp)

add_dependencies(part1_main part1_auxiliary)