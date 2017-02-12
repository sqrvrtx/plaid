# -*- coding: utf-8 -*-

import os
import subprocess

import yaml

import yml_check
import jinja_check


def find_files(filenames, check_files, include=True):

    if include:
        for fname in check_files:
            if fname not in filenames:
                yield "{0} not in directory - please add".format(fname)
    elif not include:
        for fname in check_files:
            if fname in filenames:
                yield "{0} in directory - please remove".format(fname)


def run(*args):
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, _ = p.communicate()
    return out


def do_check_pep8(files, status):
    """
    Run the python pep8 tool against the filst of supplied files.
    Append any linting errors to the returned status list

    Args:
        files (str): list of files to run pep8 against
        status (list): list of pre-receive check failures to eventually print
                       to the user

    Returns:
       status list of current pre-redeive check failures. Might be an empty
       list.
    """
    for file_name in files:

        args = ['flake8', '--max-line-length=120', '{0}'.format(file_name)]
        output = run(*args)

        if output:
            status.append("Python PEP8/Flake8: {0}: {1}".format(file_name,
                                                                output))

    return status


def do_check(func, files, status):
    """
    Generic do_check helper method

    Args:
        func (function): Specific function to call
        files (list): list of files to run against
        status (list): list of pre-receive check failures to eventually print
                       to the user

    Returns:
       status list of current pre-redeive check failures. Might be an empty
       list.
    """

    for file_name in files:
        with open(file_name, 'r') as f:
            output = func.parse(f.read(), file_name)

        if output:
            status.append("{0}: {1}".format(file_name, output))

    return status


def get_directory_tree():
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            yield(os.path.join(root, name))


def main():
    mypath = os.path.join(os.path.expanduser('~'), '.plaidrc')
    with open(mypath, 'r') as f:
        yaml_dict = yaml.load(f.read())

    files = list(get_directory_tree())
    yml_files = [x for x in files if x.endswith('.yml')]
    jinja_files = [x for x in files if x.endswith('.j2')]
    py_files = [x for x in files if x.endswith('.py')]
    status = []
    status = do_check(yml_check, yml_files, status)
    status = do_check(jinja_check, jinja_files, status)
    status = do_check_pep8(py_files, status)

    if status:
        print("****************************\n\n"
              "Ansible checks FAILED:\n"
              "Please study the output and please resolve\n\n"
              "***************************\n")
        for msg in status:
            print(msg)

    filenames = [os.path.basename(x) for x in files]

    include_files = yaml_dict.get('include_files')
    if include_files:
        for result in find_files(filenames, include_files):
            print(result)

    exclude_files = yaml_dict.get('exclude_files')
    if exclude_files:
        for result in find_files(filenames, exclude_files, include=False):
            print(result)
