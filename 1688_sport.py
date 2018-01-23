import Crawler
import csv_writer


# An example of using JsSpider to scape a Js rendered page
# Surrounded by try-except
try:
    # Demo url
    url = "https://sport.1688.com"
    js_spider = Crawler.JsSpider(url)
    # Scroll to the bottom the activate js
    js_spider.scroll_bottom()
    # Wait for js to load
    js_spider.wait(4)
    # Start parsing
    js_spider.parse()
    # Find wrapper div
    wrappers = js_spider.find_tags("div", "ch-offer-body")
    # Mapper for csv writing
    mapper = {}
    # For each wrapper div, find:
    # 1. img src
    # 2. title
    # 3. price
    # 4. link to product
    key_index = 0
    for wrap in wrappers:
        inner_map = {}
        # img
        try:
            img = js_spider.find_inner(wrap, "img", "/")['lazy-src']
        except KeyError:
            img = js_spider.find_inner(wrap, "img", "/")['src']
        inner_map["img"] = img
        # link
        link = js_spider.find_inner(wrap, "a", "ch-offer-title ch-offer-title-rowone")
        inner_map["link"] = link['href']
        # title
        title = js_spider.find_inner(wrap, "span", "ch-offer-title-main")
        inner_map["title"] = title.text.strip()
        # price
        sign = js_spider.find_inner(wrap, "span", "ch-offer-price-cny").text
        price = js_spider.find_inner(wrap, "span", "ch-offer-price-many").text.strip()
        inner_map["price"] = (sign + price)
        # Add to mapper
        mapper["id-"+str(key_index)] = inner_map
        key_index += 1
    csv_writer.write_to("Crawler/data.csv", "1688 Sport", mapper)
# If any exceptions occur, quit the spider to release resource
finally:
    # Quit spider, IMPORTANT STEP!
    js_spider.quit_spider()