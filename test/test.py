from scraper.scrape import Scraper
import pytest


def test_get_url():
    scrape = Scraper()
    response = scrape.get_url("https://domoplius.lt/skelbimai/butai?action_type=1&page_nr=1&slist=109410160")
    result_status = response.status_code
    assert result_status == 200


def test_get_page_number():
    scrape = Scraper()
    result = scrape.get_page_number(31)
    assert result == 2


def test_collect_information_address():
    scrape = Scraper()
    data = scrape.collect_information(30)
    data1 = data['address'][0]
    assert data1 == '3 kambarių butas Vilniuje, Šeškinėje, Dūkštų g. +15'


def test_collect_information_area():
    scrape = Scraper()
    data = scrape.collect_information(30)
    data1 = data['area'][0]
    assert data1 == '65.00'


def test_collect_information_room():
    scrape = Scraper()
    data = scrape.collect_information(30)
    data1 = data['room'][0]
    assert data1 == '3'


def test_collect_information_year():
    scrape = Scraper()
    data = scrape.collect_information(30)
    data1 = data['year'][0]
    assert data1 == '1980'


def test_collect_information_floor():
    scrape = Scraper()
    data = scrape.collect_information(30)
    data1 = data['floor'][0]
    assert data1 == '4/9'


def test_collect_information_price():
    scrape = Scraper()
    data = scrape.collect_information(30)
    data1 = data['price'][0]
    assert data1 == '86 000 € (1 323 €/m²)'