import json
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def render_website():
    with open("meta_data.json", "r", encoding="utf-8") as f:
        books = json.load(f)

    for book in books:
        book["img_src"] = quote(book["img_src"].replace("\\", "/"), safe="/")

    book_pairs = list(chunked(books, 2))

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("template.html")

    html = template.render(book_pairs=book_pairs)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Готово: index.html, книг — {len(books)}")


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