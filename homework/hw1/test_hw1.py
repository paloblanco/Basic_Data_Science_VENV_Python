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
    test_result = RoccoHW1.rotate_list(test_list, test_num)
    assert isinstance(test_result, list)
    for i,j in zip(test_result, [4,1,2,3]):
        assert i == j
    return


def test_reverse_dict():
    """
    Should Reverse the order of a provided dict. should not be expected to handle duplicates
    """
    test_dict = {"apple" : "red", "banana" : "yellow"}
    expected_result = {"red" : "apple", "yellow" : "banana"}
    test_result = RoccoHW1.reverse_dict(test_dict)

    assert isinstance(test_result, dict)
    for key, val in expected_result.items():
        assert val == test_result.get(key)
    return

def test_retrieve_html():
    """
    Return the raw HTML at the specified URL.
    Args:
        url (string): 
    Returns:
        status_code (integer):
        raw_html (string): the raw HTML content of the response, properly encoded according to the HTTP headers.
    """
    test_url = 'http://www.nytimes.com/2016/08/28/magazine/inside-facebooks-totally-insane-unintentionally-gigantic-hyperpartisan-political-media-machine.html'
    desired_code = 200
    desired_html = u'<!DOCTYPE html>\n<!--[if (gt IE 9)|!(IE)]> <!--> <html lang="en" class="no-js section-magazine...'

    test_code, test_html = RoccoHW1.retrieve_html(test_url)

    assert isinstance(test_code, int)
    assert isinstance(test_html, str) # this is adequate to know we are returning html
    assert test_code == desired_code
    # assert test_html[:20] == desired_html[:20]
    return
