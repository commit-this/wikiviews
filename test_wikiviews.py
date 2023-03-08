import pytest
from wikiviews import Article, TopViews, snip_url, get_pageviews, tabulate_pageviews, get_topviews, tabulate_topviews


article = Article("Dreadnought", 2017)
topviews = TopViews("05", "2020", 50)
python = Article("Python_(programming_language)", 2021)
kiloviews = TopViews("02", "2018", 1000)
invalid_pageviews = Article("fjoeapjfapwf", 1989)
invalid_topviews = TopViews("9", "1900", 0)


def test_snip_url():
    assert snip_url("https://en.wikipedia.org/wiki/Dreadnought") == "Dreadnought"
    assert snip_url("https://en.wikipedia.org/wiki/Python_(programming_language)") == "Python_(programming_language)"
    assert snip_url("https://en.wikipedia.org/wiki/3") == "3"
    with pytest.raises(Exception):
        snip_url(3)


def test_get_pageviews():
    assert len(get_pageviews(article)) > 0
    assert len(get_pageviews(python)) > 0
    with pytest.raises(SystemExit):
        get_pageviews(invalid_pageviews)


def test_tabulate_pageviews():
    assert len(tabulate_pageviews(get_pageviews(article))) > 0


def test_get_topviews():
    assert len(get_topviews(topviews)) > 0
    assert len(get_topviews(kiloviews)) > 0
    with pytest.raises(SystemExit):
        get_topviews(invalid_topviews)

def test_tabulate_topviews():
    assert len(tabulate_topviews(get_topviews(topviews), topviews)) > 0
