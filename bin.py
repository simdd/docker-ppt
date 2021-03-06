import os
import re
import sys
from flask_cors import CORS
from flask import Flask, jsonify

# parse file
filename = os.path.abspath(sys.argv[1])

with open(filename, 'r', encoding="utf-8") as file:
    text = file.read()


def parseUser(text):
    reCover = r"--cover--(.*)--cover--"
    reTitle = r"title:\s*([^\n\r]*)\n"
    reAuthor = r"author:\s*([^\n\r]*)\n"
    reDate = r"date:\s*([^\n\r]*)\n"

    cover = re.search(reCover, text, re.S).group(1)
    title = re.search(reTitle, cover, re.S).group(1)
    author = re.search(reAuthor, cover, re.S).group(1)
    date = re.search(reDate, cover, re.S).group(1)

    return {'title': title, 'author': author, 'date': date}


def parsePages(text):
    rePages = r"--page--(.*)--page--"
    pages = re.search(rePages, text, re.S).group(1)
    pages = pages.split('\n~\n')
    print(pages)
    return pages


userinfo = parseUser(text)
pages = parsePages(text)


app = Flask(__name__)
CORS(app)


@app.route("/page")
def page():
    return jsonify(pages)


@app.route("/user")
def user():
    return jsonify(userinfo)


def main():
    app.run(host='0.0.0.0', port=4321)


if __name__ == "__main__":
    main()
