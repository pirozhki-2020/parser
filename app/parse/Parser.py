import csv

from app.line_pipeline.pipelines_functions import *
from app.parse.schemes import ListCocktailSchema


class Parser:
    def __init__(self, source_path='../data/sources.csv', delimiter=','):
        self.source_file = source_path
        self.delimiter = ','
        self.reader = None
        self.file_descriptor = None
        self.schema = None

    def _init_reader(self):
        self.file_descriptor = open(self.source_file, 'r')
        self.reader = csv.DictReader(self.file_descriptor,
                                     delimiter=self.delimiter)

    def _close_reader(self):
        self.file_descriptor.close()

    def _line_pipeline(self, line):
        line = remove_web_scrapper_order(line)
        line = remove_web_scraper_start_url(line)
        line = remove_coctail_preview_href(line)
        line = remove_coctail_preview(line)
        line = format_image_link(line)
        line = make_lists(line)
        return line

    def _parse(self):
        if self.reader is None:
            self._init_reader()
        lines = {'cocktails': [self._line_pipeline(line) for line in \
                               self.reader]}
        self.schema = ListCocktailSchema().load(lines)

    @property
    def json(self):
        if self.schema is None:
            self._parse()
        return json.dumps(self.schema, ensure_ascii=False, indent=4)

    def __del__(self):
        if self.reader:
            self._close_reader()


if __name__ == '__main__':
    parser = Parser()
