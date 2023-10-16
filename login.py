from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials for demonstration purposes
valid_users = {'merchant1': 'password1', 'merchant2': 'password2'}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    # Check if the provided credentials are valid
    if username in valid_users and valid_users[username] == password:
        # Redirect to a merchant dashboard or another page
        return redirect(url_for('dashboard', username=username))
    else:
        # Invalid credentials, redirect back to the login page with an error message
        return render_template('login.html', error='Invalid username or password')

@app.route('/dashboard/<username>')
def dashboard(username):        
    return f'<h1>Welcome, {username}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)


















# The Webpage using  HTML in same directory 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form action="/authenticate" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>

