Quick Start Guide
=================

This guide will get you up and running with the Napari Chromosome Analysis toolkit quickly.

Prerequisites
-------------

Before starting, ensure you have:

* Python 3.8+ installed
* All dependencies installed (see :doc:`installation`)
* Sample chromosome images in TIFF format
* Trained Cellpose model (if using custom segmentation)

Basic Usage
-----------

1. **Launch the application**::

    python main.py

2. **Load images**:
   
   * Click "Load Images" button
   * Select a folder containing your chromosome images
   * The software expects images with specific suffixes (e.g., DAPI, DNA-FISH, CENP-C)

3. **Configure channel identifiers**:
   
   * Set the appropriate file suffixes for each channel
   * DAPI: for chromosome segmentation
   * DNA-FISH: for spot detection (channel 1)
   * CENP-C: for centromere detection (channel 2)

4. **Segment chromosomes**:
   
   * Click "Segment (DAPI) Image" 
   * The software will use Cellpose to identify individual chromosomes
   * Adjust post-processing settings if needed

5. **Detect spots**:
   
   * Adjust threshold sliders for each channel
   * Click "Detect Channel 1 spots" for DNA-FISH
   * Click "Detect Channel 2 spots" for CENP-C
   * Review and manually correct detections if needed

6. **Find common regions**:
   
   * Click "Find Common" to identify overlapping regions
   * This step is crucial for accurate quantification

7. **Measure intensities**:
   
   * Click "Get Intensity at Spots Locations"
   * Export results as CSV files

Example Workflow
----------------

Here's a typical analysis workflow:

**Single Image Analysis**:

1. Load images → Configure channels → Segment → Detect spots → Find common → Measure intensities

**Batch Processing**:

1. Load images → Configure channels → Set thresholds → Click "Batch Processing"
2. The software will process all folders automatically
3. Results will be saved in each folder plus a combined CSV

Key Features
------------

**Interactive Controls**:

* Threshold sliders for spot detection
* Manual correction tools
* Line drawing for chromosome splitting/merging

**Visualization**:

* Multi-channel image display
* Overlay of detected spots
* Segmentation masks

**Export Options**:

* CSV files with intensity measurements
* PNG images with overlays
* Segmentation masks

**Batch Processing**:

* Process multiple image folders
* Consistent settings across all images
* Combined results table

Tips for Best Results
---------------------

* **Image Quality**: Use high-quality, well-contrasted images
* **Thresholds**: Adjust detection thresholds based on your imaging conditions
* **Manual Correction**: Review automated detections and correct manually if needed
* **Consistent Naming**: Use consistent file naming conventions for batch processing
* **GPU Usage**: Enable GPU acceleration for faster Cellpose segmentation

Next Steps
----------

* See :doc:`user_guide` for detailed feature descriptions
* Check :doc:`api` for programmatic usage
* Review example datasets and parameters

Common Issues
-------------

**No spots detected**: 
   Lower the detection threshold or check image quality

**Too many false positives**: 
   Increase the detection threshold or improve image preprocessing

**Segmentation errors**: 
   Check that DAPI images are properly focused and contrasted 