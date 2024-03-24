# initialize the OCCT git submodule
git submodule init
git submodule update
# and build it
cd OCCT/
mkdir -p build
cd build
cmake ..
make -j 8
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    ln -s lin64/gcc/lib/ lib
elif [[ "$OSTYPE" == "darwin"* ]]; then
    ln -s mac64/clang/lib/ lib
fi
cd ../../

# create a new conda environment
mamba create -y -n ocp310 python=3.10 pybind11
mamba activate ocp310
pip install cmake ocp-tessellate cadquery-ocp

# and build ocp-tessellate-native
mkdir build
cd build
cmake ..
make
cd ..

mamba deactivate 