from flask import Flask

# Initialize the Flask app
app = Flask(__name__)  # Fixes: `flask` -> `Flask`, `_name_` -> `__name__`

# Define a route for the homepage
@app.route('/')
def home():
    return 'Hello, Flask!'  # Fixes: added a comma for consistency

# Run the app
if __name__ == '__main__':  # Fixes: `name` -> `__name__`, `'_main_'` -> `'__main__'`
    app.run(debug=True)
