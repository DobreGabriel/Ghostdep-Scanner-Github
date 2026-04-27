from setuptools import setup, find_packages

setup(
    name="ghostdep",
    version="0.3",
    packages=find_packages(),
    install_requires=["typer", "requests"],
    entry_points={
        "console_scripts": [
            "ghostdep=cli:app"
        ]
    },
)
