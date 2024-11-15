import bcrypt
import flask
import os
from flask import (
    Flask,
    request,
    redirect,
    send_from_directory,
    url_for,
    render_template,
)

from flask_cors import CORS

app = Flask(__name__, static_folder="frontend/dist/frontend/browser/", static_url_path="")
app.secret_key = "amuncreierAMG"

__angular_paths = []
__angular_default_path = "index.html"
__root = app.static_folder


@app.errorhandler(404)
def not_found_error(error):
    return send_from_directory(__root, "index.html")


print("Running @ ", __root)

for root, subdirs, files in os.walk(__root):
    if len(root) > len(__root):
        root += "/"

    for file in files:
        relativePath = str.replace(root + file, __root, "")
        __angular_paths.append(relativePath)
    print("Angular paths: [ ", __angular_paths, " ]")


# Special trick to capture all remaining routes
@app.route("/<path:path>")
@app.route("/", defaults={"path": ""})
def angular(path):
    if path not in __angular_paths:
        path = __angular_default_path
    return send_from_directory(__root, path)


xcors = CORS(
    app,
)

# testing
if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Running the app in debug mode
