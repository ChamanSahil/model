from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
app.debug = True

DREAMS = ['India is the best']
print("Setting up things")

@app.route('/test')
def build():
    print("\nThe Decision Tree is:")
    return "This is a python project"
  
@app.route('/dreams')
def dreams():
    # Return the list of remembered dreams. 
    return jsonify(DREAMS)
  
if __name__ == '__main__':
    app.run()
