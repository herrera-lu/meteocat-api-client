from setuptools import setup

setup(
    name="meteocat-api-client",
    version="0.1.0",
    description="Client que consumeix dades de l'API REST del Servei Meteorològic de Catalunya",
    url="https://github.com/herrera-lu/meteocat-api-client",
    author="Lluís Herrera",
    author_email="soluciona.cat@outlook.com",
    license="MIT",
    packages=[
        "meteocat_api_client",
        "meteocat_api_client.connexio",
        "meteocat_api_client.xarxes",
        "meteocat_api_client.xarxes.pronostic",
        "meteocat_api_client.xarxes.xema",
        "meteocat_api_client.helpers",
    ],
    package_data={
        "meteocat_api_client.connexio": ["*"],
        "meteocat_api_client.xarxes": ["*"],
        "meteocat_api_client.xarxes.pronostic": ["*"],
        "meteocat_api_client.xarxes.xema": ["*"],
        "meteocat_api_client.helpers": ["*"],
    },
    install_requires=[
        "wheel>=0.37.1",
        "requests>=2.27.1",
        "requests-cache>=0.9.3",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
