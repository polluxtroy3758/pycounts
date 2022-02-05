# read version from installed package
from importlib.metadata import version

__version__ = version("pycounts_polluxtroy3758")

from pycounts_polluxtroy3758.plotting import plot_words  # noqa: F401
from pycounts_polluxtroy3758.pycounts import count_words  # noqa: F401
