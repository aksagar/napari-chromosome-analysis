Napari Chromosome Analysis
===========================

Welcome to the Napari Chromosome Analysis documentation!

This project provides tools for analyzing metaphase chromosomes using the Napari platform.
It facilitates the visualization and segmentation of chromosome images, enabling users 
to efficiently assess chromosome structures and perform quantitative analysis.

The code integrates tools for detecting centromeres and measuring CENP-A levels 
within metaphase chromosome regions, enhancing the accuracy of chromosome analysis.

Features
--------

* **Image Processing**: Load and process DAPI, DNA-FISH, and CENP-C images
* **Chromosome Segmentation**: Automatic chromosome segmentation using Cellpose
* **Spot Detection**: Detect DNA-FISH and CENP-C spots with customizable thresholds
* **Batch Processing**: Process multiple images in batch mode
* **Interactive Analysis**: Interactive tools for manual correction and analysis
* **Quantitative Analysis**: Measure intensities and calculate statistics

Author
------

**Md Abdul Kader Sagar**  
Email: sagarm2@nih.gov  
Institute: National Cancer Institute/NIH

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   installation
   quickstart
   user_guide
   api

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Getting Started
===============

To get started with this project, see the :doc:`installation` and :doc:`quickstart` guides.

For detailed information about the API, see the :doc:`api` reference.

License
=======

This project is developed at the National Cancer Institute/NIH.

Contact
=======

For questions or support, please contact:

* **Email**: sagarm2@nih.gov
* **Institute**: National Cancer Institute/NIH 