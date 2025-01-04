"""setup.py"""

from setuptools import setup, find_packages

setup(
    name="pylibrary",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    description="print library to print the return, args or etc.",
    author="Abdullah",
    license="MIT",
    python_requires=">=3.7",
)
