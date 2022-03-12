from setuptools import setup

setup(
    name="api-meteocat-py",
    version="0.1.0",
    description="Client que consumeix dades de l'API REST del Servei Meteorològic de Catalunya",
    url="https://github.com/herrera-lu/api-meteocat-py",
    author="Lluís Herrera",
    author_email="lluis.herrera@outlook.com",
    license="MIT",
    packages=["api_meteocat_py"],
    install_requires=[
        "requests>=2.27.1",
        "requests-cache>=0.9.3",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
