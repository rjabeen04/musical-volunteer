from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for, jsonify


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

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        data = {
            'name': name,
            'email': email,
            'message': message
        }

        redis_client = current_app.redis_client
        redis_client.rpush('contact_messages', json.dumps(data))

        flash('Thank you for contacting us!', 'success')
        return redirect(url_for('main.home'))

    return render_template('contact.html')

@main.route('/contact_submissions')
def contact_submissions():
    redis_client = current_app.redis_client
    stored = redis_client.lrange('contact_messages', 0, -1)
    messages = [json.loads(msg) for msg in stored]
    return render_template('contact_submissions.html', messages=messages)

@main.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

