import click
from .monitor import SystemMonitor

@click.command()
@click.option('--theme', '-t', default='default', help='Color theme (default, dark, light)')
def main(theme):
    """📊 Term-Stat: Lightweight System Monitor"""
    monitor = SystemMonitor()
    monitor.run()

if __name__ == '__main__':
    main()
