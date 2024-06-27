from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    title = "My Flask App"
    description = "This is a simple web application using Flask."
    items = ['Flask', 'Jinja2', 'Python']
    return render_template('index.html', title=title, description=description, items=items)

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
