from flask import Flask, render_template
import os, json

app = Flask(__name__)

@app.route('/items')
def items():
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(json_path, 'r') as f:
        data = json.load(f)
    return render_template('items.html', items=data.get('items', []))

if __name__ == '__main__':
    app.run(debug=True, port=5000)