import imp
import os

import click
import logging

logging.basicConfig(level="INFO", format='%(message)s')
logging.getLogger().handlers[0].setFormatter(
            logging.Formatter('%(message)s'))

logger = logging.getLogger("oda_api")
logger.setLevel("DEBUG")


@click.command()
@click.argument("test_file")
@click.argument("test_name")
@click.option('--argument', '-a', multiple=True)
def cli(test_file, test_name, argument):
    m = imp.load_source(
            os.path.basename(test_file).replace(".py", ""), 
            test_file)
    getattr(m, test_name)(*argument)

if __name__ == "__main__":
    cli()
    
