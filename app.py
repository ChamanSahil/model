from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder='', template_folder='')

DREAMS = ['India is the best']

@app.route('/')
def build():
    print("\nThe Decision Tree is:")
    return "This is a Python project"
  
