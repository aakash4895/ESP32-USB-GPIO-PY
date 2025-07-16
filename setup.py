from setuptools import setup, find_packages

setup(
    name="ESP32 USB FPIO",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pyserial"],
    author="Aakash Singh",
    description="A Python library for controlling ESP32 GPIO pins via USB serial communication. This library provides a simple and intuitive interface to interact with ESP32 GPIO pins remotely through USB connection.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
