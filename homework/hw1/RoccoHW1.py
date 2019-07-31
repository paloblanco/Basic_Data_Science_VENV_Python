#%% [markdown]
# # HW 1: Done by Rocco Panella
# I am writing my homeworkd for CMUs data science courses in flat python files. I plan on doing this for two reasons:
# 
# 1. Get used to using a proper text editor for data science work
# 2. I want to use TDD as I do this. I plan on writing a test file for every HW to test all of my funcitons.

#%%
from typing import Union, List, Dict, Any, Tuple


#%%
# Sample function - can I write a test?

def add_args(*args: Union[int, float]) -> Union[int, float]:
    """
    For all added arguments, find the sum
    """
    my_sum = sum(args)
    return my_sum

#%%
# Getting Started Problems

def rotate_list(l: List[Any], n: int) -> List[Any]:
    """
    rotate(l,n) takes a list l and an integer n, and returns a new list with the first n elements moved to the end. 
    Example: rotate([1,2,3,4], 3) -> [4,1,2,3]
    """
    new_beginning = l[n:]
    new_end = l[:n]

    list_solution = new_beginning + new_end
    return list_solution
    

def reverse_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    reverse_dict(d) takes a dictionary d, and 
    returns a new dictionary with the keys and values swapped.
    Assume all values of the given dictionary are unique, 
    i.e. don't worry about conflicting keys. 
    Example: 
    reverse_dict({"apple" : "red", "banana" : "yellow"}) -> {"red" : "apple", "yellow" : "banana"}
    """
    new_dict: Dict[Any, Any] = {}
    for key, val in d.items():
        new_dict[val] = key
    return new_dict


#%%
#========== Scraper Imports
import io, time, json
import requests
from bs4 import BeautifulSoup

#%%
#============ Scraper Problems
def retrieve_html(url: str) -> Tuple[int, str]:
    """
    Return the raw HTML at the specified URL.
    Args:
        url (string): 
    Returns:
        status_code (integer):
        raw_html (string): the raw HTML content of the response, properly encoded according to the HTTP headers.
    """
    response = requests.get(url)
    status_code = response.status_code
    raw_html = response.text
    
    return status_code, raw_html

#%%
#=====================
# get my api key

def read_api_key() -> str:
    """
    Read the Yelp API Key from file.
    Returns:
        api_key (string): The API Key
    """
    with open("private/yelp_key.txt", 'r') as f:
        return f.read().replace('\n','')

def yelp_search(api_key: str, query: str) -> Tuple[int, List[dict]]:
    """
    Make an authenticated request to the Yelp API.
    Args:
        query (string): Search term, such as 'Pittsburgh'. This will be used in 'location'
    Returns:
        num_records (integer): total number of businesses on Yelp corresponding to the query
        businesses (list): list of dicts representing each business
    Notes:
        Realpython has a good article on this: https://realpython.com/python-requests/
    """
    http_address = "https://api.yelp.com/v3/businesses/search"
    params = {"location": query}
    headers = {"Authorization":f"Bearer {api_key}"}
    response = requests.get(http_address, params=params, headers=headers)
    num_records = len(response.json()['businesses'])
    businesses = response.json()['businesses']
    return num_records, businesses




#%%
