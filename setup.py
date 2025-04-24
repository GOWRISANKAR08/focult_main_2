# from setuptools import setup

# setup(
#     name="user_module",  
#     version="0.1.0",
#     packages=["user_module"],
#     package_dir={"": "."},
#     include_package_data=True,
#     install_requires=["Django>=5.0"],

# )

# from setuptools import setup, find_packages

# setup(
#     name="django_modules",
#     version="0.1.0",
#     packages=find_packages(),  # Auto-finds all modules
#     package_dir={"": "."},
#     include_package_data=True,
#     install_requires=["Django>=5.0"],
#     python_requires=">=3.8",
#     zip_safe=False,
# )


# from setuptools import setup, find_packages

# from setuptools import setup, find_packages

# setup(
#     name="main_app",
#     version="0.1.0",
#     packages=['main_app', 'main_app.user_module', 'main_app.order_module'],  # Explicit list
#     package_dir={'main_app': 'main_app'},  # Maps package name to directory
#     include_package_data=True,
#     install_requires=["Django>=5.0"],
#     python_requires=">=3.8",
#     zip_safe=False,
# )


from setuptools import setup, find_packages

setup(
    name="main_app",
    version="0.1.0",
    packages=find_packages(),  # Will find main_app and subpackages
    package_dir={'': '.'},     # Look in current directory
    include_package_data=True,
    install_requires=["Django>=5.0"],
    python_requires=">=3.8",
    zip_safe=False,
)