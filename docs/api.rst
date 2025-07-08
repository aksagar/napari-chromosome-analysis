API Documentation
=================

This section provides detailed documentation for the programmatic interface of the Napari Chromosome Analysis toolkit.

Core Classes
------------

ImageProcessor
~~~~~~~~~~~~~~

The main image processing class that handles segmentation, spot detection, and analysis.

.. autoclass:: image_processor.ImageProcessor
   :members:
   :undoc-members:
   :show-inheritance:

Key Methods:

* ``load_images(folder_path, dapi_id, dna_fish_id, cenpc_id, skip_segmentation)``
* ``segment_image(image, save_dir=None)``
* ``detect_spots_cent(image, channel_type, threshold, save_dir=None)``
* ``find_common()``
* ``measure_intensity_at_spots(intensity_image, spots_df, channel_name)``

BatchProcessor
~~~~~~~~~~~~~~

Handles batch processing of multiple image folders.

.. autoclass:: batch_processor.BatchProcessor
   :members:
   :undoc-members:
   :show-inheritance:

Key Methods:

* ``batch_processing(root_folder, dapi_id, dna_fish_id, cenpc_id, skip_segmentation)``

SegmentationPostprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides post-processing operations for segmentation results.

.. autoclass:: segmentation_postprocessing.SegmentationPostprocessing
   :members:
   :undoc-members:
   :show-inheritance:

GUI Components
--------------

The main application includes several GUI components built with magicgui and Qt:

Control Widgets
~~~~~~~~~~~~~~~

* ``ControlWidgetDNAFISH`` - DNA-FISH spot detection controls
* ``ControlWidgetCENPC`` - CENP-C spot detection controls
* ``ChannelIdentifiers`` - Channel configuration widget
* ``SegmentDAPIWidget`` - DAPI segmentation controls

Main Functions
~~~~~~~~~~~~~~

Core analysis functions accessible through the GUI:

* ``load_images()`` - Load multi-channel images
* ``segment_image()`` - Segment chromosomes using Cellpose
* ``detect_dna_fish_spots()`` - Detect DNA-FISH spots
* ``detect_cenpc_spots()`` - Detect CENP-C spots
* ``find_common()`` - Find overlapping regions
* ``get_intensity_at_cenpc_location()`` - Measure intensities

Usage Examples
--------------

Basic Usage
~~~~~~~~~~~

Here's how to use the core classes programmatically:

.. code-block:: python

    from image_processor import ImageProcessor
    from batch_processor import BatchProcessor
    
    # Initialize processor
    processor = ImageProcessor()
    
    # Load images
    images = processor.load_images(
        folder_path="path/to/images",
        dapi_id="DAPI",
        dna_fish_id="DNA-FISH", 
        cenpc_id="CENP-C",
        skip_segmentation=False
    )
    
    # Segment chromosomes
    if images:
        masks = processor.segment_image(images[0])
        
        # Detect spots
        spots_ch1 = processor.detect_spots_cent(
            images[1], 'DNA-FISH', threshold=0.4
        )
        spots_ch2 = processor.detect_spots_cent(
            images[2], 'CENP-C', threshold=0.4
        )
        
        # Find common regions
        common_nuclei = processor.find_common()
        
        # Measure intensities
        results = processor.gen_intensity_from_df(
            processor.img_cenpc, 
            processor.df_centroid_dna_fish
        )

Batch Processing
~~~~~~~~~~~~~~~~

For processing multiple folders:

.. code-block:: python

    from batch_processor import BatchProcessor
    from image_processor import ImageProcessor
    
    # Initialize components
    processor = ImageProcessor()
    
    # Mock control widgets (normally from GUI)
    class MockWidget:
        def __init__(self, threshold):
            self.threshold = threshold
        def value(self):
            return self.threshold
        
        class slider:
            def __init__(self, threshold):
                self.threshold = threshold
            def value(self):
                return self.threshold
    
    control_dna_fish = MockWidget(40)
    control_cenpc = MockWidget(40)
    
    # Initialize batch processor
    batch_processor = BatchProcessor(
        processor, 
        control_dna_fish, 
        control_cenpc
    )
    
    # Run batch processing
    batch_processor.batch_processing(
        root_folder="path/to/root",
        dapi_id="DAPI",
        dna_fish_id="DNA-FISH",
        cenpc_id="CENP-C",
        skip_segmentation=False
    )

Custom Analysis
~~~~~~~~~~~~~~~

For advanced users who want to modify the analysis pipeline:

