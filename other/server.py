from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({'error': 'Division by zero!'}), 400
    else:
        return jsonify({'error': 'Invalid operation!'}), 400
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
