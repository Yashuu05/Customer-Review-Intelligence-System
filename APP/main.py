from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def feedback():
    return render_template('feedback_form.html')

@app.route('/admin')
def admin():
    return render_template('admin_dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
