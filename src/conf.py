import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = html_title = 'Dasar-Dasar Pengolah Kata'
author = 'hilmanahwaa'
copyright = f'2025, {author}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_tabs.tabs'
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
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

emoji_font_stack = "'Apple Color Emoji', 'Noto Color Emoji', 'Segoe UI Emoji'"

html_theme_options = {
    "light_css_variables": {
        "font-stack": "'Noto Serif', 'New York', Cambria, Georgia, serif",
        "font-stack--monospace": "'Fira Code', 'SF Mono', Consolas, 'Courier New', Courier, monospace",
        "font-stack--headings": "'Fira Sans', 'SF Pro', 'Trebuchet MS', Helvetica, Arial, sans-serif",
    },
}

html_favicon = "_static/favicon.svg"

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

language = 'id'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['extra.css', 'fonts/fonts.css']
html_js_files = ['scripts/gumshoe-patched.js']
