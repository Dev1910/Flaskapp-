from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Global variable to store the visit count
visit_count = 0

# Define a route and the corresponding function
@app.route('/')
def hello_world():
    global visit_count
    visit_count += 1
    return f'Hello, World! This page has been visited {visit_count} times.'

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()
