Napari Chromosome Analysis
===========================

.. figure:: _static/images/slide_02_the_interface_img02.png
   :alt: Napari Chromosome Analysis Interface
   :align: center
   :width: 90%

   The Napari Chromosome Analysis toolkit

An automatic deep learning toolkit for metaphase chromosome analysis, written in Python using Napari and Cellpose. It enables researchers to analyze multi-channel fluorescence microscopy images for chromosome segmentation, spot detection, and intensity quantification.

.. image:: _static/images/slide_06_slide_6_img06.jpg
   :alt: Chromosome segmentation example
   :align: right
   :width: 300px

**Key Features:**

* **Automated Segmentation** - Cellpose-based chromosome detection
* **Multi-Channel Analysis** - DAPI, DNA-FISH, and CENP-C support
* **Spot Detection** - Adjustable threshold-based detection
* **Interactive Visualization** - Built on Napari platform
* **Batch Processing** - High-throughput analysis
* **Manual Corrections** - Interactive refinement tools

This toolkit integrates tools for detecting centromeres and measuring CENP-A levels within metaphase chromosome regions, enhancing the accuracy of chromosome analysis for researchers at the National Cancer Institute/NIH and beyond.

Tutorial
--------

Start here if you're new to the toolkit. These guides will get you up and running quickly.

.. toctree::
   :maxdepth: 1
   
   getting_started
   installation
   tutorial

**Getting Started**
   Overview of the toolkit, key features, and typical workflows.

**Installation**
   Step-by-step installation instructions and requirements.

**Tutorial: Your First Analysis**
   Hands-on tutorial walking through your first complete analysis from start to finish.

User Guide
----------

Detailed how-to guides for all features and workflows.

.. toctree::
   :maxdepth: 2
   
   workflow
   batch_processing
   manual_corrections
   advanced_features
   troubleshooting

**Basic Workflow**
   Complete guide to single-image analysis with all parameters explained.

**Batch Processing**
   Process multiple image folders automatically with consistent settings.

**Manual Corrections**
   Interactive tools for merging chromosomes, removing regions, and deleting spots.

**Advanced Features**
   Parameter optimization, Python scripting, and performance tuning.

**Troubleshooting**
   Solutions to common problems, error messages, and debugging tips.

API Reference
-------------

API documentation for programmatic usage.

.. toctree::
   :maxdepth: 2
   
   api
   modules

**API Reference**
   Complete API documentation for all classes and functions.

**Module Reference**
   Detailed module documentation and code examples.

Quick Links
-----------

.. list-table::
   :widths: 40 60
   :class: borderless

   * - **I want to...**
     - **Go to...**
   * - Get started quickly
     - :doc:`tutorial`
   * - Understand the workflow
     - :doc:`workflow`
   * - Process many images
     - :doc:`batch_processing`
   * - Fix detection errors
     - :doc:`manual_corrections`
   * - Optimize parameters
     - :doc:`advanced_features`
   * - Solve a problem
     - :doc:`troubleshooting`
   * - Use the API
     - :doc:`api`

Example Workflow
----------------

.. figure:: _static/images/slide_08_after_clicking_detect_channel__img08.png
   :alt: Spot detection visualization
   :align: center
   :width: 75%

   Example of spot detection results

A typical analysis workflow:

1. **Configure** channel identifiers → 2. **Load** images → 3. **Segment** chromosomes → 4. **Detect** spots → 5. **Find** common regions → 6. **Measure** intensities → 7. **Export** results

See the :doc:`tutorial` for a step-by-step walkthrough.

Use Cases
---------

This toolkit is designed for researchers working on:

**Chromosome Structure Analysis**
   Quantitative assessment of metaphase chromosome morphology and organization.

**Centromere Studies**
   CENP-C localization, intensity measurements, and centromere protein analysis.

**DNA-FISH Analysis**
   Detection and quantification of specific DNA sequences in metaphase chromosomes.

**Signal Co-localization**
   Spatial relationships between different fluorescent markers on chromosomes.

**High-Throughput Screening**
   Automated analysis of large image datasets from screening experiments.

Image Requirements
------------------

**Required Channels:**

* **DAPI** - Chromosome/nuclear staining for segmentation
* **DNA-FISH** (Channel 1) - Specific DNA sequence detection
* **CENP-C** (Channel 2) - Centromere protein detection

**Supported Formats:**

TIFF (recommended), PNG, JPG

**File Naming:**

Images should contain identifiable strings (e.g., ``sample_001_w435.tif``, ``sample_001_w525.tif``, ``sample_001_w679.tif``)

Example Results
---------------

.. figure:: _static/images/slide_09_do_the_same_for_channel_2_and__img09.png
   :alt: Multi-channel analysis result
   :align: center
   :width: 80%

   Complete analysis showing detected spots in both channels

**Outputs:**

* Visual overlays (segmented chromosomes + detected spots)
* CSV files with coordinates and intensity measurements
* Summary statistics for batch-processed datasets
* Exportable images for presentations and publications

Performance
-----------

**Processing Speed:**

* Single image: ~30-60 seconds (with GPU)
* Batch of 100 images: ~1-2 hours (with GPU)

**Accuracy:**

* Chromosome segmentation: High accuracy with trained Cellpose models
* Spot detection: Adjustable sensitivity via threshold controls
* Manual correction: Interactive refinement for maximum accuracy

Citation
--------

If you use this toolkit in your research, please cite:

**Author:** Md Abdul Kader Sagar  
**Email:** sagarm2@nih.gov  
**Affiliation:** HITIF/LRBGE/CCR/NCI (National Cancer Institute/NIH)

License
-------

This project is developed at the National Cancer Institute/NIH.

Contact and Support
-------------------

**Questions or Issues?**

* **Email:** sagarm2@nih.gov
* **Institution:** National Cancer Institute/NIH

**Community Resources:**

* Napari Documentation: https://napari.org/
* Cellpose Documentation: https://cellpose.readthedocs.io/

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
