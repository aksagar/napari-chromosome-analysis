Tutorial: Your First Analysis
==============================

This tutorial will guide you through your first chromosome analysis from start to finish. By the end, you'll have processed an image and generated results.

Prerequisites
-------------

Before starting this tutorial, ensure you have:

* ✅ Installed the software (see :doc:`installation`)
* ✅ Sample images ready (3 channels: DAPI, DNA-FISH, CENP-C)
* ✅ Images in a single folder

.. tip::
   Don't have test images? Use the sample dataset provided with the repository.

Step 1: Launch the Application
-------------------------------

Open a terminal and run::

    python main.py

The Napari viewer window will open with the chromosome analysis interface.

.. figure:: _static/images/slide_02_the_interface_img02.png
   :alt: Main interface
   :align: center
   :width: 85%

   **The main interface** - Ready for your first analysis

Understanding the Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interface has three main areas:

* **Left panel**: Image layers and folder list
* **Right panel**: Control widgets and analysis buttons
* **Center**: Napari viewer for visualizing your images

Step 2: Configure Channel Identifiers
--------------------------------------

Before loading images, tell the software how to identify your channels.

.. figure:: _static/images/slide_03_workflow_guide_step_1_setting_img03.png
   :alt: Channel configuration
   :align: center
   :width: 70%

   **Channel identifiers** - Configure to match your filenames

In the **Channel Identifiers** section, enter:

* **DAPI Channel Identifier**: ``435`` (or ``dapi``, ``DAPI``, etc.)
* **Channel 1 Identifier**: ``525`` (or ``dna_fish``, ``DNA-FISH``, etc.)
* **Channel 2 Identifier**: ``679`` (or ``cenpc``, ``CENP-C``, etc.)

.. note::
   The identifiers should match part of your image filenames. For example, if your files are named ``image_w435.tif``, ``image_w525.tif``, and ``image_w679.tif``, use ``435``, ``525``, and ``679``.

Step 3: Load Your Images
-------------------------

1. Click the **Load Images** button
2. Navigate to your image folder
3. Click **Select**

Your images will load into the viewer!

.. figure:: _static/images/slide_04_step_2_loading_images_click_l_img04.png
   :alt: After loading images
   :align: center
   :width: 80%

   **Images loaded** - All three channels are now visible

Exploring Your Images
~~~~~~~~~~~~~~~~~~~~~

.. figure:: _static/images/slide_05_this_is_how_napari_works._all__img05.png
   :alt: Layer controls
   :align: center
   :width: 75%

   **Layer controls** - Toggle visibility and adjust contrast

* Click the **eye icon** to show/hide layers
* Use **Toggle All Layers** to show/hide everything
* Adjust the **contrast sliders** for each layer
* Use mouse **scroll wheel** to zoom
* **Click and drag** to pan

Step 4: Segment Chromosomes
----------------------------

Click the **Segment (DAPI) Image** button.

The software will use Cellpose to automatically identify individual chromosomes.

.. figure:: _static/images/slide_06_slide_6_img06.jpg
   :alt: Segmentation result
   :align: center
   :width: 75%

   **Segmentation complete** - Each chromosome is labeled with a different color

.. tip::
   If segmentation takes too long or you only want to analyze spots, check the **Skip Segmentation** checkbox before loading images.

Step 5: Detect Spots in Channel 1
----------------------------------

1. Look at the **DNA-FISH Threshold** slider (default: 50)
2. Leave it at 50 for now (we'll optimize later)
3. Click **Detect Channel 1 Spots**

.. figure:: _static/images/slide_08_after_clicking_detect_channel__img08.png
   :alt: Channel 1 spots detected
   :align: center
   :width: 80%

   **Spots detected** - Brown markers show DNA-FISH spot locations

The detected spots appear as a new layer. Toggle the DNA-FISH layer on/off to see how spots align with the signal.

Step 6: Detect Spots in Channel 2
----------------------------------

1. Check the **CENP-C Threshold** slider (default: 50)
2. Click **Detect Channel 2 Spots**

.. figure:: _static/images/slide_09_do_the_same_for_channel_2_and__img09.png
   :alt: Both channels detected
   :align: center
   :width: 80%

   **Both channels** - Spots detected in DNA-FISH and CENP-C

Now you have spots detected in both channels!

Step 7: Find Common Regions
----------------------------

Click **Find Common** to identify chromosomes where both signals are present.

This step filters your data to include only meaningful co-localized signals, removing background noise.

.. tip::
   This step is important! It ensures you're only measuring regions where both signals actually overlap.

Step 8: Get Results
--------------------

Click **Get Intensity at Spots Location**.

The software will:

* Calculate Channel 2 intensity at Channel 1 spot locations
* Calculate Channel 1 intensity at Channel 2 spot locations
* Save results as a CSV file

**Where are my results?**

Check the terminal output - it will show you where the CSV file was saved. The file is named ``<folder_name>_intensity.csv`` in the same folder as your images.

.. note::
   The CSV file contains spot coordinates, intensity values, and metadata for further analysis in Excel, Python, R, or other tools.

Congratulations! 🎉
-------------------

You've completed your first analysis!

Your results are saved and ready for further analysis.

What's Next?
------------

Now that you've completed a basic analysis, you can:

**Optimize Your Analysis**

* Adjust threshold sliders to optimize spot detection
* Learn about manual corrections in :doc:`manual_corrections`
* Understand all parameters in :doc:`workflow`

**Process More Images**

* Use "Run All" for one-click analysis: :doc:`workflow`
* Process multiple images with batch processing: :doc:`batch_processing`

**Understand Your Results**

* Learn about the CSV output format
* Explore advanced features in :doc:`advanced_features`

Quick Reference: One-Click Analysis
------------------------------------

Once you know your optimal thresholds, use **Run All** for faster processing:

.. figure:: _static/images/slide_13_run_all_img12.png
   :alt: Run All button
   :align: center
   :width: 60%

   **Run All** - One-click analysis with your configured settings

1. Configure channel identifiers
2. Load images
3. Adjust both threshold sliders
4. Click **Run All**

Done! Results are automatically saved.

Troubleshooting
---------------

**Problem: No spots detected**

* **Solution**: Lower the threshold slider value (try 30-40)

**Problem: Too many spots (false positives)**

* **Solution**: Increase the threshold slider value (try 60-70)

**Problem: Segmentation failed**

* **Solution**: Check that DAPI image has good contrast and chromosomes are well-separated

**Problem: Images won't load**

* **Solution**: Verify filenames contain your configured identifiers

Need More Help?
---------------

* **Detailed guide**: :doc:`workflow`
* **Manual corrections**: :doc:`manual_corrections`
* **Batch processing**: :doc:`batch_processing`
* **Contact**: sagarm2@nih.gov

