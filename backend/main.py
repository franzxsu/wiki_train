import requests
import csv
import os


def fetch_wikipedia_article(language, title):
    url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(url)
    data = response.json()
    if 'extract' in data:
        return data['title'], data['extract']
    else:
        return None, None


def save_to_csv(data, filename):
    directory = "\dataset"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'First Paragraph'])
        for title, paragraph in data:
            writer.writerow([title, paragraph])


def main():
    num_queries = 10000  # Number of queries to generate

    # List of historical figures for queries
    titles = [
        "Jose_Rizal",
        "Ferdinand_Magellan",
        "Emilio_Aguinaldo",
        "Andres_Bonifacio",
        "Manuel_L._Quezon",
        "Apolinario_Mabini",
        "Juan_Luna",
        "Gregorio_del_Pilar",
        "Lapu-Lapu"
    ]

    # Generate queries for both languages
    english_queries = generate_queries(num_queries, titles)
    ilocano_queries = generate_queries(num_queries, titles)

    english_data = []
    ilocano_data = []

    for eng_title, ilo_title in zip(english_queries, ilocano_queries):
        eng_title, eng_paragraph = fetch_wikipedia_article("en", eng_title)
        ilo_title, ilo_paragraph = fetch_wikipedia_article("ilo", ilo_title)

        # Check if data exists for both languages
        if eng_title and eng_paragraph and ilo_title and ilo_paragraph:
            english_data.append((eng_title, eng_paragraph))
            ilocano_data.append((ilo_title, ilo_paragraph))
        else:
            print("Missing Wikipedia data available for", eng_title, ilo_title)

    save_to_csv(english_data, 'english.csv')
    save_to_csv(ilocano_data, 'ilocano.csv')

def generate_queries(num_queries, titles):
    queries = []
    for _ in range(num_queries):
        query = random.choice(titles)
        queries.append(query)
    return queries

if __name__ == "__main__":
    main()
