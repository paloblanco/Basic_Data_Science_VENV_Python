#%% [markdown]
# # Data Gathering and Scraping
# THese are my interactive notes on gathering and scrpaing data

#%%
import requests

#%%
response = requests.get("http://www.cmu.edu")

print("Status Code: " + str(response.status_code))
print("Headers: " + str(response.headers))

#%%
print(response.text[:400])


#%%
# passing parameters as a dictionary. I believe you need to know these ahead of time.
params = {"query": "python download url content", "source":"chrome"}
response = requests.get("http://www.google.com/search", params=params)
print(response.status_code)

#%%
