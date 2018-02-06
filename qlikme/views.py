from flask import request, render_template

from qlikme import app
from qlikme import forms

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = forms.QlikmeForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    elif request.method == 'POST':
        return render_template('results.html',
                name=request.form.get('name'),
                color=request.form.get('color'),
                pet=request.form.get('pet'))
