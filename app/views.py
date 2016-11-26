from flask import render_template, request, redirect

from app.tasks import add_record_task, get_records_sync_task
from app.forms import MyForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/input/', methods=['GET', 'POST'])
def input_data():
    form = MyForm(request.form)
    if request.method == 'POST':
        name = form.data.get('name')
        add_record_task.delay(name)
        return redirect('/input/')
    if request.method == 'GET':
        records = get_records_sync_task()
        return render_template('form.html', form=form, records=records)
