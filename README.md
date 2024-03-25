# Building ocp-addons

## Create an Python

```bash
mamba env create -f env.yml
mamba activate ocp-addons
```


## Clone the repository

```bash
git clone https://github.com/bernhard-42/ocp-tessellate-native.git
cd ocp-tessellate-native
```

## Clone and build OCCT

```bash
cd OCCT
git submodule update --init --recursive
mkdir -p build
cd build/
$CONDA_PREFIX/bin/cmake ..
# make -j 8  # <== change to number of CPU cores available
# ln -s mac64/clang/lib  # <= MacOS
# ln -s lin64/gcc/lib    # <= Linux
```

## Build opc-addons

```bash
cd ../..
mkdir -p build
cd build/

export SITE=$(python -c "import site; print(site.getsitepackages()[0])")
$CONDA_PREFIX/bin/cmake ..
make 
ls -l ocp_tessellate*
```

## Test library

```bash
cd ..
python test.py
```


