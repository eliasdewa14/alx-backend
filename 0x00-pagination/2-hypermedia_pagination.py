#!/usr/bin/env python3
"""Define a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10."""

from typing import Tuple, List
import csv
import math


index_range = __import__("0-simple_helper_function").index_range


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
        """ return the appropriate page of the dataset """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """  returns a dictionary containing key-value pairs """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        total_pages = math.floor(len(self.dataset()) / page_size)
        next_page = (page + 1) if (page + 1) < total_pages else None
        prev_page = (page - 1) if page > 1 else None
        
        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
