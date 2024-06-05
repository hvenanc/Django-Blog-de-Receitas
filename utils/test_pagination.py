from unittest import TestCase
from utils.pagination import make_pagination_range

class PaginationTest(TestCase):


    def test_make_pagination_range_returns_pagination_range(self):
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            number_pages = 4,
            current_page=1
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

    
    def test_current_range_select_page(self):
        # Current page = 1 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            number_pages = 4,
            current_page=1
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

        # Current page = 2 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            number_pages = 4,
            current_page=2
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)
        
        # Current page = 3 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            number_pages = 4,
            current_page=3
        )['pagination']
        self.assertEqual([2,3,4,5], pagination)

        # Current page = 4 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            number_pages=4,
            current_page=4,
        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)

    
    def test_make_pagination_range_is_static_when_last_page_is_next(self):

        # Current page = 18 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            number_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Current page = 19 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            number_pages=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Current page = 20 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            number_pages=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Current page = 21 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            number_pages=4,
            current_page=21,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)