import requests
import csv
import os
import random

def fetch_wikipedia_article(language, title):
    url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(url)
    data = response.json()
    if 'extract' in data:
        return data['title'], data['extract']
    else:
        return None, None

def search_wikipedia(language, query):
    url = f"https://{language}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srlimit": 1  # Limiting to the first search result
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'query' in data and 'search' in data['query'] and data['query']['search']:
        return data['query']['search'][0]['title']
    else:
        return None

def save_to_csv(data, filename):
    directory = "backend/dataset"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'First Paragraph'])
        for title, paragraph in data:
            writer.writerow([title, paragraph])

def generate_queries(num_queries):
    # List of diverse topics for queries
    titles = [
        "World War II",
        "Ancient civilizations",
        "Jose Rizal",
    ]

    queries = []
    for _ in range(num_queries):
        query = random.choice(titles)
        queries.append(query)
    return queries

def main():
    num_queries = 10  # Number of queries to generate

    # Generate diverse queries for both languages
    english_queries = generate_queries(num_queries)
    ilocano_queries = generate_queries(num_queries)

    english_data = []
    ilocano_data = []

    for eng_query, ilo_query in zip(english_queries, ilocano_queries):
        eng_title = search_wikipedia("en", eng_query)
        ilo_title = search_wikipedia("ilo", ilo_query)
        print("-----------------")
        print("ENGLISH:" +eng_title)
        print("ILOCANO:" +ilo_title)
        print("-----------------")

        if eng_title and ilo_title:
            eng_title, eng_paragraph = fetch_wikipedia_article("en", eng_title)
            ilo_title, ilo_paragraph = fetch_wikipedia_article("ilo", ilo_title)

            # Check if data exists for both languages
            if eng_title and eng_paragraph and ilo_title and ilo_paragraph:
                english_data.append((eng_title, eng_paragraph))
                ilocano_data.append((ilo_title, ilo_paragraph))
            else:
                print("Missing Wikipedia data available for", eng_title, ilo_title)
        else:
            print("No search result available for", eng_query, ilo_query)

    save_to_csv(english_data, 'english.csv')
    save_to_csv(ilocano_data, 'ilocano.csv')

if __name__ == "__main__":
    main()
