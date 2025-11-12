Advanced Features
=================

Advanced capabilities and customization options for power users.

Parameter Optimization
----------------------

Fine-tuning detection parameters for your specific imaging conditions.

Threshold Optimization Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Systematic Approach:**

1. **Start with default** (50 for both channels)
2. **Visual inspection** - Check for false positives/negatives
3. **Adjust incrementally** - Change by ±10 and reassess
4. **Test on multiple images** - Verify consistency
5. **Document optimal values** - Record for future use

**Optimization Metrics:**

* **Sensitivity**: Percentage of true spots detected
* **Specificity**: Percentage of detections that are true spots
* **Balance**: Trade-off between false positives and false negatives

**Ground Truth Validation:**

For critical applications:

1. Manually count spots in 3-5 representative images
2. Test threshold values from 30-70 in increments of 10
3. Calculate accuracy for each threshold
4. Choose value with best balance

Post-Processing Options
~~~~~~~~~~~~~~~~~~~~~~~

**Cellpose Segmentation:**

Advanced users can modify segmentation parameters in the code:

* ``diameter``: Expected chromosome size
* ``flow_threshold``: Segmentation sensitivity  
* ``cellprob_threshold``: Detection threshold

**Spot Detection:**

Modify detection algorithm parameters:

* Minimum spot size (pixels)
* Maximum spot size (pixels)
* Background subtraction method

Data Export Options
-------------------

CSV File Customization
~~~~~~~~~~~~~~~~~~~~~~

**Default Columns:**

* ``spot_id``
* ``x_coordinate``, ``y_coordinate``
* ``channel1_intensity``, ``channel2_intensity``
* ``folder_name``

**Additional Data** (can be enabled):

* Spot area (pixels)
* Spot eccentricity
* Background intensity
* Chromosome ID
* Distance to nearest spot

**Export Format Options:**

* CSV (default, Excel-compatible)
* TSV (tab-separated)
* JSON (for programmatic access)
* HDF5 (for large datasets)

Image Export
~~~~~~~~~~~~

**From Napari:**

File → Save Selected Layer(s)

**Exportable Layers:**

* Original images
* Segmentation overlays
* Spot detections
* Combined visualizations

**Formats:**

* PNG (publication-ready)
* TIFF (preserves metadata)
* PDF (vector graphics)

**Batch Image Export:**

Save visualizations for all processed images:

1. Enable "Save visualizations" in batch processing
2. PNG files saved automatically
3. Named: ``<folder>_visualization.png``

Integration with Other Tools
-----------------------------

Python Scripting
~~~~~~~~~~~~~~~~

Use the toolkit programmatically:

```python
from image_processor import ImageProcessor

# Initialize processor
processor = ImageProcessor()

# Load images
processor.load_images('path/to/images', 
                     dapi_id='435',
                     ch1_id='525', 
                     ch2_id='679')

# Run analysis
processor.segment_image()
processor.detect_spots1(threshold=0.5)
processor.detect_spots2(threshold=0.5)
processor.find_common()

# Get results
results = processor.measure_intensity_at_spots()
```

**Benefits:**

* Automated workflows
* Custom parameter sweeps
* Integration with analysis pipelines
* High-throughput processing

Jupyter Notebook Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run analyses interactively:

```python
import napari
from image_processor import ImageProcessor

# Create viewer
viewer = napari.Viewer()

# Load and analyze
processor = ImageProcessor(viewer=viewer)
processor.load_images('sample_folder')
processor.segment_image()

# Interactive visualization in notebook
viewer.show()
```

External Analysis Tools
~~~~~~~~~~~~~~~~~~~~~~~

**Export to:**

* **R**: Read CSV files with ``read.csv()``
* **MATLAB**: Import with ``readtable()``
* **GraphPad Prism**: Open CSV directly
* **ImageJ/Fiji**: Export segmentation as TIFF
* **Python pandas**: ``pd.read_csv()``

Performance Optimization
------------------------

GPU Acceleration
~~~~~~~~~~~~~~~~

**Enable CUDA for Cellpose:**

