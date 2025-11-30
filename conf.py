# Configuration file for the Sphinx documentation builder.

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
from pathlib import Path
sys.path.append(str((Path(__file__)/'../_ext').resolve()))

from datetime import datetime, timezone

project = 'Florious Blog'
html_title = project
copyright = '2025, Florious'
author = 'Florious'
release = datetime.now(timezone.utc).strftime('%Y%m%d')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'alias',
    'oi',
    'kotoba',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

language = 'zh'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
font_css = {
    'admonition-font-size': '1rem',
    'admonition-title-font-size': '1.2rem',
    'font-size--small': '90%',
    'font-size--small--2': '90%',
    'font-size--small--3': '90%',
    'font-size--small--4': '90%',
}
html_theme_options = {
    'dark_css_variables': font_css,
    'light_css_variables': font_css,
}
html_static_path = ['_static']

# -- Options for comments
kotoba = {
    'giscus': {
        'data-repo': 'florious0721/blog',
        'data-repo-id': 'R_kgDOQXP2nA',
        'data-category-id': 'DIC_kwDOQXP2nM4CzLoZ',
        'data-mapping': 'pathname',
        'data-strict': '0',
        'data-reactions-enabled': '1',
        'data-emit-metadata': '0',
        'data-input-position': 'top',
        'data-theme': 'preferred_color_scheme',
        'data-lang': 'zh-CN',
        'data-loading': 'lazy',
        'crossorigin': 'anonymous',
    }
}


# -- Options for extlinks
extlinks = {
    'github': ('https://github.com/%s', ''),
    'rtd': ('https://%s.readthedocs.io', '%s 文档'),
}

# -- Options for todolist
todo_include_todos = True
