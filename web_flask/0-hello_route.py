from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

<<<<<<< HEAD
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

=======
@app.route('/airbnb-onepage/', methods=['GET'])
def hello_route():
    return 'Hello, Airbnb! This is a one-page route.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> d550d3c41699d950daa11a0a78f37fc0729663bf
