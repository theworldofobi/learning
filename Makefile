# Minimal Makefile for the ASIC Design for Beginners book.
SPHINXBUILD ?= uv run sphinx-build
SPHINXOPTS  ?=
SOURCEDIR   = docs
BUILDDIR    = docs/_build

.PHONY: help sync html strict livehtml linkcheck clean

help:
	@echo "Targets:"
	@echo "  sync       install dependencies (uv sync)"
	@echo "  html       build the HTML book"
	@echo "  strict     build HTML, treating warnings as errors"
	@echo "  livehtml   live-reloading preview server"
	@echo "  linkcheck  check external links"
	@echo "  clean      remove build output"

sync:
	uv sync

html:
	$(SPHINXBUILD) -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html

strict:
	$(SPHINXBUILD) -b html -W --keep-going $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html

livehtml:
	uv run sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html --ignore "*/_build/*"

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/linkcheck

clean:
	rm -rf $(BUILDDIR)
