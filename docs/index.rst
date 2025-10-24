Napari Chromosome Analysis
===========================

Welcome to the Napari Chromosome Analysis documentation!

.. figure:: _static/images/slide_02_the_interface_img02.png
   :alt: Napari Chromosome Analysis Interface
   :align: center
   :width: 90%

   The Napari Chromosome Analysis toolkit interface

This project provides tools for analyzing metaphase chromosomes using the Napari platform.
It facilitates the visualization and segmentation of chromosome images, enabling users 
to efficiently assess chromosome structures and perform quantitative analysis.

The code integrates tools for detecting centromeres and measuring CENP-A levels 
within metaphase chromosome regions, enhancing the accuracy of chromosome analysis.

Features
--------

.. image:: _static/images/slide_06_slide_6_img06.jpg
   :alt: Chromosome segmentation example
   :align: right
   :width: 300px

* **Image Processing**: Load and process DAPI, DNA-FISH, and CENP-C images
* **Chromosome Segmentation**: Automatic chromosome segmentation using Cellpose
* **Spot Detection**: Detect DNA-FISH and CENP-C spots with customizable thresholds
* **Batch Processing**: Process multiple images in batch mode
* **Interactive Analysis**: Interactive tools for manual correction and analysis
* **Quantitative Analysis**: Measure intensities and calculate statistics

Key Capabilities
----------------

**Automated Segmentation**

Uses trained Cellpose models to automatically identify and segment individual metaphase chromosomes from DAPI images.

**Multi-Channel Spot Detection**

Detects and localizes DNA-FISH and CENP-C spots with adjustable threshold controls for optimal sensitivity and specificity.

**Co-localization Analysis**

Identifies regions where multiple signals overlap, enabling precise quantification of signal co-localization.

**Manual Correction Tools**

Provides interactive tools for:

* Merging incorrectly split chromosomes
* Removing unwanted regions
* Deleting false-positive spots
* Refining automated results

**Batch Processing**

Process multiple image folders automatically with consistent parameters, generating individual and summary results files.

Author
------

**Md Abdul Kader Sagar**  

* Email: sagarm2@nih.gov  
* Affiliation: HITIF/LRBGE/CCR/NCI (National Cancer Institute/NIH)

Quick Links
-----------

.. list-table::
   :widths: 30 70
   :class: borderless

   * - :doc:`installation`
     - Installation instructions and requirements
   * - :doc:`quickstart`
     - Get started quickly with basic workflows
   * - :doc:`user_guide`
     - Comprehensive guide with screenshots and examples
   * - :doc:`api`
     - API reference and function documentation

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Documentation

   installation
   quickstart
   user_guide

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api
   modules

Getting Started
===============

To get started with this project:

1. **Install the software** - See the :doc:`installation` guide for detailed instructions
2. **Try the quick start** - Follow the :doc:`quickstart` tutorial for a rapid introduction
3. **Read the user guide** - Explore the comprehensive :doc:`user_guide` with screenshots
4. **Check the API docs** - Review the :doc:`api` reference for programmatic usage

Typical Workflow
----------------

.. figure:: _static/images/slide_08_after_clicking_detect_channel__img08.png
   :alt: Spot detection visualization
   :align: center
   :width: 75%

   Example of spot detection results

A typical analysis workflow consists of:

1. **Configure** channel identifiers to match your image naming convention
2. **Load** multi-channel fluorescence microscopy images
3. **Segment** chromosomes using automated Cellpose-based detection
4. **Detect** DNA-FISH and CENP-C spots with threshold controls
5. **Analyze** co-localization by finding common regions
6. **Measure** signal intensities at spot locations
7. **Export** results as CSV files for further analysis

For Multiple Images
~~~~~~~~~~~~~~~~~~~

Use the batch processing feature to:

* Process entire folders of images automatically
* Apply consistent parameters across all samples
* Generate combined summary reports
* Save time on large datasets

Use Cases
---------

This toolkit is designed for researchers working on:

* **Chromosome Structure Analysis**: Quantitative assessment of metaphase chromosome morphology
* **Centromere Studies**: CENP-C localization and intensity measurements
* **DNA-FISH Analysis**: Detection and quantification of specific DNA sequences
* **Signal Co-localization**: Spatial relationship between different fluorescent markers
* **High-Throughput Screening**: Batch processing of large image datasets

Image Requirements
------------------

The software works with multi-channel fluorescence microscopy images:

* **DAPI channel**: For chromosome segmentation
* **DNA-FISH channel**: For detecting specific DNA sequences  
* **CENP-C channel**: For detecting centromere proteins

**Supported formats**: TIFF (recommended), PNG, JPG

Example Results
---------------

.. figure:: _static/images/slide_09_do_the_same_for_channel_2_and__img09.png
   :alt: Multi-channel analysis result
   :align: center
   :width: 80%

   Complete analysis showing chromosomes and detected spots in both channels

The analysis generates:

* **Visual overlays** showing segmented chromosomes and detected spots
* **CSV data files** with coordinates and intensity measurements
* **Summary statistics** for batch processed datasets
* **Exportable images** for presentations and publications

Community and Support
---------------------

**Questions or Issues?**

For questions, bug reports, or feature requests:

* **Email**: sagarm2@nih.gov
* **Institution**: National Cancer Institute/NIH

**Contributing**

This project is developed at the National Cancer Institute. Contributions and feedback are welcome.

License
=======

This project is developed at the National Cancer Institute/NIH.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
