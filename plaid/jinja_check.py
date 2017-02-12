"""
Generic jinja2 parser
"""


import sys

from jinja2 import meta, Environment


def find_undeclared_variables(template, file_name):
    '''
    Finds undeclared variables in a jinja template. Ths checks for the use case
    when a develop inadvertently adds a file to the templates directory

    Args:
        template (jinja2.nodes.Template'): Parsed Jinja template

    Returns:
        str: Error string
    '''

    undecl_vars = meta.find_undeclared_variables(template)

    if not undecl_vars:
        return ("ERROR: Jinja2 Template File:"
                "File {0} has no variable to substitute in the template!\n"
                .format(file_name))


def parse(file_contents, file_name):
    '''
    Takes a list of files which are assumed to be jinja2 templates and tries to
    parse the contents of the files

    Args:
        file_contents (str): File contents of a jinja file

    Raises:
        Exception: An exception is raised if the contents of the file cannot be
                   parsed.
    '''

    env = Environment()
    result = ""
    try:
        ast = env.parse(file_contents)
        result = find_undeclared_variables(ast, file_name)
    except Exception:
        _, exc_value, _ = sys.exc_info()
        result += "ERROR: Jinja2 Template File: {0}".format(file_name)
        result += repr(exc_value) + '\n'

    return result
