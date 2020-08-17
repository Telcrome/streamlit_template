import os
import click
import streamlit.cli


@click.group()
def main():
    """
    Main entry point for cli tools
    """
    pass


@main.command(name='gui')
def main_gui():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'gui.py')
    args = []
    streamlit.cli._main_run(filename, args)


if __name__ == '__main__':
    main()
