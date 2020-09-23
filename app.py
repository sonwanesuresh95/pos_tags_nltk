from flask import Flask, request, render_template
from generate_tags import generate_tags

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


@app.route('/pos_tag', methods=['GET', 'POST'])
def pos_tags():
    data = request.form['text']
    response = generate_tags(data)
    return render_template('index.html',data=data, response=response)


if __name__ == '__main__':
    app.run()