#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_plaid
----------------------------------

Tests for `plaid` module.
"""

import pytest

# from contextlib import contextmanager
# from click.testing import CliRunner
#
# from plaid import plaid
# from plaid import cli


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    pass
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    pass
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
# def test_command_line_interface():
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'plaid.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