.. code-block:: python

    import numpy as np
    from image_processor import ImageProcessor
    from skimage.io import imread
    
    class CustomAnalyzer(ImageProcessor):
        def __init__(self):
            super().__init__()
            
        def custom_segmentation(self, image, custom_params):
            """Custom segmentation method"""
            # Your custom segmentation logic here
            pass
            
        def custom_spot_detection(self, image, custom_threshold):
            """Custom spot detection method"""
            # Your custom spot detection logic here
            pass
            
        def custom_analysis_pipeline(self, folder_path):
            """Complete custom analysis pipeline"""
            # Load images
            images = self.load_images(folder_path, "DAPI", "CH1", "CH2", False)
            
            # Custom segmentation
            masks = self.custom_segmentation(images[0], {})
            
            # Custom spot detection
            spots1 = self.custom_spot_detection(images[1], 0.5)
            spots2 = self.custom_spot_detection(images[2], 0.5)
            
            # Continue with standard analysis
            return self.gen_intensity_from_df(images[2], spots1)

Parameters Reference
--------------------

Segmentation Parameters
~~~~~~~~~~~~~~~~~~~~~~~

**Cellpose Parameters**:

* ``model_type``: 'cyto' or custom model path
* ``diameter``: None (auto-detect) or specific pixel diameter
* ``channels``: [0,0] for grayscale input
* ``gpu``: True/False for GPU acceleration

**Post-processing Parameters**:

* ``remove_small_objects``: Boolean, removes objects below size threshold
* ``remove_edge_objects``: Boolean, removes objects touching borders
* ``fill_holes``: Boolean, fills holes in segmented objects
* ``smooth_boundaries``: Boolean, applies morphological smoothing

Spot Detection Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

**Detection Parameters**:

* ``threshold``: Float 0-1, detection sensitivity
* ``min_distance``: Minimum distance between spots
* ``num_peaks``: Maximum number of peaks to detect

**Filtering Parameters**:

* ``min_intensity``: Minimum spot intensity
* ``max_intensity``: Maximum spot intensity
* ``exclusion_radius``: Radius around spots to exclude

Data Structures
---------------

The API works with several key data structures:

Spot DataFrames
~~~~~~~~~~~~~~~

Spot detection results are returned as pandas DataFrames with columns:

* ``X``: X-coordinate of spot centroid
* ``Y``: Y-coordinate of spot centroid
* ``intensity``: Spot intensity value
* ``label``: Associated nucleus label

Segmentation Masks
~~~~~~~~~~~~~~~~~~

Segmentation results are numpy arrays where:

* ``0``: Background pixels
* ``1, 2, 3, ...``: Individual nucleus labels

Intensity Results
~~~~~~~~~~~~~~~~~

Intensity measurements are returned as DataFrames with:

* ``spot_x``, ``spot_y``: Spot coordinates
* ``intensity_ch1``, ``intensity_ch2``: Intensity values
* ``nucleus_label``: Associated nucleus
* ``folder``: Source folder (for batch processing)

Error Handling
--------------

The API includes comprehensive error handling:

.. code-block:: python

    try:
        results = processor.segment_image(image)
    except Exception as e:
        print(f"Segmentation failed: {e}")
        # Handle error appropriately

Common exceptions:

* ``FileNotFoundError``: Image files not found
* ``ValueError``: Invalid parameters
* ``RuntimeError``: Cellpose model errors
* ``MemoryError``: Insufficient memory for processing

Extension Points
----------------

The codebase is designed to be extensible:

Custom Models
~~~~~~~~~~~~~

Replace the default Cellpose model:

.. code-block:: python

    # In image_processor.py, modify segment_image method
    def segment_image(self, image, custom_model_path=None):
        if custom_model_path:
            model = models.CellposeModel(
                gpu=True, 
                pretrained_model=custom_model_path
            )
        else:
            # Use default model
            pass

Custom Post-processing
~~~~~~~~~~~~~~~~~~~~~~

Add custom post-processing steps:

.. code-block:: python

    from segmentation_postprocessing import SegmentationPostprocessing
    
    class CustomPostprocessing(SegmentationPostprocessing):
        def custom_filter(self, masks, params):
            # Your custom filtering logic
            return filtered_masks

Custom Visualization
~~~~~~~~~~~~~~~~~~~~

Add custom visualization layers:

.. code-block:: python

    # Add custom layers to napari viewer
    viewer.add_labels(custom_masks, name='Custom Segmentation')
    viewer.add_points(custom_spots, name='Custom Spots')

This API documentation provides the foundation for extending and customizing the Napari Chromosome Analysis toolkit for your specific research needs. 