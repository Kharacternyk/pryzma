from setuptools import setup

setup(
    name="pryzma",
    licence="GPLv3+",
    packages=["pryzma"],
    install_requires=["fire", "typeguard"],
    entry_points={"console_scripts": ["pryzma=pryzma.pryzma:main"]},
)
