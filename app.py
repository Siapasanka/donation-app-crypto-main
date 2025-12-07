from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # perlu untuk flash message

# ---------- Flask-Mail Configuration ----------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rikiviell@gmail.com'        
app.config['MAIL_PASSWORD'] = 'YOUR_APP_PASSWORD_HERE'    
mail = Mail(app)

# ---------- Routes ----------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_body = request.form['message']

        msg = Message(subject=f"Contact Form Message from {name}",
                      sender='noreply@yourdomain.com',  # bisa sembarang
                      recipients=[app.config['MAIL_USERNAME']],
                      body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}")
        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            print(e)
            flash('Failed to send message. Please check server configuration.', 'error')

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
