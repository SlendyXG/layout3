# Maxim's Library

A static website that displays a personal book collection. Books are rendered as horizontal Bootstrap cards with covers, titles, authors, genres, and links to the full text. The site is generated from `meta_data.json` and `template.html` by a Python script and published on GitHub Pages.

**Live site:** https://slendyxg.github.io/layout3/

## How to install

Python 3 should be already installed. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

## How to use offline (no Python required)

This is the easiest way to browse the library on your computer — no coding, no installations.

1. Open the repository page on GitHub.
2. Click the green **Code** button and choose **Download ZIP**.
3. Unpack the downloaded archive to any folder.
4. Open the `index.html` file inside the unpacked folder using any modern browser (double-click it, or drag it into a browser window).
5. The first page of the library opens automatically. Use the **Назад** / **Вперёд** buttons at the top to switch between pages.
6. Click **Читать** on any book card to open its text in a new browser tab.

All styles, covers, and book texts are stored locally, so this works without an internet connection.

## How to run

### Build the site

```
python render_website.py
```

The script reads `meta_data.json`, renders `template.html` for each page, and writes `pages/index1.html`, `pages/index2.html`, … (paginated book pages) and `index.html` (a redirect to `pages/index1.html`).

### Preview with auto-reload

```
python render_website.py
```

Then open http://127.0.0.1:5500 in a browser. Any change to `template.html` or `meta_data.json` triggers an automatic rebuild and page reload. Stop the server with `Ctrl+C`.

### Use a custom JSON file

```
python render_website.py --json-path meta_data_v2.json
```

The path can also be set via the `META_DATA_PATH` environment variable:

```
#Linux / macOS
export META_DATA_PATH=meta_data_v2.json
python render_website.py
```

```
#Windows PowerShell
$env:META_DATA_PATH = "meta_data_v2.json"
python render_website.py
```

If neither the CLI option nor the environment variable is provided, `meta_data.json` is used by default.

### Use a `.env` file

For local development it is convenient to keep the path in a `.env` file at the project root:

```
#.env
META_DATA_PATH=meta_data_v2.json
```

Create the file manually (it is not committed to the repository), then run:

```
python render_website.py
```

The script will pick up the value automatically. To switch between datasets, edit `.env` — no code changes required. A `.env.example` file is included as a template.

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).