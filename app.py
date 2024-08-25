from flask import Flask, request, jsonify
from model import answer_question

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    context = data.get('context', '')
    question = data.get('question', '')
    
    if not context or not question:
        return jsonify({"error": "Please provide both context and question."}), 400
    
    answer = answer_question(context, question)
    
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
