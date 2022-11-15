cmake_minimum_required (VERSION 3.2.5)

project(Program_HelloWorld CXX)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_COMPLIER "C:/MinGW/bin/g++")
set(CMAKE_C_COMPLIER "C:/MinGW/bin/gcc")

add_library("HelloWorld" HelloWorld.cpp)
