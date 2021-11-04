Alfred Book Search
==================

A book search workflow for [Alfred 4](https://www.alfredapp.com).


Setup
---

Download the latest `.alfredworkflow` file from here and import it to your Alfred.

https://github.com/chroju/alfred-book-search/releases

### Usage

Type `book [keyword]` in your Alfred to search books. Multiple actions can be performed on the selected book by modifier keys.

* Only `Return` : Open the book in hanmoto.com
* `Command + Return` : Open the book in Amazon (default: amazon.co.jp)
* `option + Return` : Open the book in booklog.jp
* `shift + Return` : Copy the book information in reference format

### Variables

| Variable name | Required | Description | Default |
|---|---|---|---|
| AMAZON_DOMAIN | yes | Open the book page from this amazon domain | amazon.co.jp |


Note
---

`icon.png` is by [irasutoya](https://www.irasutoya.com/2013/09/blog-post_6591.html).


LICENSE
---

MIT
