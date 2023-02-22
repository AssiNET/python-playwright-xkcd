import pytest
import os
import datetime

from pages.about import AboutPage
from pages.home import HomePage
from playwright.sync_api import Page

@pytest.fixture
def home_page(page: Page) -> HomePage:
    home_p = HomePage(page)
    home_p.load()
    return home_p

@pytest.fixture
def about_page(page: Page) -> AboutPage:
    about_p = AboutPage(page)
    about_p.load()
    return about_p

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = 'reports/'+datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+".html"