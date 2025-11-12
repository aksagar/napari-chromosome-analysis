#!/usr/bin/env python
"""
Setup script for MetaChrome toolkit.

Author: Md Abdul Kader Sagar
Email: sagarm2@nih.gov
Institute: National Cancer Institute/NIH
"""

from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
try:
    long_description = (this_directory / "README.md").read_text()
except FileNotFoundError:
    long_description = """
    MetaChrome - Metaphase Chromosome Analysis Toolkit
    
    A comprehensive toolkit for analyzing metaphase chromosomes using the Napari platform.
    Features chromosome segmentation, spot detection, and quantitative analysis.
    """

setup(
    name="metachrome",
    version="1.0.0",
    author="Md Abdul Kader Sagar",
    author_email="sagarm2@nih.gov",
    description="MetaChrome - A toolkit for analyzing metaphase chromosomes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aksagar/napari-chromosome-analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    python_requires=">=3.8",
    install_requires=[
        "napari>=0.4.0",
        "cellpose>=2.0.0",
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
        "scikit-image>=0.18.0",
        "matplotlib>=3.3.0",
        "magicgui>=0.5.0",
        "qtpy>=2.0.0",
        "superqt>=0.3.0",
        "pillow>=8.0.0",
    ],
    extras_require={
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.18.0",
        ],
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
            "isort>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "metachrome=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="metachrome, chromosome, analysis, segmentation, fluorescence, microscopy, napari",
    project_urls={
        "Documentation": "https://metachrome.readthedocs.io/",
        "Source": "https://github.com/aksagar/napari-chromosome-analysis",
        "Tracker": "https://github.com/aksagar/napari-chromosome-analysis/issues",
    },
) 