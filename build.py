import os
from flask import Flask
from flask_frozen import Freezer
from app import app

# Create public directory if it doesn't exist
if not os.path.exists('public'):
    os.makedirs('public')

freezer = Freezer(app)

if __name__ == '__main__':
    # Generate static files
    freezer.freeze() 