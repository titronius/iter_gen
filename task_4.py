import types

def flat_generator(list_of_lists):
    cursor = 0
    end = len(list_of_lists)
    
    global values_of_list
    values_of_list = []
    
    while cursor < end:
        results = list_of_lists[cursor]
        cursor += 1
        check_list(results)
    
    for item in values_of_list:
        yield item
            
def check_list(list_to_check):
    if isinstance(list_to_check, list):
        for item in list_to_check:
            check_list(item)
    else:
        values_of_list.append(list_to_check)

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()