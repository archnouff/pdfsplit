from pathlib import Path

from setuptools import setup, find_packages

package_name = "pdfsplit"

# Get version
version_dict = {}
with open(Path(package_name) / 'version.py', 'r') as ver_file:
    exec(ver_file.read(), version_dict)
version = version_dict["__version__"]

# Iterate cli directory for command lines
command_names = sorted([
    f.stem
    for f in (Path(__file__).parent / package_name / 'cli').glob('*.py')
    if f.stem != '__init__'
])

setup(
    version=version,
    name=package_name,
    author="Pierre Arquier",
    author_email="arquier.pierre@gmail.com",
    description="Tool to split PDF files",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            f'{name.replace("_", "-")}={package_name}.cli.{name}:main' for name in command_names
        ]
    },
    install_requires=[
        "click~=8.1.3",
        "pikepdf~=7.2.0",
        "PyYAML~=6.0",
    ],
    extras_require={
        "test": [
            "pytest~=6.2.4",
        ],
    },
    package_data={
        '': [
        ],
    },
    include_package_data=True,
)
