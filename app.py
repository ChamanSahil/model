from flask import Flask, request, render_template, jsonify
app = Flask(__name)

DREAMS = ['India is the best']
print("Setting up things")

@app.route('/')
def build():
    print("\nThe Decision Tree is:")
    return "This is a python project"
  
@app.route('/dreams', methods=['GET', 'POST'])
def dreams():
    """Simple API endpoint for dreams. 
    In memory, ephemeral, like real dreams.
    """
  
    # Add a dream to the in-memory database, if given. 
    if 'dream' in request.args:
        DREAMS.append(request.args['dream'])
    
    # Return the list of remembered dreams. 
    return jsonify(DREAMS)
  
if __name__ == '__main__':
    app.run()
