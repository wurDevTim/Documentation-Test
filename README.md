# Documentation-Test
Documentation Test

### Build requirements:
mkdocs >= 1.5.3
mkdocs-material >= 9.5.6


### Documentation
Build with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)



How to Build
- Make a Venv
'''
python -m venv venv
venv/Scripts/activate
'''
- Install dependencies
'''
pip install mkdocs >= 1.5.3
pip install mkdocs-material >= 9.5.9
pip install mkdocstrings >= 0.24.0
pip install mkdocstrings[python]
'''

Testing:
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.

Publish on github:
'
mkdocs gh-deploy
'

For full documentation visit [mkdocs.org](https://www.mkdocs.org).