import json
import os
import csv
import math

def main():
    # Load up the file which is in the data folder
    path = os.path.join(os.path.dirname(__file__), '../data/taylor_swift_filtered_articles_500_oct_nov.csv')
    
    # Open the file
    with open(path, 'r', encoding='utf-8') as csvfile:
        tfidf_scores = calculate_tfidf(csvfile)

    # Write the results to a JSON file
    with open('tfidf_scores.json', 'w') as file:
        json.dump(tfidf_scores, file, indent=2)
       

def calculate_tfidf(csvfile):
    reader = csv.reader(csvfile)
    
    # Get the header
    header = next(reader)
    title_index = header.index("Title")
    description_index = header.index("Description")
    category_index = header.index("3rd coding")

    # Load the stopwords
    stopwords = load_stopwords()

    # Store document-wise word counts and categories
    words_by_row = {}
    i = 0

    # Iterate through rows in the CSV file
    for row in reader:
        title_description = f"{row[title_index]} {row[description_index]}".lower()
        category = int(row[category_index])

        # Clean the text
        text = clean_text(title_description, stopwords).split()

        # Count word occurrences in the document
        word_counts = {}
        for word in text:
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1

        # Store the word counts and category for this document
        words_by_row[i] = (word_counts, category)
        i += 1

    words_by_category = {}

    for row in words_by_row:
        category = words_by_row[row][1]

        words = words_by_row[row][0]

        for word in words:
            tf = words[word]

            idf = math.log(len(words_by_row) / sum(1 for r in words_by_row if word in words_by_row[r][0]))

            tfidf = tf * idf
            if category not in words_by_category:
                words_by_category[category] = {}
            if word not in words_by_category[category]:
                words_by_category[category][word] = 0
            words_by_category[category][word] += tfidf

    # Sort words by TF-IDF score in descending order
    for category in words_by_category:
        words_by_category[category] = sorted(words_by_category[category].items(), key=lambda x: x[1], reverse=True)

    # Select the top 10 wrods for each category and round the TF-IDF scores and sort the categories by category ID
    top_words_by_category = {}
    for category in sorted(words_by_category.keys()):
        top_words_by_category[category] = [(word, round(tfidf, 2)) for word, tfidf in words_by_category[category][:10]]

    return top_words_by_category

def load_stopwords():
    # Load the stopwords
    stopwords_path = os.path.join(os.path.dirname(__file__), '../data/stopwords.txt')
    stopwords = set()
    with open(stopwords_path, 'r', encoding='utf-8') as stopwords_file:
        for line in stopwords_file:
            stopwords.add(line.strip())
    return stopwords

def clean_text(text, stopwords):
    punctuation = '()[],-.?!:;#&'

    # Remove punctuation
    for char in punctuation:
        text = text.replace(char, ' ')

    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stopwords])

    # Remove non-alphabetic words
    text = ' '.join([word for word in text.split() if word.isalpha()])

    return text

if __name__ == "__main__":
    main()
