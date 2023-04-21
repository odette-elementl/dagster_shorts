from setuptools import find_packages, setup

setup(
    name="my_data_pipeline",
    packages=find_packages(exclude=["my_data_pipeline_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
