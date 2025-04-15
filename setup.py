from setuptools import setup

setup(
    name="user_module",  # Must match import name exactly
    version="0.1.0",
    packages=["user_module"],
    package_dir={"": "."},
    include_package_data=True,
    install_requires=["Django>=5.0"],
)