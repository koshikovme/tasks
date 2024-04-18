from flask import Flask, request, redirect, url_for, render_template, make_response, session, abort, jsonify
from db.database import execute
from db.user import create_user, hash_password, user_exists, get_tasks
from db.task import remove_task, update_priority, update_status, add_task, sorted_tasks


app = Flask(__name__)
app.secret_key='ADADADAD'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        password = session['password']
        id = user_exists(username, password)
        if id:
            tasks = get_tasks(id[0])
            return render_template('index.html', tasks=tasks)
    return render_template('index.html', tasks=[])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        hashed_password = hash_password(password)
        
        id = user_exists(username, hashed_password)
        
        if id:
            session['username'] = username
            session['password'] = hashed_password
            session['id'] = id

            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)
    
    return render_template('login.html')


@app.route('/signUp', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        create_user(username, password)

        id = user_exists(username, hash_password(password))

        if id:
            session['username'] = username
            session['password'] = hash_password(password)
            session['id'] = id

            return redirect(url_for('login'))

    return render_template('signUp.html')





@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    session.pop('id', None)
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('username')
    return response



@app.route('/create-task', methods=['POST'])
def create_task():
    header = request.json.get('header')
    details = request.json.get('details')
    priority = request.json.get('priority')
    user_id = request.json.get('userId')


    add_task(header, details, priority, user_id)

    return jsonify({'message': 'Priority updated successfully', 'taskId': header}), 200


@app.route('/remove-task', methods=['POST'])
def remove_task_by_id():
    task_id = request.json.get('taskId')

    remove_task(task_id=task_id)

    return jsonify({'message': 'Task removed successfully', 'taskId': task_id}), 200

@app.route('/update-priority', methods=['POST'])
def update_priority_by_id():
    task_id = request.json.get('taskId')
    new_priority = request.json.get('newPriority')  

    update_priority(task_id=task_id, new_priority=new_priority)

    return jsonify({'message': 'Priority updated successfully', 'taskId': task_id}), 200

@app.route('/update-is-done', methods=['POST'])
def update_status_by_id():
    task_id = request.json.get('taskId')
    is_done = request.json.get('isDone')

    print("UPDATE STATUS: ", task_id, is_done)

    update_status(task_id=task_id, is_done=is_done)

    return jsonify({'message': 'Priority updated successfully', 'taskId': task_id}), 200

@app.route('/sort-by', methods=['GET'])
def sort_by():
    sort_by = request.args.get('sort_by', 'id')
    user_id = session.get('id')
    if user_id:
        user_id = user_id[0] if isinstance(user_id, tuple) else user_id
        tasks = sorted_tasks(user_id, sort_by)
        return render_template('index.html', tasks=tasks)
    else:
        return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
    )
