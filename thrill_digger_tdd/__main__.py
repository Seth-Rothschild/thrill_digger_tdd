import click
from thrill_digger_tdd import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    pass


if __name__ == "__main__":
    main()
