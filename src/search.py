import json
import sys
from google_books_api import GoogleBooksAPI


def convert_book_info_to_alfred_json(book_info):
    result = {"items": []}
    for v in book_info['items']:
        info = v["volumeInfo"]
        ids = info.get("industryIdentifiers")
        if ids == None or 'ISBN_10' not in [i["type"] for i in ids]:
            continue
        isbn = [i["identifier"] for i in ids if 'ISBN_10' in i['type']][0]

        item = {}
        item["uid"] = isbn
        item["title"] = info["title"]

        publisher = info.get('publisher', '-')
        date = info["publishedDate"]
        authors = info.get("authors")
        if authors:
            authors_str = ", ".join(authors)
        else:
            authors_str = "-"

        item["subtitle"] = f"{authors_str} / {publisher} / {date} / {isbn}"

        item["arg"] = isbn
        item["autocomplete"] = info["title"]
        result["items"].append(item)
    return json.dumps(result, indent=2, ensure_ascii=False)


def main():
    args = sys.argv
    query = args[1]

    google_books = GoogleBooksAPI()
    res = google_books.search(query)

    return convert_book_info_to_alfred_json(res.json())


if __name__ == '__main__':
    print(main())
