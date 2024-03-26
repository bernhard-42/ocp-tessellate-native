cmake_minimum_required(VERSION 3.10)
project(ocp_tessellate_native)

set(CMAKE_CXX_STANDARD 17)

cmake_policy(SET CMP0148 NEW)
cmake_policy(SET CMP0094 NEW)

execute_process(COMMAND python -c "import site; print(site.getsitepackages()[0], end='')" OUTPUT_VARIABLE SITE)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-deprecated-declarations")

include_directories(OCCT/build/include/opencascade/)

if(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
    link_directories(${SITE}/vtkmodules/.dylibs)
endif()

if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    link_directories(${SITE}/cadquery_ocp.libs)
endif()

# Find Python
set(Python_EXECUTABLE $ENV{CONDA_PREFIX}/bin/python3)
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Find pybind11 package
set(pybind11_DIR ${SITE}/pybind11/share/cmake/pybind11)
find_package(pybind11 REQUIRED)

# Add the pybind11 module
pybind11_add_module(ocp_tessellate_native src/tessellate.cpp)

# Link against the Python libraries

if(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
    target_link_libraries(ocp_tessellate_native PRIVATE pybind11::module  -lTKG3d.7.7.2 -lTKTopAlgo.7.7.2 -lTKMesh.7.7.2)
endif()

if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    target_link_libraries(ocp_tessellate_native PRIVATE pybind11::module   -l:libTKG3d-1cd4a50d.so.7.7.2 -l:libTKTopAlgo-ab298754.so.7.7.2 -l:libTKMesh-83dc7137.so.7.7.2)
endif()