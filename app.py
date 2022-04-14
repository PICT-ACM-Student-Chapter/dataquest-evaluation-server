from flask import Flask, request
import os
import pandas as pd
from sklearn.metrics import accuracy_score

app = Flask(__name__)

@app.route('/fe-se-round-1', methods=['POST'])
def eval1():
    if request.method == 'POST':

        file = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static', file.filename)
        file.save(filepath)
        print(filepath)
        attempt = pd.read_csv(filepath)
        soln = pd.read_csv('static/fe-se-1.csv')

        if attempt.shape == soln.shape:
            print("Fine til; here")
            attempt = attempt.iloc[:, 1].values
            soln = soln.iloc[:, 1].values
            
            public_soln = soln[:1000]
            public_att = attempt[:1000]

            private_soln = soln[1000:]
            private_att = attempt[1000:]

            public_acc = accuracy_score(public_soln, public_att)
            private_acc = accuracy_score(private_soln, private_att)

    return {'private': private_acc,
    'public': public_acc}

    

@app.route('/te-be-round-1', methods=['POST'])
def eval2():
    if request.method == 'POST':
        file = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static', file.filename)
        file.save(filepath)
        attempt = pd.read_csv(filepath)
    
        soln = pd.read_csv('static/te-be-1.csv')

        public_acc = 0

        private_acc = 0
        print(soln.shape)
        if attempt.shape == soln.shape:
            
            attempt = attempt.iloc[:, 1].values
            soln = soln.iloc[:, 1].values

            pr_mark = int(soln.shape[0]*0.7)
            
            public_soln = soln[:pr_mark]
            public_att = attempt[:pr_mark]

            private_soln = soln[pr_mark:]
            private_att = attempt[pr_mark:]

            public_acc = accuracy_score(public_soln, public_att)
            private_acc = accuracy_score(private_soln, private_att)

    return {'private': private_acc,
    'public': public_acc}


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)