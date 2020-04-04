from app.parse.Parser import Parser

parser = Parser()
with open('../data/sources.json', 'w') as f:
    f.write(parser.json)
