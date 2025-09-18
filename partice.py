import csv

file_path = "hacker_news.csv"

def findpython():
    count = 0
    with open(file_path, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row.get("title")  
            if title and "python" in title.lower():
                count += 1
                print(f"{count}. {title}")
    print("Total Python titles:", count)


def findamazon():
    count = 0
    with open(file_path, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            url = row.get("url")
            title = row.get("title")
            if url and "amazon" in url.lower():
                count += 1
                print(f"{count}. {title} --> {url}")
    print("Total Amazon URLs:", count)


choice = int(input("1. Find 'amazon' in url\n2. Find 'python' in title\n-----> "))

if choice == 1:
    findamazon()
elif choice == 2:
    findpython()
else:
    print("Invalid input, please use correct option")
