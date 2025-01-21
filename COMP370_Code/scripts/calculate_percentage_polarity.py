import csv, os, json

def main():
    path = os.path.join(os.path.dirname(__file__), '../data/taylor_swift_filtered_articles_500_oct_nov.csv')
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        polarity_index = header.index("polarity")

        polarity = {}
        # we have positive, negative, neutral
        polarity["positive"] = 0
        polarity["negative"] = 0
        polarity["neutral"] = 0

        for row in reader:
            polarity[row[polarity_index]] += 1

        # calculate percentages
        total = polarity["positive"] + polarity["negative"] + polarity["neutral"]
        polarity["positive"] = polarity["positive"] / total
        polarity["negative"] = polarity["negative"] / total
        polarity["neutral"] = polarity["neutral"] / total

        # write to json
        with open('polarity.json', 'w') as file:
            json.dump(polarity, file, indent=2)

if __name__ == '__main__':
    main()