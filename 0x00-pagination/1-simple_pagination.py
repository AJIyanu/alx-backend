#!/usr/bin/env python3
"""Now i have you documented"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple of size two containing"""
    if page <= 0:
        return (0, 0)
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets page implemented by me"""
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        therange = index_range(page, page_size)
        setdata = self.dataset()
        try:
            dataset = [setdata[row] for row in range(therange[0], therange[1])]
            return dataset
        except IndexError:
            return []
