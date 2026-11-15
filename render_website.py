import argparse
import json
import os
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked

BOOKS_PER_PAGE = 10
DEFAULT_JSON_PATH = "meta_data.json"


def render_website(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        books = json.load(f)

    for book in books:
        book["img_src"] = quote(book["img_src"].replace("\\", "/"), safe="/")
        book["book_path"] = quote(book["book_path"].replace("\\", "/"), safe="/")
        book["genres"] = [
            g.strip().rstrip(".")
            for g in book["genres"].split(",")
            if g.strip()
        ]

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
            "  <link rel=\"icon\" href=\"favicon.ico\" type=\"image/x-icon\">\n"
            "  <meta http-equiv=\"refresh\" content=\"0; url=pages/index1.html\">\n"
            "  <title>Библиотека Максима</title>\n"
            "</head>\n"
            "<body>\n"
            "  <p><a href=\"pages/index1.html\">Перейти к библиотеке</a></p>\n"
            "</body>\n"
            "</html>\n"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Generate the book library website from a JSON metadata file."
    )
    parser.add_argument(
        "-j",
        "--json-path",
        default=os.getenv("META_DATA_PATH", DEFAULT_JSON_PATH),
        help="Path to the book metadata JSON (default: %(default)s)",
    )
    args = parser.parse_args()

    json_path = args.json_path

    def on_reload():
        render_website(json_path)

    render_website(json_path)

    server = Server()
    server.watch("template.html", on_reload)
    server.watch(json_path, on_reload)
    server.serve(root=".", port=5500)


if __name__ == "__main__":
    main()