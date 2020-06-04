from flask import Flask, request

app = Flask(__name__)
app.secret_key = b"aslkdcpounqg-_C;lalm2308u2r"
# api = Api(app)


@app.route("/")
def index():
    if request.method == "GET":
        return "it's get!"
    return "it's post!"


@app.route("/info")
def info():
    return "info.html"


@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post %d" % post_id


if __name__ == "__main__":
    app.run(debug=True)
