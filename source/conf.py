# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PEB'
copyright = '2025, Kamil Lewandowski'
author = 'Kamil Lewandowski'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*.Identifier']

language = 'pl'

# -- Performance optimizations -----------------------------------------------
# Enable parallel reading of source files for faster builds
numfig = False  # Disable figure numbering to speed up builds if not needed

# Keep going on errors to build as much as possible
keep_going = True

# Source file encoding
source_encoding = 'utf-8-sig'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = []  # Empty list to avoid warnings if _static doesn't exist
html_title = "Zadanie CLAAP01"

# Performance: disable unnecessary HTML features
html_copy_source = False  # Don't copy RST source files to output
html_show_sourcelink = False  # Don't show "View page source" links
html_use_index = True  # Keep index for navigation
html_split_index = False  # Single index page is faster

latex_elements = {
        'extraclassoptions': 'openany,oneside'
        }