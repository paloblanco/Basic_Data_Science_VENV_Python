import RoccoHW1

def test_add_args():
    assert RoccoHW1.add_args(1,2,3) == 6
    return

def test_rotate_list():
    """
    rotate(l,n) takes a list l and an integer n, and returns a new list with the first n elements moved to the end. 
    Example: rotate([1,2,3,4], 3) -> [4,1,2,3]
    """
    test_list = [1,2,3,4]
    test_num = 3
    for i,j in zip(RoccoHW1.rotate_list(test_list, test_num), [4,1,2,3]):
        assert i == j
    return