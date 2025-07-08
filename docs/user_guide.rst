User Guide
==========

This comprehensive guide covers all features of the Napari Chromosome Analysis toolkit.

Overview
--------

The Napari Chromosome Analysis toolkit is designed for analyzing metaphase chromosomes using advanced image processing techniques. It provides tools for:

* Automated chromosome segmentation using Cellpose
* Multi-channel fluorescence image analysis
* Spot detection for DNA-FISH and CENP-C signals
* Quantitative intensity measurements
* Batch processing capabilities
* Interactive manual correction tools

Getting Started
---------------

Image Requirements
~~~~~~~~~~~~~~~~~~

The software works with multi-channel fluorescence microscopy images:

* **DAPI channel**: For chromosome segmentation
* **DNA-FISH channel**: For detecting specific DNA sequences
* **CENP-C channel**: For detecting centromere proteins

Supported formats: TIFF, PNG, JPG

File Naming Convention
~~~~~~~~~~~~~~~~~~~~~~

Use consistent suffixes for automatic channel identification:

* ``*_DAPI.tif`` - DAPI channel
* ``*_DNA-FISH.tif`` - DNA-FISH channel  
* ``*_CENP-C.tif`` - CENP-C channel

Or customize the suffixes in the Channel Identifiers widget.

Main Interface
--------------

The main interface consists of several components:

**Napari Viewer**
   The central image display area with layer controls

**Control Panels**
   * Load Images widget
   * Channel Identifiers
   * Segmentation controls
   * Spot detection sliders
   * Batch processing tools

**Analysis Tools**
   * Threshold adjustment sliders
   * Manual correction tools
   * Line drawing for chromosome editing
   * Intensity measurement tools

Core Workflows
--------------

Single Image Analysis
~~~~~~~~~~~~~~~~~~~~~

1. **Load Images**
   
   * Click "Load Images" and select folder
   * Images are automatically loaded based on suffixes
   * Check that all channels are properly identified

2. **Configure Channels**
   
   * Adjust channel identifiers if needed
   * Set custom suffixes for your naming convention
   * Save settings for future use

3. **Segment Chromosomes**
   
   * Click "Segment (DAPI) Image"
   * Uses trained Cellpose model for chromosome detection
   * Post-processing options available:
     - Remove small objects
     - Remove edge objects
     - Fill holes
     - Smooth boundaries

4. **Detect Spots**
   
   * Adjust threshold sliders for each channel
   * Click detection buttons for Channel 1 and Channel 2
   * Review detected spots in the viewer
   * Use manual correction tools if needed

5. **Find Common Regions**
   
   * Click "Find Common" to identify overlapping areas
   * Only spots in common regions are used for analysis
   * This step filters out background noise

6. **Measure Intensities**
   
   * Click "Get Intensity at Spots Locations"
   * Measurements are taken at spot centroids
   * Results include intensity values for both channels

7. **Export Results**
   
   * Save spot coordinates as CSV
   * Export segmentation masks as PNG
   * Save intensity measurements

Batch Processing
~~~~~~~~~~~~~~~~

For processing multiple image folders:

1. **Setup**
   
   * Configure channel identifiers
   * Set optimal threshold values using test images
   * Choose whether to use current UI settings

2. **Execute**
   
   * Click "Batch Load" to select root folder
   * Click "Batch Processing" to start
   * Progress is displayed in the console

3. **Results**
   
   * Individual CSV files saved in each folder
   * Combined results file in root folder
   * Intermediate files for debugging

Advanced Features
-----------------

Manual Correction Tools
~~~~~~~~~~~~~~~~~~~~~~~

**Line Drawing**
   * Draw lines to split or merge chromosomes
   * Useful for correcting segmentation errors
   * Lines are applied to the segmentation mask

**Spot Deletion**
   * Remove false positive spots manually
   * Draw lines through unwanted spots
   * Spots intersecting the line are removed

**Chromosome Counting**
   * Visual counter for chromosome numbers
   * Helps track segmentation accuracy
   * Updates automatically with changes

Post-processing Options
~~~~~~~~~~~~~~~~~~~~~~~

**Remove Small Objects**
   Filters out noise and small artifacts

**Remove Edge Objects**
   Excludes chromosomes touching image borders

**Fill Holes**
   Fills gaps within chromosome regions

**Smooth Boundaries**
   Applies morphological smoothing

Parameters and Settings
-----------------------

Detection Thresholds
~~~~~~~~~~~~~~~~~~~~

**DNA-FISH Threshold**
   * Range: 0-100% (displayed as 0-1.0 internally)
   * Lower values = more sensitive detection
   * Higher values = more specific detection

**CENP-C Threshold**
   * Same range and behavior as DNA-FISH
   * Optimize based on signal-to-noise ratio

Segmentation Parameters
~~~~~~~~~~~~~~~~~~~~~~~

**Cellpose Settings**
   * Model: Custom trained model for chromosomes
   * Diameter: Automatically determined
   * Channels: [0,0] for grayscale input
   * GPU acceleration: Enabled by default

**Post-processing**
   * Configurable through checkboxes
   * Applied in sequence after segmentation
   * Can be adjusted per image if needed

Data Export
-----------

File Formats
~~~~~~~~~~~~

**CSV Files**
   * Spot coordinates (X, Y)
   * Intensity measurements
   * Metadata (folder names, parameters)

**PNG Images**
   * Segmentation overlays
   * Spot detection results
   * Publication-ready figures

**NumPy Arrays**
   * Raw segmentation masks
   * Intermediate processing results
   * For advanced analysis

Output Structure
~~~~~~~~~~~~~~~~

For each processed folder::

    folder_name/
    ├── folder_name_intensity.csv
    ├── segmentation_overlay.png
    ├── spots_channel1.csv
    ├── spots_channel2.csv
    └── intermediate_results/
        ├── segmentation.npy
        ├── spots_ch1.npy
        └── spots_ch2.npy

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Segmentation Problems**
   * Check DAPI image quality and contrast
   * Verify that chromosomes are well-separated
   * Adjust post-processing parameters

**Spot Detection Issues**
   * Optimize threshold values
   * Check for proper image focus
   * Review channel assignments

**Performance Issues**
   * Enable GPU acceleration for Cellpose
   * Reduce image size if memory limited
   * Process smaller batches

**File Loading Errors**
   * Verify file naming conventions
   * Check image formats (TIFF preferred)
   * Ensure all channels are present

Error Messages
~~~~~~~~~~~~~~

**"No images found"**
   Check folder structure and naming conventions

**"CUDA out of memory"**
   Reduce image size or use CPU mode

**"Model not found"**
   Verify Cellpose model path in code

Best Practices
--------------

Image Acquisition
~~~~~~~~~~~~~~~~~

* Use consistent imaging parameters
* Ensure proper focus across all channels
* Optimize exposure times for each channel
* Maintain consistent sample preparation

Data Organization
~~~~~~~~~~~~~~~~~

* Use clear folder structures
* Follow consistent naming conventions
* Keep raw and processed data separate
* Document analysis parameters

Quality Control
~~~~~~~~~~~~~~~

* Manually review a subset of results
* Check for systematic errors
* Validate thresholds on test images
* Compare with manual counts when possible

Performance Optimization
~~~~~~~~~~~~~~~~~~~~~~~~

* Use GPU acceleration when available
* Process similar images in batches
* Optimize threshold values beforehand
* Clean up intermediate files regularly 