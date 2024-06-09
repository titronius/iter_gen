class FlatIterator:

    def __init__(self,list_of_list):
        self.list_of_list = list_of_list
        self.end = len(list_of_list)
        self.current = 0
        self.values_of_list = []
    
    def __iter__(self):
        self.check_list(self.list_of_list[self.current])
        self.results = iter(self.values_of_list)
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
            self.values_of_list = []
            self.check_list(self.list_of_list[self.current])
            self.results = iter(self.values_of_list)
            item = self._get_item()
        return item
    
    def check_list(self,list_to_check):
        if isinstance(list_to_check, list):
            for item in list_to_check:
                self.check_list(item)
        else:
            self.values_of_list.append(list_to_check)

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()