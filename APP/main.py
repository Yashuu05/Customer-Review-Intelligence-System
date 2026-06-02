from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flash_messages'

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('signup'))
        
        # Mock Authentication
        if email == 'yash@gmail.com' and password == 'yash123':
            return redirect(url_for('admin'))
        else:
            flash('For testing, please use yash@gmail.com / yash123', 'error')
            return redirect(url_for('signup'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Mock Authentication
        if email == 'yash@gmail.com' and password == 'yash123':
            return redirect(url_for('admin'))
        else:
            flash('Invalid email or password. Use yash@gmail.com / yash123', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback_form.html')

@app.route('/admin')
def admin():
    return render_template('admin_dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
