import pkg_resources
from setuptools import setup
from pathlib import Path

with Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

consts: dict = {}
exec((Path("pyopenhardwaremonitor") / "const.py").read_text(encoding="utf-8"), consts)  # noqa: S102

setup(
    name="pyopenhardwaremonitor",
    packages=["pyopenhardwaremonitor"],
    install_requires=install_requires,
    version=consts["__version__"],
    description="A python3 library to communicate with an Open Hardware Monitor remote server",
    python_requires=">=3.11.0",
    author="Peter Åslund",
    author_email="peter@peteraslund.me",
    url="https://github.com/lazytarget/pyOpenHardwareMonitor",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
