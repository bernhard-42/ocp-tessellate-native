# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
import os, sys

__version__ = "1.0.0"
description="Natively tessellate OCCT objects for OCP"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

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
