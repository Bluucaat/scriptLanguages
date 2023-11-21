import requests
import csv

def download_corpus(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print(f"Failed to download the corpus. Status code: {response.status_code}")
        return []

def find_jsun_words(lines):
    jsun_words = []

    for line in csv.reader(lines):
        word = line[0].lower()  # Convert the word to lowercase for case-insensitive comparison
        if 'jsun' in word:
            jsun_words.append(word)

    return jsun_words

# URL to the corpus file
corpus_url = 'https://raw.githubusercontent.com/jabbalaci/Programozas_1/main/datasets/DT2.csv'

# Download the corpus
corpus = download_corpus(corpus_url)

# Find words with the specified letter order (J, S, U, N)
jsun_words = find_jsun_words(corpus)

# Display the matching words
print(jsun_words)