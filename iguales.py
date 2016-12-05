import csv
from collections import Counter


class Repeated:

    def __init__(self, path, *args):
        with open(path) as fh:
            reader = list(csv.DictReader(fh))

            l = [x[k] for x in reader for k in args]




Repeated('prueba.csv', 'id', 'sexo', 'edad')