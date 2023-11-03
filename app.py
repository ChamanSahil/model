from flask import Flask
app = Flask(__name__)

DREAMS = ['I am going to win this event nad prove myself']

@app.route('/')
def build():
    if response.status_code == 200:
        labels = response.text.split('\n')
        print(labels)
        res = processImage(
            "https://versatilevats.com/squarehub/glitch/chamanrock145-Lawnmover.jpeg",
            labels
        )
        return res
    else:
        print("Error while fetching the labels")
        return "Error while fetching the labels"
  
@app.route('/dreams')
def dreams():
    return DREAMS
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
