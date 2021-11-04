import json
import sys
from openbd_api import OpenBDAPI
from google_books_api import GoogleBooksAPI


def get_reference_format(book_info):
    if type(book_info) is dict:
        items = _get_items_from_google(book_info)
    else:
        items = _get_items_from_hanmoto(book_info)

    return f"{items['authors']}{items['translators']}. {items['title']}. {items['version']}{items['publisher']}, {items['pub_year']}, {items['pages']}p."


def _get_items_from_google(book_info):
    book = book_info['items'][0]

    title = book['volumeInfo']['title']
    pages = book['volumeInfo']['pageCount']
    publisher = book['volumeInfo']['publisher']
    pub_year = book['volumeInfo']['publishedDate'][0:4]
    authors = ', '.join(book['volumeInfo']['authors'])

    return {
        'title': title,
        'pages': pages,
        'publisher': publisher,
        'pub_year': pub_year,
        'authors': authors,
        'translators': '',
        'version': ''
    }


def _get_items_from_hanmoto(book_info):
    book_onix = book_info[0]['onix']
    book_hanmoto = book_info[0]['hanmoto']

    title = book_onix['DescriptiveDetail']['TitleDetail']['TitleElement']['TitleText']['content']
    part = book_onix['DescriptiveDetail']['TitleDetail']['TitleElement'].get(
        'PartNumber')
    if part:
        title = f"{title} {part}"

    pages = book_onix['DescriptiveDetail']['Extent'][0]['ExtentValue']
    publisher = book_onix['PublishingDetail']['Imprint']['ImprintName']

    pub_dates = book_onix['PublishingDetail'].get('PublishingDate')
    pub_date = [i['Date']
                for i in pub_dates if i['PublishingDateRole'] == '01'][0]
    if not pub_date:
        pub_date = book_hanmoto.get('dateshuppan')
    pub_year = pub_date[0:4]

    contributors = book_onix['DescriptiveDetail']['Contributor']

    authors = [i['PersonName']['content']
               for i in contributors if 'A01' in i['ContributorRole']]
    authors_str = ', '.join(authors)

    translators = [i['PersonName']['content']
                   for i in contributors if 'B06' in i['ContributorRole']]
    translators_str = ', '.join(translators)
    if translators_str:
        translators_str = f" ({translators_str} 訳) "

    version = book_hanmoto.get('han')
    if version == '1' or version == None:
        version = ''
    else:
        version = f"{version}版, "

    return {
        'title': title,
        'pages': pages,
        'publisher': publisher,
        'pub_year': pub_year,
        'authors': authors_str,
        'translators': translators_str,
        'version': version
    }


def main():
    args = sys.argv
    isbn = args[1]

    openbd = OpenBDAPI()
    res = openbd.get(isbn)

    if res.json()[0]:
        return get_reference_format(res.json())

    google_books = GoogleBooksAPI()
    res = google_books.search(f"isbn{isbn}")

    return get_reference_format(res.json())


if __name__ == '__main__':
    print(main(), end='')
