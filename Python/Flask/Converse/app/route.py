from flask import current_app as app


@app.route("/")
def main():
    return "haha"


@app.route("/product")
def product():
    return "haha"


@app.route("/account")
def account():
    return "haha"
