Installation
============

This guide will help you install the Napari Chromosome Analysis toolkit.

Requirements
------------

The following are required to run this software:

* Python 3.8 or higher
* CUDA-compatible GPU (recommended for Cellpose)
* At least 8GB of RAM

Dependencies
------------

The main dependencies include:

* `napari <https://napari.org/>`_ - Multi-dimensional image viewer
* `cellpose <https://github.com/MouseLand/cellpose>`_ - Cell segmentation
* `scikit-image <https://scikit-image.org/>`_ - Image processing
* `numpy <https://numpy.org/>`_ - Numerical computing
* `pandas <https://pandas.pydata.org/>`_ - Data analysis
* `matplotlib <https://matplotlib.org/>`_ - Plotting
* `magicgui <https://github.com/pyapp-kit/magicgui>`_ - GUI widgets
* `qtpy <https://github.com/spyder-ide/qtpy>`_ - Qt abstraction layer

Installation Steps
------------------

1. **Clone the repository**::

    git clone <repository-url>
    cd napari_ui

2. **Create a conda environment**::

    conda create -n napari-chr python=3.9
    conda activate napari-chr

3. **Install dependencies**::

    pip install napari cellpose scikit-image numpy pandas matplotlib magicgui qtpy superqt pillow

4. **Install Cellpose model**::

    # The code expects a trained Cellpose model at:
    # /gpfs/gsfs10/users/sagarm2/cellpose_chr/newDataSet/trainingfiles/models/cellpose_1718127286.8010929
    # You may need to update the path in the code to point to your model

5. **Test the installation**::

    python main.py

GPU Support
-----------

For optimal performance with Cellpose segmentation, ensure you have:

* CUDA toolkit installed
* Compatible GPU drivers
* PyTorch with CUDA support

To install PyTorch with CUDA support::

    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

Troubleshooting
---------------

**ImportError: No module named 'napari'**
    Make sure you have activated the correct conda environment and installed all dependencies.

**CUDA out of memory**
    Reduce the image size or use CPU-only mode by setting ``gpu=False`` in the Cellpose model initialization.

**Qt application issues**
    Ensure you have a compatible Qt backend installed. Try::
    
        pip install PyQt5
        
    or::
    
        pip install PySide2 