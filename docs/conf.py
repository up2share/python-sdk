import os
import sys

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(".."))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Up2Share SDK'
copyright = '2025 Up2Share'
author = 'Up2Share'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

# Add 'm2r' for Markdown support
extensions += ['m2r']

# Specify the file format for source files (Markdown)
source_suffix = '.rst'
source_encoding = 'utf-8-sig'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_mock_imports = ["external_dependency"]


# Define the master document to be index (or any other name you prefer)
master_doc = 'index'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "0.2"
# The full version, including alpha/beta/rc tags.
release = "0.2.0"

release_date = "October 19, 2023"

site_base = os.environ.get("RTD_SITE_BASE", "https://up2sha.re")
