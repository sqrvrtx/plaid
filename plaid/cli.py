# -*- coding: utf-8 -*-

import click


@click.command()
def main(args=None):
    """Console script for plaid"""
    click.echo("See click documentation at http://click.pocoo.org/")
    import plaid
    plaid.main()


if __name__ == "__main__":
    main()
