from flask import Flask, request, render_template, jsonify
vishal = Flask(__name__)
vishal.debug = True

DREAMS = ['India is the best']
print("Setting up things")

@vishal.route('/test')
def build():
    print("\nThe Decision Tree is:")
    return "This is a python project"
  
@vishal.route('/dreams')
def dreams():
    # Return the list of remembered dreams. 
    return jsonify(DREAMS)
  
if __name__ == '__main__':
    vishal.run()
