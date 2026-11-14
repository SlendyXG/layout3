import json
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    with open("meta_data.json", "r", encoding="utf-8") as f:
        books = json.load(f)

    for book in books:
        book["img_src"] = quote(book["img_src"].replace("\\", "/"), safe="/")

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("template.html")

    html = template.render(books=books)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Готово: index.html, книг — {len(books)}")


if __name__ == "__main__":
    main()