"""Sphinx configuration."""
project = "Add Only Dictionary"
author = "Matt Koski"
copyright = "2022, Matt Koski"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
