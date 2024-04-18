import requests
import csv
import os
import pandas as pd

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
    # Read titles from CSV file
    titles_df = pd.read_csv('clean_titles.csv')  # Adjust filename as needed
    titles = titles_df['name'].tolist()  # Assuming 'Title' is the column name

    english_data = []
    ilocano_data = []
    
    counter=0

    for title in titles:
        counter=counter+1
        eng_title, eng_paragraph = fetch_wikipedia_article("en", title)
        ilo_title, ilo_paragraph = fetch_wikipedia_article("ilo", title)

        print("reading "+str(counter)+" of 1349... ["+title+"]")

        # Check if data exists for both languages
        if eng_title and eng_paragraph and ilo_title and ilo_paragraph:
            english_data.append((eng_title, eng_paragraph))
            ilocano_data.append((ilo_title, ilo_paragraph))
        else:
            print("Missing Wikipedia data available for " + title)

    save_to_csv(english_data, 'english.csv')
    save_to_csv(ilocano_data, 'ilokano.csv')

if __name__ == "__main__":
    main()
