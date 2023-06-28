from setuptools import setup, find_packages

setup(
    name="BaseBotService",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "pytest-cov",
        "behave",
        "requests",
        "selenium",
        "pandas",
        "python-docx",
        "openpyxl",
        "loguru",
        "PyYAML"
    ],
    author="Tu Nombre",
    author_email="tu.email@dominio.com",
    description="Descripción corta del proyecto",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/EnriqueERamirez/BaseBotService.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
