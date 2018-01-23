import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver


class JsSpider():
    """
    A spider that can scape the js rendered page, it might takes longer
    compare with the static Spider :O
    """
    def __init__(self, url):
        """
        Loading the js rendered webpage using Chrome Broswer
        Simulator.
        Arg: url: The root url
        """
        self._driver = webdriver.Chrome()
        self._driver.get(url)
        self._url = url
        self._soup = None

    def scroll_bottom(self):
        """
        Simulate the action that scrolls the page to the most bottom.
        This is useful when the webpage is loading dynamicly.
        """
        # Execute Js
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait(self, seconds):
        """
        Make the JsSpider wait for seconds before retriving the page source,
        this method give time for the browser the execute the JavaScriipt and
        the waiting time is vary.
        """
        time.sleep(seconds)

    def parse(self):
        """
        Start parsing the page, this method should be called
        after all actions.
        """
        self._soup = BeautifulSoup(self._driver.page_source, 'lxml')
    
    def find_inner(self, outer_tag, type_, class_name):
        """
        Find only one specific inner tag by its class name, the first
        tag that matches will be returned
        Arg: outer_tag: The outer tag, for exmaple if a div contains
                        another div, the outer tag should be the previous one.
                        And it should be a Tag object in BeautifulSoup
        Arg: type_: The type of the tag that is looking for, such as 'a', 'p'
        Arg: class_name: The class attribute of the tag, if there is no class name,
                         it should be '/'
        """
        if class_name == "/":
            return outer_tag.find(type_)
        else:
            return outer_tag.find(type_, {"class": class_name})

    def find_inners(self, outer_tag, type_, class_name):
        """
        Find all specific tags inside another tag by the given
        class name, if there are more than one tag, it will return a list
        Arg: outer_tag: The outer tag, for exmaple if a div contains
                        another div, the outer tag should be the previous one.
                        And it should be a Tag object in BeautifulSoup
        Arg: type_: The type of the tag that is looking for, such as 'a', 'p'
        Arg: class_name: The class attribute of the tag, if there is no class name,
                         it should be '/'
        """
        if class_name == "/":
            return outer_tag.find_all(type_)
        else:
            return outer_tag.find_all(type_, {"class": class_name})

    def find_tag(self, type_, class_name):
        """
        Find only one specific tag by its class name, the first
        tag that matches will be returned
        Arg: type_: The type of the tag, such as 'a', 'p', 'div' and so on
        Arg: class_name: The class attribute of the tag, if there is no class name,
                         it should be '/'
        """
        if class_name == "/":
            return self._soup.find(type_)
        else:
            return self._soup.find(type_, {"class": class_name})

    def find_tags(self, type_, class_name):
        """
        Find all specific tags by the given class name, if there are
        more than one tag, it will return a list
        Arg: type_: The type of the tag, such as 'a', 'p', 'div' and so on
        Arg: class_name: The class attribute of the tag, if there is no class name,
                         it should be '/'
        """
        if class_name == "/":
            return self._soup.find_all(type_)
        else:
            return self._soup.find_all(type_, {"class": class_name})

    def quit_spider(self):
        """
        Quit the browser simulator, this step is important and must
        be done, otherwise it will have to be shutted down manually
        """
        self._driver.quit()


class Spider():
    "Static web spider, useful to scrape static html page :/"
    def __init__(self, url):
        """
        Initializing, request html page.
        Arg: url: The root url
        """
        self._url = url
        req = Request(self._url, headers={'User-Agent': 'Mozilla/5.0'})
        _raw_page = urlopen(req).read()
        # Analyze using beautifulsoup
        self._soup = BeautifulSoup(_raw_page.decode('utf-8'), 'lxml')
    
    def find_inner(self, outer_tag, type_, class_name):
        """
        Find only one specific inner tag by its class name, the first
        tag that matches will be returned
        Arg: outer_tag: The outer tag, for exmaple if a div contains
                        another div, the outer tag should be the previous one.
                        And it should be a Tag object in BeautifulSoup
        Arg: type_: The type of the tag that is looking for, such as 'a', 'p'
        Arg: class_name: The class attribute of the tag, if there is no class name,
                         it should be '/'
        """
        if class_name == "/":
            return outer_tag.find(type_)
        else:
            return outer_tag.find(type_, {"class": class_name})
    
    def find_inners(self, outer_tag, type_, class_name):
        """
        Fetch informations inside a specific tag.
        This method will return the Tag objects in BeautifulSoup,
        if there are more than one Tag, it will be a list
        Arg: outer_tag: The outer tag, for exmaple if a div contains
                        another div, the outer tag should be the previous one.
                        And it should be a Tag object in BeautifulSoup
        Arg: type_: The type of the tag that is looking for, such as 'a', 'p'
        Arg: class_name: The class attribute of the tag, if there is no class name,
                         it should be '/'
        """
        if class_name == "/":
            return outer_tag.find_all(type_)
        else:
            return outer_tag.find_all(type_, {"class": class_name})

    def find_tag(self, type_, class_name):
        """
        Find only one specific tag by its class name, the first
        tag that matches will be returned
        Arg: type_: The type of the tag, such as 'a', 'p', 'div' and so on
        Arg: class_name: The class attribute of the tag, if there is no class name,
                         it should be '/'
        """
        if class_name == "/":
            return self._soup.find(type_)
        else:
            return self._soup.find(type_, {"class": class_name})

    def find_tags(self, type_, class_name):
        """
        Fetch informations based on the type of the tag and the class name.
        This method will the Tag objects in BeautifulSoup, if there are
        more than one tag, it will be a list
        Arg: type_: The type of the tag, such as 'a', 'p', 'div' and so on
        Arg: class_name: The class attribute of the tag, if there is no class name,
                         it should be '/'
        """
        if class_name == "/":
            return self._soup.find_all(type_)
        else:
            return self._soup.find_all(type_, {"class": class_name})
