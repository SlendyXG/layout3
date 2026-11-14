import json
import os
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked

BOOKS_PER_PAGE = 10


def render_website():
    with open("meta_data.json", "r", encoding="utf-8") as f:
        books = json.load(f)

    for book in books:
        book["img_src"] = quote(book["img_src"].replace("\\", "/"), safe="/")
        book["book_path"] = quote(book["book_path"].replace("\\", "/"), safe="/")

    pages = list(chunked(books, BOOKS_PER_PAGE))
    total_pages = len(pages)

    os.makedirs("pages", exist_ok=True)

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("template.html")

    for page_number, page_books in enumerate(pages, start=1):
        pairs = list(chunked(page_books, 2))
        html = template.render(
            book_pairs=pairs,
            page_number=page_number,
            total_pages=total_pages,
        )
        with open(f"pages/index{page_number}.html", "w", encoding="utf-8") as f:
            f.write(html)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(
            "<!DOCTYPE html>\n"
            "<html lang=\"ru\">\n"
            "<head>\n"
            "  <meta charset=\"UTF-8\">\n"
            "  <meta http-equiv=\"refresh\" content=\"0; url=pages/index1.html\">\n"
            "  <title>Библиотека Максима</title>\n"
            "</head>\n"
            "<body>\n"
            "  <p><a href=\"pages/index1.html\">Перейти к библиотеке</a></p>\n"
            "</body>\n"
            "</html>\n"
        )

    print(f"Готово: {total_pages} страниц, книг — {len(books)}")


def on_reload():
    render_website()


def main():
    render_website()

    server = Server()
    server.watch("template.html", on_reload)
    server.watch("meta_data.json", on_reload)
    server.serve(root=".", port=5500)


if __name__ == "__main__":
    main()