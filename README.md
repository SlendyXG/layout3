# Maxim's Library

A static website that displays a personal book collection. Books are rendered as horizontal Bootstrap cards with covers, titles, authors, genres, and links to the full text. The site is generated from `meta_data.json` and `template.html` by a Python script and published on GitHub Pages.

**Live site:** https://slendyxg.github.io/layout3/

## How to install

Python 3 should be already installed. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

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

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).