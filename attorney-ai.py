import openai
import requests
import webbrowser
import json
import os
from requests_cache import CachedSession

# Set OpenAI API key
openai.api_key = "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"

# Set up caching
cache_name = "legal_nlp_cache"
cache_expire_after = 3600  # in seconds
session = CachedSession(cache_name=cache_name, expire_after=cache_expire_after)

# Define function to generate response using GPT-4 model
def generate_response(prompt, engine):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].text.strip()

# Define function to search the web and return relevant links
def search_web(query):
    headers = {"x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
               "x-rapidapi-host": "contextualwebsearch-websearch-v1.p.rapidapi.com"}
    params = {"q": query, "pageNumber": "1", "pageSize": "3", "autoCorrect": "true"}
    response = session.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI", headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        links = []
        for result in data["value"]:
            links.append(result["url"])
        return links
    else:
        return None

# Define function to search Maricopa County Superior Court website
def search_law_library(query):
    base_url = "https://www.maricopacountysuperiorcourt.gov/LawLibrary/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}

    # Get the search page and extract the "view state" value
    search_url = base_url + "LawLibrarySearch.aspx"
    response = session.get(search_url, headers=headers)
    view_state = response.text.split('id="__VIEWSTATE" value="')[1].split('"')[0]

    # Post the search query and extract the results page
    data = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": view_state,
        "ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolderRight$Search1$tbSearchText": query,
        "ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolderRight$Search1$btnSearch": "Search",
        "ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolderRight$Search1$ddlSearchTypes": "AllWords"
    }
    response = session.post(search_url, headers=headers, data=data)
    results_page = response.text

    # Extract the links to the search results
    links = []
    for line in results_page.split('\n'):
        if '<a id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderRight_Search1_dlSearchResults_hlDocLink' in line:
            url = base_url + line.split('href="')[1].split('"')[0]
            links.append(url)
    return links


