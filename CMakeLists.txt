cmake_minimum_required(VERSION 3.10)
project(ocp_tessellate_native)

set(CMAKE_CXX_STANDARD 17)

cmake_policy(SET CMP0148 NEW)
cmake_policy(SET CMP0094 NEW)

set(VERSION "7.7.2")

execute_process(COMMAND python -c "import site; print(site.getsitepackages()[0], end='')" OUTPUT_VARIABLE SITE)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-deprecated-declarations")

include_directories(OCCT/build/include/opencascade/)

if(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
    link_directories(${SITE}/vtkmodules/.dylibs)
    set(TKG3D "TKG3d") 
    set(TKTOPALGO "TKTopAlgo") 
    set(TKMESH "TKMesh")     
endif()

if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    set(CMAKE_CXX_COMPILER "$ENV{CONDA_PREFIX}/bin/x86_64-conda-linux-gnu-g++")
    
    add_compile_options("-flto=auto")

    link_directories(${SITE}/cadquery_ocp.libs)
    execute_process(COMMAND bash -c "readelf -d ${SITE}/OCP.cpython* > /tmp/readelf.output")
    execute_process(COMMAND bash -c "grep -o \"libTKG3d-\[0-9a-fA-F\]\\+\.so\" /tmp/readelf.output" OUTPUT_VARIABLE TKG3D OUTPUT_STRIP_TRAILING_WHITESPACE)
    execute_process(COMMAND bash -c "grep -o \"libTKTopAlgo-\[0-9a-fA-F\]\\+\.so\" /tmp/readelf.output" OUTPUT_VARIABLE TKTOPALGO OUTPUT_STRIP_TRAILING_WHITESPACE)
    execute_process(COMMAND bash -c "grep -o \"libTKMesh-\[0-9a-fA-F\]\\+\.so\" /tmp/readelf.output" OUTPUT_VARIABLE TKMESH OUTPUT_STRIP_TRAILING_WHITESPACE)
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
    target_link_libraries(ocp_tessellate_native PRIVATE pybind11::module -l${TKG3D}.${VERSION} -l${TKTOPALGO}.${VERSION} -l${TKMESH}.${VERSION})
endif()

if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    target_link_libraries(ocp_tessellate_native PRIVATE pybind11::module -l:${TKG3D}.${VERSION} -l:${TKTOPALGO}.${VERSION} -l:${TKMESH}.${VERSION})
endif()
