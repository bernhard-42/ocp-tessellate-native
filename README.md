# Building ocp-addons

## Create a Python environment

```bash
mamba env create -f env.yml
mamba activate ocp-addons
```

### Linux

```bash
sudo apt-get update
sudo apt-get install freetype* libfreetype6-dev libgl1-mesa-glx
mamba install -c conda-forge gxx_linux-64=12*
```

## Clone the repository

```bash
git clone https://github.com/bernhard-42/ocp-tessellate-native.git
cd ocp-tessellate-native
```

## Build ocp-addons

```bash
python -m build -n
auditwheel repair --plat manylinux_2_35_x86_64 dist/ocp_tessellate_native-*.whl
```

## Test library

```bash
cd ..
python test.py
```



