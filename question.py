#text70/# question.py
#8/8/2019
import click
import re


@click.command()
@click.option('--question', prompt='Are you a robot? [y/n]',
                help='The ultimate question.')


def robot(question):
    """The answer to life itself and everything"""
    if (question == str('y')):
        click.echo('Woo-hoo a human')
    if (question == str('n')):
        click.echo("Beep-boop")
    if (question == str(42)):
        click.echo("A true believer")
    else:
        while question:
            click.echo("Try again")
            return robot()
        



if __name__ == '__main__':
    robot()
