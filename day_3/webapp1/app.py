
from flask import Flask,request,render_template
import re
app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index_fn():
    if request.method=='POST':
        c=0
        p = request.form["in_1"]
        s = request.form['in_2']
        pattern=re.compile(p)
        matches =[(ele.start(), ele.end()) for ele in re.finditer(pattern,s)]
        c=int(len(matches))
        return render_template('index.html', string=s, regex=p, match=matches, result=c)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)