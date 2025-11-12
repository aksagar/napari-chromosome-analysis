Troubleshooting
===============

Solutions to common problems and error messages.

Installation Issues
-------------------

Python Version Errors
~~~~~~~~~~~~~~~~~~~~~

**Error:** ``Python 3.8 or higher is required``

**Solution:**

```bash
# Check Python version
python --version

# Install Python 3.9+
# On Mac with Homebrew:
brew install python@3.9

# On Ubuntu/Debian:
sudo apt-get install python3.9
```

Dependency Installation Failures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:** ``Could not install napari``

**Solutions:**

1. **Use virtual environment:**

```bash
python -m venv napari-env
source napari-env/bin/activate  # Mac/Linux
# or
napari-env\Scripts\activate  # Windows

pip install napari cellpose scikit-image
```

2. **Update pip:**

```bash
pip install --upgrade pip
pip install napari
```

3. **Use conda instead:**

```bash
conda create -n napari-chr python=3.9
conda activate napari-chr
conda install -c conda-forge napari
```

CUDA/GPU Issues
~~~~~~~~~~~~~~~

**Error:** ``CUDA out of memory``

**Solutions:**

1. **Reduce image size:**

Resize images to smaller dimensions before processing.

2. **Use CPU mode:**

In the code, disable GPU:

```python
model = Cellpose(gpu=False)
```

3. **Close other GPU applications:**

Free up GPU memory by closing other programs.

4. **Process one image at a time:**

Avoid batch processing large images.

Qt/GUI Issues
~~~~~~~~~~~~~

**Error:** ``No module named 'PyQt5'``

**Solution:**

```bash
pip install PyQt5
# or
pip install PySide2
```

**Error:** ``Could not initialize Qt application``

**Solution on macOS:**

```bash
# Install via conda
conda install pyqt

# Or set backend
export QT_API=pyqt5
```

Image Loading Problems
----------------------

No Images Found
~~~~~~~~~~~~~~~

**Error:** ``No images found in folder``

**Diagnosis:**

* Channel identifiers don't match filenames
* Images are in subdirectories
* Wrong folder selected

**Solutions:**

1. **Check filenames:**

```bash
ls /path/to/images/
# Verify files contain your identifier strings
```

2. **Update identifiers:**

Match the actual strings in your filenames:

```
If files are: sample_DAPI.tif, sample_GFP.tif, sample_RFP.tif
Use identifiers: DAPI, GFP, RFP
```

3. **Check folder structure:**

Images should be in the folder you selected, not in subdirectories.

File Format Not Supported
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:** ``Cannot read file format``

**Supported Formats:**

* TIFF (.tif, .tiff) - **recommended**
* PNG (.png)
* JPEG (.jpg, .jpeg)

**Solution:**

Convert images to TIFF:

```python
from PIL import Image
img = Image.open('image.jpg')
img.save('image.tif')
```

Incorrect Number of Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Only 1 or 2 channels loaded

**Solutions:**

1. **Verify all files exist:**

```bash
ls -1 /path/to/images/*435*  # DAPI
ls -1 /path/to/images/*525*  # Channel 1
ls -1 /path/to/images/*679*  # Channel 2
```

2. **Check identifier case sensitivity:**

Use identifiers that match exactly (case-sensitive on Linux/Mac).

3. **Enable "Skip Segmentation":**

If DAPI is missing and not needed.

Segmentation Problems
---------------------

Segmentation Failed
~~~~~~~~~~~~~~~~~~~

**Error:** ``Segmentation could not complete``

**Causes & Solutions:**

**Poor Image Quality:**

* Low contrast
* Out of focus
* Overexposed

**Solution:** Adjust image acquisition settings or skip segmentation.

**Model File Missing:**

**Error:** ``Cellpose model not found``

**Solution:**

Verify model path in code or use default model:

```python
model = Cellpose(gpu=True, model_type='cyto')  # Use built-in model
```

Too Many/Few Chromosomes Detected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** 100+ chromosomes detected (should be ~46)

**Causes:**

* Threshold too low
* Debris in image
* Over-segmentation

**Solutions:**

1. **Adjust Cellpose parameters** (in code):

```python
model.eval(..., flow_threshold=0.6)  # Increase from default 0.4
```