```bash
# Install PyTorch with CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

**Verify GPU Usage:**

Check console output for:

```
Using GPU for Cellpose segmentation
Device: CUDA (NVIDIA GeForce RTX 3080)
```

**Performance Gains:**

* CPU: 30-60 seconds per image
* GPU: 5-15 seconds per image
* **4-6x speedup** with GPU

Memory Management
~~~~~~~~~~~~~~~~~

**For Large Images:**

* Reduce image resolution if possible
* Process in smaller tiles
* Close other applications
* Increase system swap space

**For Batch Processing:**

* Process in chunks of 20-50 images
* Clear results periodically
* Monitor system memory usage

Parallel Processing
~~~~~~~~~~~~~~~~~~~

**Multi-CPU Processing:**

Enable multi-threading in batch processing:

```python
processor.batch_process(folders, 
                       n_workers=4,
                       use_gpu=True)
```

**Guidelines:**

* Set ``n_workers`` = number of CPU cores - 1
* Don't exceed available CPU cores
* GPU processing is still single-threaded

Custom Trained Models
---------------------

Using Your Own Cellpose Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Train Custom Model:**

1. Prepare training data (images + manual labels)
2. Train Cellpose model following their documentation
3. Save trained model file

**Use in Toolkit:**

Update model path in code:

```python
model_path = '/path/to/your/custom_model'
processor.segment_image(model_path=model_path)
```

**When to Train Custom Models:**

* Default model doesn't work well
* Unusual chromosome morphology
* Different cell types
* Specific experimental conditions

Model Performance Evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Metrics:**

* Intersection over Union (IoU)
* Precision/Recall
* F1 Score
* Visual comparison with manual annotations

**Validation Dataset:**

* 10-20 manually annotated images
* Representative of experimental conditions
* Test on independent data (not training set)

Advanced Batch Processing
--------------------------

Conditional Processing
~~~~~~~~~~~~~~~~~~~~~~

Process images based on conditions:

```python
# Only process images with > 20 chromosomes
if processor.count_chromosomes() > 20:
    processor.detect_spots1()
    processor.detect_spots2()
```

**Use Cases:**

* Quality filtering
* Selective analysis
* Multi-stage processing

Parameter Sweeps
~~~~~~~~~~~~~~~~

Test multiple parameter combinations:

```python
thresholds = [30, 40, 50, 60, 70]

for t1 in thresholds:
    for t2 in thresholds:
        processor.detect_spots1(threshold=t1/100)
        processor.detect_spots2(threshold=t2/100)
        results = processor.measure_intensity()
        save_results(f'results_t1{t1}_t2{t2}.csv', results)
```

**Applications:**

* Parameter optimization
* Sensitivity analysis
* Method comparison

Custom Metrics
--------------

Calculating Additional Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Spot Density:**

```python
n_spots = len(spot_coordinates)
area = np.sum(segmentation > 0)  # pixels
density = n_spots / area
```

**Co-localization Metrics:**

* Overlap coefficient
* Pearson correlation
* Manders coefficients

**Chromosome Metrics:**

* Area
* Perimeter
* Eccentricity
* Orientation

Statistical Analysis Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Export for Statistics:**

```python
import pandas as pd

# Load results
df = pd.read_csv('results.csv')

# Calculate statistics
mean_intensity = df['channel1_intensity'].mean()
std_intensity = df['channel1_intensity'].std()

# Group by folder
grouped = df.groupby('folder_name').mean()
```

**Visualization:**

```python
import matplotlib.pyplot as plt

# Plot intensity distribution
plt.hist(df['channel1_intensity'], bins=50)
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.savefig('intensity_distribution.png')
```

Quality Control Metrics
-----------------------

Automated QC Checks
~~~~~~~~~~~~~~~~~~~

**Image Quality:**

* Check for saturation (% pixels at max value)
* Verify signal-to-noise ratio
* Detect out-of-focus images

**Analysis Quality:**

* Flag images with unusually high/low spot counts
* Identify failed segmentations
* Detect outliers in intensity distributions

**Implementation:**

```python
# Flag suspicious images
if processor.count_spots() < 5:
    print(f"WARNING: Very few spots detected in {folder_name}")
    
if processor.count_chromosomes() > 100:
    print(f"WARNING: Segmentation may have errors in {folder_name}")
```

Troubleshooting Advanced Issues
--------------------------------

**Performance Bottlenecks:**

* Profile code to identify slow steps
* Use smaller images for testing
* Optimize I/O operations

**Memory Leaks:**

* Clear variables after processing
* Use context managers for file operations
* Monitor memory usage during batch processing

**Reproducibility:**

* Set random seeds
* Document all parameter changes
* Version control analysis scripts
* Save processing logs

Next Steps
----------

* :doc:`troubleshooting` - Common issues and solutions
* :doc:`api` - API reference documentation
* Contact: sagarm2@nih.gov for advanced support

