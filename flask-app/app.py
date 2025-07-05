python
Copy
Edit
from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return "Hello from Flask App running in Docker!"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
