from pathlib import Path

from setuptools import setup

consts = {}
#exec((Path("openhardwaremonitor") / "const.py").read_text(encoding="utf-8"), consts)  # noqa: S102

setup(
    name="pyOpenHardwareMonitor",
    packages=["openhardwaremonitor"],
    install_requires=["aiohttp>=3.0.6"],
    #package_data={"openhardwaremonitor": ["py.typed"]},
    version=consts["__version__"],
    description="A python3 library to communicate with an OpenHardwareMonitor remote server",
    python_requires=">=3.11.0",
    author="Peter Åslund",
    author_email="peter@peteraslund.me",
    url="https://github.com/lazytarget/pyOpenHardwareMonitor",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ],
)