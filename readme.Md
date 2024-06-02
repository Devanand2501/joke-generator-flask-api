# Joke Generator

This is a simple web application that generates jokes based on selected categories and blacklist flags. It uses the JokeAPI to fetch jokes and Flask to serve the web interface, with seamless integration of a REST API.

## Requirements

- Docker
- Web browser

## Installation

1. Clone the repository:

    ```bash
    https://github.com/Devanand2501/joke-generator-flask-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd joke-generator
    ```

3. Build the Docker image:

    ```bash
    docker build -t joke-generator:0.0.1.RELEASE .
    ```

## Usage

1. Run the Docker container:

    ```bash
    docker run -d -p 5000:5000 joke-generator:0.0.1.RELEASE
    ```

2. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

3. Select joke categories, blacklist flags, joke type, and the number of jokes you want.

4. Click on the "Get Joke" button.

5. Enjoy the jokes!

## Seamless Integration of REST API

This project seamlessly integrates a REST API with Flask, allowing you to programmatically access the joke generation functionality. You can send HTTP requests to the Flask server to get jokes in JSON format.

Example:

- **Endpoint**: `http://localhost:5000/`
- **Method**: `POST`
- **Body** (JSON):
  
  ```json
  {
    "category": ["Programming"],
    "blacklist_flags": ["nsfw"],
    "joke_type": "single",
    "num_jokes": 1
  }
  ```

- **Response** (JSON):

  ```json
  {
    "joke": [
      {
        "category": "Programming",
        "type": "single",
        "joke": "Why do programmers prefer dark mode? Less syntax highlighting."
      }
    ]
  }

## Customization

- If you want to modify the categories or blacklist flags, you can do so in the `index.html` file.
- For any changes in the Flask application logic, modify the `main.py` file.
- Additional styling can be done by editing the CSS in the `index.html` file.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Credits

- This project uses the [JokeAPI](https://jokeapi.dev/) to fetch jokes.
- Built with Python Flask.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

