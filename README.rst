===============================
Plaid
===============================


.. image:: https://img.shields.io/pypi/v/plaid.svg
        :target: https://pypi.python.org/pypi/plaid

.. image:: https://img.shields.io/travis/sqrvrtx/plaid.svg
        :target: https://travis-ci.org/sqrvrtx/plaid

.. image:: https://readthedocs.org/projects/plaid/badge/?version=latest
        :target: https://plaid.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/sqrvrtx/plaid/shield.svg
     :target: https://pyup.io/repos/github/sqrvrtx/plaid/
     :alt: Updates


Python Ansible role checker


* Free software: MIT license
* Documentation: https://plaid.readthedocs.io.


Features
--------

Generic ansible role checker. Parses yaml, jinja2 templates and checks for
pep8/flake 8 python errors. Also check for files we expect and those we don't.
This is configured in the .plaidrc file:

---

include_files:
  - README.md
  - molecule.yml

exclude_files:
  - .travis.yml
