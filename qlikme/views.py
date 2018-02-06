from flask import request, render_template

from qlikme import app
from qlikme import forms
from qlikme.utils import insert

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = forms.QlikmeForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    elif request.method == 'POST':
        insert(request.form.get('name'), 
               request.form.get('color'),
               request.form.get('pet'))

        return render_template('results.html',
                name=request.form.get('name'),
                color=request.form.get('color'),
                pet=request.form.get('pet'))
