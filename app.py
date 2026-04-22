import os
import re
import markdown
from flask import Flask, render_template, abort, jsonify

app = Flask(__name__)
DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")


def make_title(slug):
    clean = re.sub(r"^\d+-", "", slug)
    return clean.replace("-", " ").replace("_", " ").title()


def get_sections():
    sections = []
    for folder in sorted(os.listdir(DOCS_DIR)):
        folder_path = os.path.join(DOCS_DIR, folder)
        if not os.path.isdir(folder_path):
            continue
        title = make_title(folder)
        docs = []
        for fname in sorted(os.listdir(folder_path)):
            if fname.endswith(".md"):
                slug = fname[:-3]
                docs.append({"slug": slug, "title": make_title(slug)})
        sections.append({"folder": folder, "title": title, "docs": docs})
    return sections


@app.route("/")
def index():
    sections = get_sections()
    return render_template("index.html", sections=sections)


@app.route("/docs/<section>/<slug>")
def doc(section, slug):
    path = os.path.join(DOCS_DIR, section, f"{slug}.md")
    if not os.path.exists(path):
        abort(404)
    with open(path) as f:
        content = f.read()
    html = markdown.markdown(content, extensions=["fenced_code", "tables", "toc"])
    title = slug.replace("-", " ").replace("_", " ").title()
    sections = get_sections()
    return render_template("doc.html", title=title, content=html, sections=sections)


@app.route("/api/mtime")
def mtime():
    mtimes = []
    for folder in os.listdir(DOCS_DIR):
        folder_path = os.path.join(DOCS_DIR, folder)
        if os.path.isdir(folder_path):
            for fname in os.listdir(folder_path):
                if fname.endswith(".md"):
                    mtimes.append(os.path.getmtime(os.path.join(folder_path, fname)))
    return jsonify({"mtime": max(mtimes) if mtimes else 0})


if __name__ == "__main__":
    app.run(debug=True, port=5050)
