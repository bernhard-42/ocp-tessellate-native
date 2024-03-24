cmake_minimum_required(VERSION 3.10)
project(ocp_tessellate_native)

set(CMAKE_CXX_STANDARD 17)

cmake_policy(SET CMP0148 NEW)
cmake_policy(SET CMP0094 NEW)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-deprecated-declarations")

include_directories(OCCT/build/include/opencascade/)
link_directories(OCCT/build/lib/)

# Find Python
set(Python_EXECUTABLE $ENV{CONDA_PREFIX}/bin/python3)
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Find pybind11 package - be sure SITE is set to CONDA_PREFIX/.../site-packages
set(pybind11_DIR $ENV{SITE}/pybind11/share/cmake/pybind11)
find_package(pybind11 REQUIRED)

# Add the pybind11 module
pybind11_add_module(ocp_tessellate_native src/tessellate.cpp)

# Link against the Python libraries
target_link_libraries(ocp_tessellate_native PRIVATE pybind11::module -lTKG3d -lTKTopAlgo -lTKMesh)
