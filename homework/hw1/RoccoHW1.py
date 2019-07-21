#%% [markdown]
# # HW 1: Done by Rocco Panella
# I am writing my homeworkd for CMUs data science courses in flat python files. I plan on doing this for two reasons:
# 1. Get used to using a proper text editor for data science work
# 2. I want to use TDD as I do this. I plan on writing a test file for every HW to test all of my funcitons.

#%%
# Sample function - can I write a test?

def add_args(*args):
    """
    For all added arguments, find the sum
    """
    my_sum = sum(args)
    return my_sum

#%%
# rotate(l,n) takes a list l and an integer n, and returns a new list with the first n elements moved to the end. 
#
# Example: 
#   rotate([1,2,3,4], 3) -> [4,1,2,3]

def rotate_list(l, n):
    """
    rotate(l,n) takes a list l and an integer n, and returns a new list with the first n elements moved to the end. 
    Example: rotate([1,2,3,4], 3) -> [4,1,2,3]
    """
    new_beginning = l[n:]
    new_end = l[:n]

    list_solution = new_beginning + new_end
    return list_solution
    
# reverse_dict(d) takes a dictionary d, and returns a new dictionary with the keys and values swapped.
# Assume all values of the given dictionary are unique, i.e. don't worry about conflicting keys. 
#
# Example: 
#   reverse_dict({"apple" : "red", "banana" : "yellow"}) -> {"red" : "apple", "yellow" : "banana"}
def reverse_dict(d):
    # Write solution here
    pass


#%%
