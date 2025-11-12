Getting Started
===============

Welcome to MetaChrome!

.. figure:: _static/images/slide_02_the_interface_img02.png
   :alt: MetaChrome Interface
   :align: center
   :width: 90%

   The MetaChrome toolkit interface

Overview
--------

MetaChrome is a comprehensive solution for analyzing metaphase chromosomes using advanced image processing techniques. Built on the powerful Napari platform, it combines automated segmentation with interactive visualization and manual correction tools.

What is MetaChrome?
-------------------

This toolkit provides researchers with:

* **Automated chromosome segmentation** using trained Cellpose models
* **Multi-channel fluorescence analysis** for DAPI, DNA-FISH, and CENP-C
* **Spot detection and quantification** with customizable thresholds
* **Interactive visualization** in the Napari viewer
* **Batch processing** for high-throughput analysis
* **Manual correction tools** for quality control

Key Features
------------

.. image:: _static/images/slide_06_slide_6_img06.jpg
   :alt: Chromosome segmentation example
   :align: right
   :width: 300px

**Automated Segmentation**

Uses trained Cellpose models to automatically identify and segment individual metaphase chromosomes from DAPI images with high accuracy.

**Multi-Channel Spot Detection**

Detects and localizes DNA-FISH and CENP-C spots with adjustable threshold controls for optimal sensitivity and specificity.

**Co-localization Analysis**

Identifies regions where multiple signals overlap, enabling precise quantification of signal co-localization between channels.

**Interactive Visualization**

Built on Napari, providing powerful multi-dimensional image viewing with layer controls, zoom, pan, and real-time visualization of analysis results.

**Manual Correction Tools**

Provides interactive tools for refining automated results:

* Merge incorrectly split chromosomes
* Remove unwanted regions
* Delete false-positive spots
* Save and reload corrections

**Batch Processing**

Process multiple image folders automatically with consistent parameters, generating individual and summary results files for high-throughput workflows.

Who Should Use This?
--------------------

This toolkit is designed for researchers working on:

* **Chromosome Structure Analysis**: Quantitative assessment of metaphase chromosome morphology
* **Centromere Studies**: CENP-C localization and intensity measurements
* **DNA-FISH Analysis**: Detection and quantification of specific DNA sequences
* **Signal Co-localization**: Spatial relationships between different fluorescent markers
* **High-Throughput Screening**: Automated analysis of large image datasets

Image Requirements
------------------

The software works with multi-channel fluorescence microscopy images:

**Required Channels:**

* **DAPI channel**: For chromosome segmentation (nuclear/chromosome staining)
* **DNA-FISH channel** (Channel 1): For detecting specific DNA sequences
* **CENP-C channel** (Channel 2): For detecting centromere proteins

**Supported Formats:**

* TIFF (recommended for microscopy data)
* PNG
* JPG

**Naming Convention:**

Images should contain identifiable strings in their filenames:

* Example: ``sample_001_w435.tif`` (DAPI), ``sample_001_w525.tif`` (DNA-FISH), ``sample_001_w679.tif`` (CENP-C)
* Or: ``cell1_dapi.tif``, ``cell1_dna_fish.tif``, ``cell1_cenpc.tif``

The identifiers can appear anywhere in the filename and are configurable in the interface.

Typical Workflow
----------------

.. figure:: _static/images/slide_08_after_clicking_detect_channel__img08.png
   :alt: Analysis workflow visualization
   :align: center
   :width: 75%

   Example of spot detection results in the analysis workflow

A typical analysis consists of:

1. **Configure** channel identifiers to match your image naming
2. **Load** multi-channel fluorescence microscopy images
3. **Segment** chromosomes using Cellpose-based detection
4. **Detect** DNA-FISH and CENP-C spots with threshold controls
5. **Analyze** co-localization by finding common regions
6. **Measure** signal intensities at spot locations
7. **Export** results as CSV files for further analysis

Use Cases
---------

**Single Image Analysis**

For detailed analysis of individual metaphase spreads with manual quality control and correction.

**Batch Processing**

For high-throughput analysis of large datasets with consistent parameters across all images.

**Interactive Exploration**

For exploratory analysis where parameters are optimized interactively before batch processing.

Output and Results
------------------

.. figure:: _static/images/slide_09_do_the_same_for_channel_2_and__img09.png
   :alt: Multi-channel analysis result
   :align: center
   :width: 80%

   Complete analysis showing detected spots in both channels

The toolkit generates:

* **Visual overlays** showing segmented chromosomes and detected spots
* **CSV data files** with coordinates and intensity measurements
* **Summary statistics** for batch processed datasets
* **Exportable images** for presentations and publications

Performance
-----------

**Processing Speed:**

* Single image: ~30-60 seconds (with GPU)
* Batch of 100 images: ~1-2 hours (with GPU)
* GPU acceleration highly recommended for Cellpose segmentation

**Accuracy:**

* Chromosome segmentation: Comparable to manual annotation
* Spot detection: Adjustable sensitivity via threshold controls
* Manual correction: Interactive refinement for maximum accuracy

Getting Help
------------

**Questions or Issues?**

* **Email**: sagarm2@nih.gov
* **Institution**: HITIF/LRBGE/CCR/NCI (National Cancer Institute/NIH)

**Next Steps**

Ready to get started?

1. :doc:`installation` - Install the software and dependencies
2. :doc:`tutorial` - Follow the quick start tutorial
3. :doc:`workflow` - Learn the complete analysis workflow

Citation
--------

If you use this toolkit in your research, please cite:

**Author:** Md Abdul Kader Sagar  
**Affiliation:** HITIF/LRBGE/CCR/NCI (National Cancer Institute/NIH)  
**Email:** sagarm2@nih.gov

License
-------

This project is developed at the National Cancer Institute/NIH.

