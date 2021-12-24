from flask import Flask, render_template, request, json
import pandas as pd
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ready')
def ready():
    return render_template('ready.html')

@app.route('/result')
def result():
    with open('static/doc/survey.json', 'r', encoding='UTF8') as f:
        survey = json.load(f)
    return render_template('result.html', survey=json.dumps(survey))

@app.route('/qna',methods=["GET", "POST"])
def qna():
    question = open('static/doc/question.txt', 'r', encoding='UTF8').read()
    answer = open('static/doc/answer.txt', 'r', encoding='UTF8').read()
    question = question.split('\n')
    answer = answer.split('\n')

    ans1 = [ans.split(',')[0] for ans in answer[:-1]]
    ans2 = [ans.split(',')[1] for ans in answer[:-1]]
    return render_template('qnapage/qna1.html', q=question, ans1=ans1, ans2=ans2)

if __name__ == '__main__':
    port = int(os.envirion.get("PORT", 5000")
    app.run(host="0.0.0.0", port=port, debug=True)