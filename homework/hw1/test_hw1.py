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

def test_yelp_api_key():
    test_str = RoccoHW1.read_api_key()

    assert isinstance(test_str, str)

def test_yelp_api():
    api_key = RoccoHW1.read_api_key()
    num_records, data = RoccoHW1.yelp_search(api_key, "Pittsburgh")

    assert isinstance(num_records, int)
    assert num_records > 1000
    assert isinstance(data, list)
    return    

def test_yelp_restaurants():
    api_key = RoccoHW1.read_api_key()
    num_records, data = RoccoHW1.yelp_search_restaurants(api_key, "Squirrel Hill, Pittsburgh")

    assert isinstance(num_records, int)
    assert num_records > 10
    assert isinstance(data, list)
    return    

def test_parse_api_response():
    test_string = """
            {
        "total": 8228,
        "businesses": [
            {
            "rating": 4,
            "price": "$",
            "phone": "+14152520800",
            "id": "four-barrel-coffee-san-francisco",
            "is_closed": false,
            "categories": [
                {
                "alias": "coffee",
                "title": "Coffee & Tea"
                }
            ],
            "review_count": 1738,
            "name": "Four Barrel Coffee",
            "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
            "coordinates": {
                "latitude": 37.7670169511878,
                "longitude": -122.42184275
            },
            "image_url": "http://s3-media2.fl.yelpcdn.com/bphoto/MmgtASP3l_t4tPCL1iAsCg/o.jpg",
            "location": {
                "city": "San Francisco",
                "country": "US",
                "address2": "",
                "address3": "",
                "state": "CA",
                "address1": "375 Valencia St",
                "zip_code": "94103"
            },
            "distance": 1604.23,
            "transactions": ["pickup", "delivery"]
            }
        ],
        "region": {
            "center": {
            "latitude": 37.767413217936834,
            "longitude": -122.42820739746094
            }
        }
        }"""
    list_urls = RoccoHW1.parse_api_response(test_string)

    assert isinstance(list_urls, list)
    for each in list_urls:
        assert isinstance(each, str)
        assert "https" in each

def test_parse_page():
    test_url = 'https://www.yelp.com/biz/pigeon-bagels-pittsburgh?adjust_creative=lYR2VjM0WMaytcyfk5_frA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=lYR2VjM0WMaytcyfk5_frA'
    list_reviews, url_next = RoccoHW1.parse_page(test_url)

    assert isinstance(list_reviews, list)
    assert isinstance(url_next, str) or url_next is None
    