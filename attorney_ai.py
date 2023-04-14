import openai
import os
import requests
import json

# Set OpenAI API key
openai.api_key = "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"

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/quack/Downloads/attorneyai.json"

# Build OpenAI prompt
def build_prompt(question, category):
    return f"Legal Question: {question}\nCategory: {category}\nAnswer:"

# Generate OpenAI response
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

# Get case data from Case.law API
def get_case_data(search_query):
    base_url = "https://api.case.law/v1/cases/"
    api_key = "dd8337713c9dab2581651aeb6b0dce136fd0fb48"
    headers = {"Authorization": f"Token {api_key}"}
    
    params = {
        "search": search_query,
        "full_case": "true",
        "page_size": 10
    }
    
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Get reporter info from Case.law API
def get_reporter_info(reporter_id):
    base_url = f"https://api.case.law/v1/reporters/{reporter_id}/"
    api_key = "dd8337713c9dab2581651aeb6b0dce136fd0fb48"
    headers = {"Authorization": f"Token {api_key}"}
    
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Get API root for custom Django API
def get_api_root():
    base_url = "https://example.com/api/rest/v3/"
    response = requests.options(base_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    # Prompt user for question and category
    question = input("Enter your legal question: ")
    category = input("Enter the category of the question: ")
    prompt = build_prompt(question, category)
    
    # Generate responses using different OpenAI models
    davinci_response = generate_response(prompt, "text-davinci-002")
    curie_response = generate_response(prompt, "text-curie-001")
    babbage_response = generate_response(prompt, "text-babbage-001")
    ada_response = generate_response(prompt, "text-ada-001")
    
    # Print responses from different models
    print("Response from Davinci model: ", davinci_response)
    print("Response from Curie model: ", curie_response)
    print("Response from Babbage model: ", babbage_response)
    print("Response from Ada model: ", ada_response)

    # Get case data and reporter info from Case.law API
    search_query = "example query"


import openai
import os
import requests
import json
from urllib.parse import urlparse

openai.api_key = "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"

def build_prompt(question, category):
    return f"Legal Question: {question}\nCategory: {category}\nAnswer:"

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

def get_case_data(search_query):
    base_url = "https://api.case.law/v1/cases/"
    api_key = "dd8337713c9dab2581651aeb6b0dce136fd0fb48"
    headers = {"Authorization": f"Token {api_key}"}
    
    params = {
        "search": search_query,
        "full_case": "true",
        "page_size": 10
 }
    
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_reporter_info(reporter_id):
    base_url = f"https://api.case.law/v1/reporters/{reporter_id}/"
    api_key = "dd8337713c9dab2581651aeb6b0dce136fd0fb48"
    headers = {"Authorization": f"Token {api_key}"}
    
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_police_reports(search_query):
    base_url = "https://example.com/api/v1/police-reports/"
    api_key = "1234567890abcdefg"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    params = {
        "search": search_query,
        "page_size": 10
 }
    
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    question = input("Enter your legal question: ")
    category = input("Enter the category of the question: ")
    prompt = build_prompt(question, category)
    
    davinci_response = generate_response(prompt, "text-davinci-002")
    curie_response = generate_response(prompt, "text-curie-001")
    babbage_response = generate_response(prompt, "text-babbage-001")
    ada_response = generate_response(prompt, "text-ada-001")
    
    print("Response from Davinci model: ", davinci_response)
    print("Response from Curie model: ", curie_response)
    print("Response from Babbage model: ", babbage_response)
    print("Response from Ada model: ", ada_response)

    search_query = "example query"  # Replace with your desired search query
    case_data = get_case_data(search_query)
    
    if case_data:
        print("\nCase data:")
        for case in case_data["results"]:
            print(f"ID: {case['id']}, Name: {case['name']}, URL: {case['url']}")

import requests
import json

# Set the API key
api_key = "dd8337713c9dab2581651aeb6b0dce136fd0fb48"

# Define the base URL and headers for the API requests
base_url = "https://api.case.law/v1/"
headers = {"Authorization": f"Token {api_key}"}

# Define a function to retrieve case data based on a search query
def search_cases(query):
    params = {"search": query, "page_size": 10, "full_case": True}
    response = requests.get(f"{base_url}cases/", headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Define a function to retrieve reporter data for a given reporter ID
def get_reporter(reporter_id):
    response = requests.get(f"{base_url}reporters/{reporter_id}/", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
search_query = "Fourth Amendment"
case_data = search_cases(search_query)
if case_data:
    for case in case_data["results"]:
        print(f"ID: {case['id']}, Name: {case['name']}")
        reporter_data = get_reporter(case["reporter"])
        if reporter_data:
            print(f"Reporter: {reporter_data['name']}")
        else:
            print("Reporter data not found")
else:
    print("No results found for search query")
