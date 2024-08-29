from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="claude_engineer",
    version="0.1.0",
    py_modules=[
        "claude_engineer",
    ],
    install_requires=required,
)
