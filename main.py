import bcrypt
import flask
import os
import requests

from flask import (
    Flask,
    request,
    redirect,
    send_from_directory,
    url_for,
    render_template,
)
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder="frontend/dist/frontend/browser/", static_url_path="")
app.secret_key = "amuncreierAMG"
## https://{POD_ID}-{INTERNAL_PORT}.proxy.runpod.net


endpoint = "https://26m9hkcn3rlli6-8080.proxy.runpod.net"


#################### ####################
@app.route("/test")
def test():
    headers = {
        "Authorization": f"Basic lmzbjal20e7ntc2ajxn2:k71nre59yh2e5oa6c3vw",  # Example, modify as per your server's requirement
    }
    url = f"{endpoint}/test"  # Adjust the endpoint as needed
    try:
        # Send a GET request to the external server
        response = requests.get(url, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Assuming the server returns JSON
        return jsonify(data)  # Return the fetched data to the client
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return an error response
        return jsonify({"error": str(e) + " - " + url}), 500


@app.route("/chroma/query", methods=["POST"])
def chromaque():
    headers = {
        "Authorization": f"Basic lmzbjal20e7ntc2ajxn2:k71nre59yh2e5oa6c3vw",  # Example, modify as per your server's requirement
    }
    url = f"{endpoint}/crud/query"  # Adjust the endpoint as needed
    print(request.json)
    print(request)
    try:
        # Send a GET request to the external server
        external_response = requests.post(
            url,
            json=request.json,  # Forward JSON body if present
            timeout=10,
        )
        external_response.raise_for_status()  # Raise an exception for HTTP errors
        data = external_response.json()  # Assuming the server returns JSON
        return jsonify(data)  # Return the fetched data to the client
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return an error response
        return jsonify({"error": str(e) + " - " + url}), 500


@app.route("/faiss/query", methods=["POST"])
def faissquery():
    headers = {
        "Authorization": f"Basic lmzbjal20e7ntc2ajxn2:k71nre59yh2e5oa6c3vw",  # Example, modify as per your server's requirement
    }
    url = f"{endpoint}/faiss/query"  # Adjust the endpoint as needed
    print(request.json)
    print(request)
    try:
        # Send a GET request to the external server
        external_response = requests.post(
            url,
            json=request.json,  # Forward JSON body if present
            timeout=10,
        )
        external_response.raise_for_status()  # Raise an exception for HTTP errors
        data = external_response.json()  # Assuming the server returns JSON
        return jsonify(data)  # Return the fetched data to the client
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return an error response
        return jsonify({"error": str(e) + " - " + url}), 500


@app.route("/faiss/doctext", methods=["POST"])
def faissqsddsduery():
    headers = {
        "Authorization": f"Basic lmzbjal20e7ntc2ajxn2:k71nre59yh2e5oa6c3vw",  # Example, modify as per your server's requirement
    }
    url = f"{endpoint}/faiss/doctext"  # Adjust the endpoint as needed
    print(request.json)
    print(request)
    try:
        # Send a GET request to the external server
        external_response = requests.post(
            url,
            json=request.json,  # Forward JSON body if present
            timeout=10,
        )
        external_response.raise_for_status()  # Raise an exception for HTTP errors
        data = external_response.json()  # Assuming the server returns JSON
        return jsonify(data)  # Return the fetched data to the client
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return an error response
        return jsonify({"error": str(e) + " - " + url}), 500


@app.route("/translate")
def translate():
    headers = {
        "Authorization": f"Basic lmzbjal20e7ntc2ajxn2:k71nre59yh2e5oa6c3vw",  # Example, modify as per your server's requirement
    }
    url = f"{endpoint}/translate"  # Adjust the endpoint as needed
    try:
        # Send a GET request to the external server
        response = requests.get(url, headers=headers, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Assuming the server returns JSON
        return jsonify(data)  # Return the fetched data to the client
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return an error response
        return jsonify({"error": str(e) + " - " + url}), 500


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