2. **Use manual corrections:**

Remove extra objects with the Remove tool.

3. **Pre-process images:**

Clean up debris before analysis.

**Problem:** Very few chromosomes detected (<10)

**Causes:**

* Threshold too high
* Poor DAPI signal
* Chromosomes clumped together

**Solutions:**

1. **Lower threshold in code**
2. **Improve DAPI staining**
3. **Use manual merge tool** for clumped chromosomes

Segmentation is Very Slow
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Typical Times:**

* With GPU: 5-15 seconds
* Without GPU: 30-60 seconds

**If Slower:**

1. **Enable GPU:**

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

2. **Reduce image size:**

Resize to 1024x1024 or smaller.

3. **Check GPU is being used:**

Console should show: ``Using GPU for segmentation``

Spot Detection Issues
---------------------

No Spots Detected
~~~~~~~~~~~~~~~~~

**Problem:** Zero spots found in one or both channels

**Solutions:**

1. **Lower threshold:**

Move slider to 20-30 (more sensitive).

2. **Check image quality:**

Verify signal is present by looking at the raw image.

3. **Verify correct channel loaded:**

Check that the fluorescence channel is displayed.

4. **Increase sensitivity in code** (advanced):

Modify detection parameters for more sensitive detection.

Too Many False Positives
~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Hundreds of spots, many are noise

**Solutions:**

1. **Increase threshold:**

Move slider to 60-70 (more specific).

2. **Improve image quality:**

* Better background subtraction
* Reduce imaging noise
* Optimize exposure time

3. **Use manual deletion:**

Remove false positives with the spot deletion tool.

4. **Filter by size** (in code):

```python
# Only keep spots of certain size
spots = filter_by_size(spots, min_size=3, max_size=50)
```

Spots Don't Match Visual Inspection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Detected spots don't align with visible signals

**Causes:**

* Wrong channel being analyzed
* Coordinate system mismatch
* Detection on wrong image plane (z-stack)

**Solutions:**

1. **Verify channel order:**

Toggle layers to confirm which is which.

2. **Check z-plane:**

If using z-stacks, ensure analyzing the correct plane.

3. **Manual verification:**

Use spot deletion to remove incorrect detections.

Intensity Measurement Problems
-------------------------------

Negative or Zero Intensities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** CSV shows 0 or negative intensity values

**Causes:**

* Background subtraction too aggressive
* Spots outside image bounds
* Empty spot regions

**Solutions:**

1. **Check background subtraction:**

Disable or reduce background subtraction.

2. **Verify spot coordinates:**

Ensure spots are within image boundaries.

3. **Inspect raw data:**

Look at intensity values before processing.

Unrealistic Intensity Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Intensities seem too high or too low

**Checks:**

1. **Verify image bit-depth:**

```python
import tifffile
img = tifffile.imread('image.tif')
print(f"Data type: {img.dtype}")
print(f"Max value: {img.max()}")
```

2. **Check for saturation:**

High values may indicate saturated pixels.

3. **Normalize if needed:**

Convert to consistent scale across images.

Missing Intensity Data
~~~~~~~~~~~~~~~~~~~~~~

**Problem:** CSV file has no data or few rows

**Solutions:**

1. **Verify "Find Common" was run:**

Must run before intensity calculation.

2. **Check spot detection:**

Ensure spots were detected in both channels.

3. **Look for error messages:**

Console may show why measurement failed.

Batch Processing Problems
--------------------------

Batch Processing Stops Unexpectedly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Processing halts mid-batch

**Causes & Solutions:**

**Memory Exhaustion:**

* Reduce batch size
* Close other applications
* Add swap space

**File Permission Errors:**

```bash
# Check permissions
ls -la /path/to/images/

# Fix permissions
chmod -R 755 /path/to/images/
```

**Corrupted Image File:**

* Identify problematic file from last console message
* Remove or fix the file
* Resume batch processing

Some Folders Skipped
~~~~~~~~~~~~~~~~~~~~

**Problem:** Not all folders were processed

**Check:**

1. **Console output** for error messages
2. **Folder structure** - each folder should have all 3 channels
3. **File permissions** - ensure read/write access

**Solution:**

Process skipped folders individually to see specific errors.

