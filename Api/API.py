from flask import Flask, request, jsonify
import time
app=Flask(_name_)


app.config['post_data_limiter'] = 0
app.config['first_time'] = None

@app.route("/")
def home():
    return "Hello Guys!"

@app.route('/post_data', methods=['POST'])
def post_data():
    if app.config['first_time'] is None:
        app.config['first_time'] = time.time()
    elif app.config['first_time'] + 60 < time.time():
        app.config['first_time'] = time.time()
        app.config['post_data_limiter'] = 0
    elif app.config['post_data_limiter'] >= 15:
        app.config['first_time'] = app.config['first_time'] + 60
        return jsonify({"message": "limit reached, 1 min penalty"})
    
    app.config['post_data_limiter'] += 1
    data = request.json
    result = {"message": "Data received successfully", "data": data}
    return jsonify(result)