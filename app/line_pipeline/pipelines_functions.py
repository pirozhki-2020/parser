from typing import OrderedDict
import re
import json


def remove_web_scrapper_order(line: OrderedDict):
    line.pop('\ufeffweb-scraper-order')
    return line


def remove_web_scraper_start_url(line: OrderedDict):
    line.pop('web-scraper-start-url')
    return line


def remove_coctail_preview(line: OrderedDict):
    line.pop('coctail-preview')
    return line


def remove_coctail_preview_href(line: OrderedDict):
    line.pop('coctail-preview-href')
    return line


def format_image_link(line: OrderedDict):
    image_pattern = re.compile(r'.*"(?P<link>.*)".*')
    image: str = line.pop('image')
    res = image_pattern.search(image)
    link = res.group('link')
    line.update({'image': link})
    return line


def make_lists(line: OrderedDict):
    line['ingredient'] = json.loads(line['ingredient'])
    line['recipe-steps'] = json.loads(line['recipe-steps'])
    line['tool-amount'] = json.loads(line['tool-amount'])
    line['ingredient amount'] = json.loads(line['ingredient amount'])
    line['tool'] = json.loads(line['tool'])
    return line
