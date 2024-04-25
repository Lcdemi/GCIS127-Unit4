import sorts

def test_shift_no_shift():
    #setup
    a_list = [1, 2, 3, 4, 5]
    index = 3
    expected = [1, 2, 3, 4, 5]

    #invoke
    sorts.shift(a_list, index)

    #analyze
    assert expected == a_list

def test_shift_2():
    #setup
    a_list = [1, 3, 4, 2, 5]
    index = 3
    expected = [1, 2, 3, 4, 5]

    #invoke
    sorts.shift(a_list, index)

    #analyze
    assert expected == a_list

def test_shift_all():
    #setup
    a_list = [2, 3, 4, 5, 1]
    index = 4
    expected = [1, 2, 3, 4, 5]

    #invoke
    sorts.shift(a_list, index)

    #analyze
    assert expected == a_list

def test_insertion_sort_arbitrary():
    #setup
    a_list = [2, 1, 5, 7, 8, 3, 4, 10, 9, 6, 2]
    expected = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #invoke
    sorts.insertion_sort(a_list)

    #analyze
    assert expected == a_list

def test_insertion_sort_sorted():
    #setup
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #invoke
    sorts.insertion_sort(a_list)

    #analyze
    assert expected == a_list

def test_insertion_sort_reverse():
    #setup
    a_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #invoke
    sorts.insertion_sort(a_list)

    #analyze
    assert expected == a_list

def test_split_even():
    #setup
    a_list = [1, 2, 5, 7]
    expected_left = [1, 2]
    expected_right = [5, 7]

    #invoke
    actual_left, actual_right = sorts.split(a_list)

    #analyze
    assert expected_left == actual_left
    assert expected_right == actual_right

def test_split_odd():
    #setup
    a_list = [1, 2, 5, 7, 9]
    expected_left = [1, 2]
    expected_right = [5, 7, 9]

    #invoke
    actual_left, actual_right = sorts.split(a_list)

    #analyze
    assert expected_left == actual_left
    assert expected_right == actual_right

def test_merge():
    #setup
    a_list = [1, 3, 5, 7]
    b_list = [2, 4, 6, 8, 10]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 10]

    #invoke
    actual = sorts.merge(a_list, b_list)

    #analyze
    assert expected == actual

def test_merge_sort_1():
    #setup
    a_list = [5]
    expected = a_list

    #invoke
    actual = sorts.merge_sort(a_list)

    #analyze
    assert expected is actual

def test_merge_sort_10():
    #setup
    a_list = [5, 3, 7, 8, 10, 1, 2, 6, 4, 9]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #invoke
    actual = sorts.merge_sort(a_list)

    #analyze
    assert expected == actual

def test_partition():
    #setup
    a_list = [5, 9, 2, 8, 4, 3, 5, 1, 8]
    pivot = 5
    expected_less = [2, 4, 3, 1]
    expected_same = [5, 5]
    expected_more = [9, 8, 8]

    #invoke
    less, same, more = sorts.partition(a_list, pivot)

    #analyze
    assert expected_less == less
    assert expected_more == more
    assert expected_same == same

def test_partition_less():
    #setup
    a_list = [5, 1, 2, 4, 4, 3, 5, 1, 2]
    pivot = 5
    expected_less = [1, 2, 4, 4, 3, 1, 2]
    expected_same = [5, 5]
    expected_more = []

    #invoke
    less, same, more = sorts.partition(a_list, pivot)

    #analyze
    assert expected_less == less
    assert expected_more == more
    assert expected_same == same

def test_partition_more():
    #setup
    a_list = [5, 6, 9, 10, 7, 5, 8, 9, 8]
    pivot = 5
    expected_less = []
    expected_same = [5, 5]
    expected_more = [6, 9, 10, 7, 8, 9, 8]

    #invoke
    less, same, more = sorts.partition(a_list, pivot)

    #analyze
    assert expected_less == less
    assert expected_more == more
    assert expected_same == same

def test_quicksort_1():
    #setup
    a = [2]
    expected = a

    #invoke
    actual = sorts.quicksort(a)

    #analyze
    assert expected is actual

def test_quicksort_10():
    #setup
    a_list = [5, 3, 7, 8, 10, 1, 2, 6, 4, 9]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #invoke
    actual = sorts.quicksort(a_list)

    #analyze
    assert expected == actual