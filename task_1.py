class FlatIterator:

    def __init__(self,list_of_list):
        self.list_of_list = list_of_list
        self.end = len(list_of_list)
        self.current = 0
    
    def __iter__(self):
        self.results = iter(self.list_of_list[self.current])
        return self
    
    def _get_item(self):
        try:
            item = next(self.results)
        except StopIteration:
            item = 'end'
        return item
    
    def __next__(self):
        item = self._get_item()
        if item == 'end':
            self.current += 1
            if self.current >= self.end:
                raise StopIteration
            self.results = iter(self.list_of_list[self.current])
            item = self._get_item()
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()