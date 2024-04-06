import requests
import csv

def fetch_wikipedia_article(language, title):
    url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(url)
    data = response.json()
    if 'extract' in data:
        return data['title'], data['extract']
    else:
        return None, None


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'First Paragraph'])
        for title, paragraph in data:
            writer.writerow([title, paragraph])


def main():
    english_titles = ["Adolf_Hitler", "Winston_Churchill"]
    ilocano_titles = ["Adolf_Hitler", "Winston_Churchill"]

    english_data = []
    ilocano_data = []

    for title in english_titles:
        eng_title, eng_paragraph = fetch_wikipedia_article("en", title)
        if eng_title and eng_paragraph:
            english_data.append((eng_title, eng_paragraph))

    for title in ilocano_titles:
        ilo_title, ilo_paragraph = fetch_wikipedia_article("ilo", title)
        if ilo_title and ilo_paragraph:
            ilocano_data.append((ilo_title, ilo_paragraph))

    save_to_csv(english_data, 'english.csv')
    save_to_csv(ilocano_data, 'ilokano.csv')


if __name__ == "__main__":
    main()
