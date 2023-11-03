from flask import Flask
app = Flask(__name__)

DREAMS = ['India is the best']
print("Setting up things")

@app.route('/')
def build():
    return "This is a python project"
  
@app.route('/dreams')
def dreams():
    return DREAMS
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
