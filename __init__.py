"""
Napari Chromosome Analysis Toolkit

A comprehensive toolkit for analyzing metaphase chromosomes using the Napari platform.
Features chromosome segmentation, spot detection, and quantitative analysis.

Author: Md Abdul Kader Sagar
Email: sagarm2@nih.gov
Institute: National Cancer Institute/NIH
"""

__version__ = "1.0.0"
__author__ = "Md Abdul Kader Sagar"
__email__ = "sagarm2@nih.gov"

# Import main classes for easier access
try:
    from .image_processor import ImageProcessor
    from .batch_processor import BatchProcessor
    from .segmentation_postprocessing import SegmentationPostprocessing
except ImportError:
    # Handle import errors gracefully (e.g., during documentation building)
    pass

__all__ = [
    "ImageProcessor",
    "BatchProcessor", 
    "SegmentationPostprocessing",
] 