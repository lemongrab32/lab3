from flask import Flask, render_template, request
from calc import calc

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        currency = request.form.get('list')
        value = request.form.get('value')
        desired = request.form.get('desired')
        print(value)
        return render_template('index.html', ans=calc(currency, value, desired))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)