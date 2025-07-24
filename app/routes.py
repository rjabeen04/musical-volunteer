from flask import Blueprint, render_template, request, current_app
import json

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'instrument': request.form['instrument'],
            'availability': request.form['availability']
        }
        redis_client = current_app.redis_client
        redis_client.rpush('volunteers', json.dumps(data))
        return render_template('thank_you.html', name=data['name'])
    return render_template('volunteer_form.html')

@main.route('/volunteers')
def list_volunteers():
    redis_client = current_app.redis_client
    stored = redis_client.lrange('volunteers', 0, -1)
    volunteers = [json.loads(v) for v in stored]
    return render_template('volunteers.html', volunteers=volunteers)
