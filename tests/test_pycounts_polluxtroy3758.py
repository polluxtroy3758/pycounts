from collections import Counter

import matplotlib
import pytest

from pycounts_polluxtroy3758.datasets import get_flatland
from pycounts_polluxtroy3758.plotting import plot_words
from pycounts_polluxtroy3758.pycounts import count_words


@pytest.fixture
def einstein_counts():
    return Counter(
        {
            "insanity": 1,
            "is": 1,
            "doing": 1,
            "the": 1,
            "same": 1,
            "thing": 1,
            "over": 2,
            "and": 2,
            "expecting": 1,
            "different": 1,
            "results": 1,
        }
    )


def test_count_words(einstein_counts):
    """Test word counting from a file."""

    expected = einstein_counts
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"


def test_plot_words(einstein_counts):
    """Test plotting of word counts."""
    counts = einstein_counts
    fig = plot_words(counts)

    assert isinstance(fig, matplotlib.container.BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrectnumber of bars plotted"


@pytest.mark.parametrize("obj", [3.141, "test.txt", ["list", "of", "words"]])
def test_plot_words_errors(obj):
    """Check TypeError raised when Counter not used."""
    with pytest.raises(TypeError):
        plot_words(obj)


def test_integration():
    """Test count_words() and plot_words() workflow."""
    counts = count_words("tests/einstein.txt")
    fig = plot_words(counts)

    assert isinstance(fig, matplotlib.container.BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrectnumber of bars plotted"
    assert max(fig.datavalues) == 2, "Highest word count should be 2"


def test_regression():
    """Regression test for Flatland."""
    top_word = count_words(get_flatland()).most_common(1)

    assert top_word[0][0] == "the", "Most common word is not 'the'"
    assert top_word[0][1] == 2245, "'the' count has changed"
