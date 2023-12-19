from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample task list
tasks = [
    {"id": 1, "description": "Buy milk", "status": "incomplete"},
    {"id": 2, "description": "Read a book", "status": "incomplete"},
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        description = request.form['description']
        new_task = {
            "id": len(tasks) + 1,
            "description": description,
            "status": "incomplete"
        }
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        task["status"] = "completed"
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
