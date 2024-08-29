from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="claude-engineer",
    version="0.1.0",
    py_modules=["main", "ollama_eng"],
    install_requires=required,
)
