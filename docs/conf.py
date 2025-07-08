# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Mock imports for ReadTheDocs compatibility
# These modules require GUI/GPU support that isn't available on ReadTheDocs
from unittest.mock import MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

MOCK_MODULES = [
    'napari',
    'napari.Viewer',
    'napari.utils',
    'napari.utils.notifications',
    'magicgui',
    'qtpy',
    'qtpy.QtWidgets',
    'superqt',
    'cellpose',
    'cellpose.models',
    'torch',
    'torchvision',
    'PyQt5',
    'PySide2',
    'PySide6',
    'PyQt6',
]

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()

# Set environment variable to indicate we're building docs
os.environ['SPHINX_BUILD'] = '1'


# -- Project information -----------------------------------------------------

project = 'Napari Chromosome Analysis'
copyright = '2024, Md Abdul Kader Sagar'
author = 'Md Abdul Kader Sagar'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'napari': ('https://napari.org/stable/', None),
}

# -- Options for autodoc extension -------------------------------------------

# This value selects if automatically documented members are sorted 
# alphabetically (value 'alphabetical'), by member type (value 'groupwise') 
# or by source order (value 'bysource'). The default is alphabetical.
autodoc_member_order = 'bysource'

# This value controls how to represent typehints.
autodoc_typehints = 'description'

# Mock imports and graceful error handling
autodoc_mock_imports = [
    'napari',
    'napari.Viewer',
    'napari.utils',
    'napari.utils.notifications',
    'magicgui',
    'qtpy',
    'qtpy.QtWidgets',
    'superqt',
    'cellpose',
    'cellpose.models',
    'torch',
    'torchvision',
    'PyQt5',
    'PySide2',
    'PySide6',
    'PyQt6',
]

# Continue building even with import errors
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'special-members': False,
    'private-members': False,
    'ignore-module-all': False,
}

# Skip problematic members that can't be imported
autodoc_preserve_defaults = True

# -- Options for Napoleon extension ------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Options for MyST parser ------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
] 