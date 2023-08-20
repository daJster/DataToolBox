from flask import Flask, render_template
import ds.data as data
import ds.log  as log


app = Flask(__name__, static_folder='static', template_folder='static')

@app.route('/')
def index():
    return render_template('UI/index.html')

if __name__ == '__main__':
    app.run(debug=True)