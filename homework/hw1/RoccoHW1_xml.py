#%% [markdown]
# # HW1 Part 2, XML parsing


#%%
from typing import Union, List, Dict, Any, Tuple

#%%
# make some basic compiled regular expressions. 
# I will test these in my test file
import re
import requests
course_webpage = str(requests.get("http://www.datasciencecourse.org/2016").content)

"""CHECK https://regex101.com/"""
# tag_open: re.Pattern = re.compile(r"<(\w+)(\s?\w*=?\S*?)>")
tag_open: re.Pattern = re.compile(r"<(\w+)( *[\W\S]*?)>")
tag_close: re.Pattern = re.compile(r"<\/(\w+)( *[\W\S]*?)>")
tag_open_close: re.Pattern = re.compile(r"<(\w+)([^>]*)\/>")

comment: re.Pattern = re.compile(r"<!--([\s\S]*?)-->")
xml_prolog: re.Pattern = re.compile(r"<\?([\s\S]*?)\?>")
html_prolog: re.Pattern = re.compile(r"<!(DOC[\w\s]*?)>")

#%%
#### Q2: fill in this cell

class XMLNode:
    
    def __init__(self, tag, attributes, content):
        self.tag = tag
        self.attributes = attributes
        self.children =  []
        self.content = content