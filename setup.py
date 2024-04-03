# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
import os, sys
import os.path


__version__ = "0.1.0"
description="Addon packages for OCP"

os.environ["CXX"] = "x86_64-conda-linux-gnu-g++"

ext_modules = [
    Pybind11Extension(
        "ocp_tessellate_native",
        ["src/tessellate.cpp"],
        define_macros=[
            ("VERSION_INFO", __version__),
            ("DESCRIPTION", description),
        ],
        include_dirs = [os.path.join(sys.prefix, "include/opencascade")],
        libraries = ["TKG3d", "TKTopAlgo", "TKMesh"],
        cxx_std = 17
    ),
]

setup(
    name="ocp_tessellate_native",
    version=__version__,
    author="Bernhard Walter",
    author_email="",
    url="https://github.com/bernhard-42/ocp-tessellator-native",
    description=description,
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.9",
)
