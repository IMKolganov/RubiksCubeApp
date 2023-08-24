from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from RubiksCube import RubiksCube

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    # Пример использования:
    cube = RubiksCube()
    print("Initial State:")
    cube.display()
    print("\nAfter Rotating Front Face:")
    cube.rotate()
    cube.display()
    return "Hello, World!"



if __name__ == '__main__':
    app.run(debug=True)


