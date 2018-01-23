import Crawler
import csv_writer


# An example of using static spider to scrape a html page
# Demo url
url = "https://www.yamibuy.com/cn"
static_spider = Crawler.Spider(url)
# Find wrapper div
wrappers = static_spider.find_tags("div", "box-cont")
# mapper for csv writing
mapper = {}
# For each wrapper div, find:
# 1. img src
# 2. title
# 3. price
# 4. link to product
key_index = 0
for wrap in wrappers:
    inner_wraps = static_spider.find_inners(wrap, "div", "sm-box")
    for inner_wrap in inner_wraps:
        inner_map = {}
        # Find informations
        name = static_spider.find_inner(inner_wrap, "p", "des")
        price = static_spider.find_inner(inner_wrap, "p","price")
        link = static_spider.find_inner(inner_wrap, "a", "/")
        img_link = static_spider.find_inner(inner_wrap, "img", "/")
        # Prevent the case that one of the element is missing
        if not(name is None or price is None or link is None or img_link is None):
            inner_map["title"] = name.text
            inner_map["price"] = price.text
            inner_map["img"] = img_link["src"]
            link = link['href'].encode('utf-8').decode('utf-8')
            # Complete the link if it is incomplete
            if not link.startswith("http"):
                link = url + "/" + link
            inner_map["link"] = link
            mapper["id-"+str(key_index)] = inner_map
            key_index += 1

csv_writer.write_to("Crawler/data.csv", "Yamibuy Home", mapper)