Inconsistent Results Across Batch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Wide variation in spot counts or intensities

**Possible Causes:**

* Variable image quality
* Inconsistent imaging parameters
* Sample-to-sample biological variation

**Solutions:**

1. **Quality control:**

Identify outliers and inspect manually.

2. **Normalize parameters:**

Adjust thresholds per subset if needed.

3. **Document variability:**

May be real biological variation.

Performance Issues
------------------

Application is Slow or Unresponsive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**General Solutions:**

1. **Close other applications**
2. **Restart the application**
3. **Reduce image size**
4. **Enable GPU acceleration**
5. **Process in smaller batches**

High Memory Usage
~~~~~~~~~~~~~~~~~

**Problem:** System runs out of RAM

**Solutions:**

1. **Process fewer images at once**
2. **Reduce image resolution**
3. **Close unnecessary layers in Napari**
4. **Increase system swap space**
5. **Use 64-bit Python**

Application Crashes
~~~~~~~~~~~~~~~~~~~

**Problem:** Unexpected crashes or freezes

**Debugging Steps:**

1. **Check console for error messages**
2. **Update all dependencies:**

```bash
pip install --upgrade napari cellpose scikit-image
```

3. **Try with minimal test case:**

Process one small image to isolate the problem.

4. **Check system resources:**

```bash
# Monitor memory and CPU
top  # Linux/Mac
# or Task Manager on Windows
```

Data and File Issues
--------------------

CSV File Empty or Malformed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Results CSV is empty or doesn't open

**Solutions:**

1. **Check file exists:**

```bash
ls -lh /path/to/results.csv
```

2. **Verify analysis completed:**

Check console for "Intensity calculation complete" message.

3. **Try alternative CSV reader:**

If Excel fails, try:

```python
import pandas as pd
df = pd.read_csv('results.csv')
print(df.head())
```

Can't Find Output Files
~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Don't know where results were saved

**Solution:**

Check console output - it shows the save location:

```
Saved results to: /path/to/folder/folder_name_intensity.csv
```

Or search for files:

```bash
find /path/to/images -name "*intensity.csv"
```

Unable to Save Corrections
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** "Save" button doesn't work or corrections not saved

**Solutions:**

1. **Check write permissions:**

```bash
ls -ld /path/to/folder/
# Should show: drwxr-xr-x (writeable)
```

2. **Verify disk space:**

```bash
df -h
```

3. **Try saving to different location**

Error Messages Reference
------------------------

Common Error Messages and Solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``ValueError: shapes not aligned``

* **Cause:** Image dimensions mismatch
* **Solution:** Verify all channels are same size

``FileNotFoundError: Model file not found``

* **Cause:** Cellpose model path incorrect
* **Solution:** Update model path or use default model

``RuntimeError: CUDA error``

* **Cause:** GPU memory issue
* **Solution:** Use CPU mode or reduce image size

``PermissionError: Access denied``

* **Cause:** No write permissions
* **Solution:** Check folder permissions

``MemoryError: Unable to allocate array``

* **Cause:** Insufficient RAM
* **Solution:** Reduce image size or add more RAM

Getting Additional Help
-----------------------

Before Contacting Support
~~~~~~~~~~~~~~~~~~~~~~~~~

Please gather:

1. **Error message** (full text from console)
2. **System information** (OS, Python version)
3. **Steps to reproduce** the problem
4. **Sample images** (if possible)
5. **Console output** (copy/paste or screenshot)

Contact Information
~~~~~~~~~~~~~~~~~~~

**Email:** sagarm2@nih.gov  
**Subject line:** "Napari Chromosome Analysis - [Your Issue]"  
**Affiliation:** HITIF/LRBGE/CCR/NCI

**Include in Email:**

* Brief problem description
* Error messages
* What you've tried
* System details

Community Resources
~~~~~~~~~~~~~~~~~~~

* **Napari Documentation:** https://napari.org/
* **Cellpose Documentation:** https://cellpose.readthedocs.io/
* **GitHub Issues:** Report bugs on the repository

Next Steps
----------

* :doc:`workflow` - Review basic workflow
* :doc:`advanced_features` - Advanced troubleshooting options
* :doc:`api` - API documentation for programmatic solutions

