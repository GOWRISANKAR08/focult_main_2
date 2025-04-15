from setuptools import setup, find_packages

setup(
    name="user_module",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Django>=5.0"],
    python_requires=">=3.8",
)