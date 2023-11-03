from flask import Flask
vishal = Flask(__name__)

DREAMS = ['India is the best']
print("Setting up things")

@vishal.route('/test')
def build():
    return "This is a python project"
  
@vishal.route('/dreams')
def dreams():
    return DREAMS
  
if __name__ == '__main__':
    vishal.run()
