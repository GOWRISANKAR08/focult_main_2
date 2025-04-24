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


from setuptools import setup, find_packages

setup(
    name="main_app",
    version="0.1.0",
    packages=find_packages(include=['main_app', 'main_app.*']),
    include_package_data=True,
    install_requires=["Django>=5.0"],
    python_requires=">=3.8",
    zip_safe=False,
)

