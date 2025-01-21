import csv, os, json

def main():
    path = os.path.join(os.path.dirname(__file__), '../data/taylor_swift_filtered_articles_500_oct_nov.csv')
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        coding_index = header.index("3rd coding")

        coding= {}
        coding["1"] = 0
        coding["2"] = 0
        coding["3"] = 0
        coding["4"] = 0
        coding["5"] = 0
        coding["6"] = 0

        for row in reader:
            coding[row[coding_index]] += 1

        # calculate percentages and round to 2 decimal places and show the number of articles
        for key in coding:
            number_of_articles = coding[key]
            coding[key] = round(coding[key] / 500 * 100, 2)
            coding[key] = str(coding[key]) + " (" + str(number_of_articles) + ")"

        # write to json
        with open('coding_percentage.json', 'w') as file:
            json.dump(coding, file, indent=2)

if __name__ == '__main__':
    main()