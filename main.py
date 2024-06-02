from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    joke = None
    error = None
    categories = request.form.getlist('category')
    blacklist_flags = request.form.getlist('blacklist_flags')
    joke_type = request.form.get('joke_type', 'single')
    num_jokes = request.form.get('num_jokes', 1)

    if request.method == 'POST':
        category = ','.join(categories)
        blacklist_flags_str = ','.join(blacklist_flags)
        url = f'https://v2.jokeapi.dev/joke/{category}?blacklistFlags={blacklist_flags_str}&type={joke_type}&amount={num_jokes}'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            data = response.json()
            if 'jokes' in data:
                joke = data['jokes']
            else:
                joke = [data]
        except requests.exceptions.HTTPError as http_err:
            error = f'HTTP error occurred: {http_err}'
        except requests.exceptions.RequestException as req_err:
            error = f'Request error occurred: {req_err}'
        except ValueError as json_err:
            error = f'Error parsing JSON: {json_err}'

    return render_template('index.html', joke=joke, error=error, 
                           categories=categories, blacklist_flags=blacklist_flags, 
                           joke_type=joke_type, num_jokes=num_jokes)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
