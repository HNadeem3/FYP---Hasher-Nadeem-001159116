from flask import Flask
# creates flash object
app = Flask(__name__)

# assign URL route
@app.route('/')
# function to display on home page
def homepage():
    return "Hello CISO. I am your AI Advisor."

# about page
@app.route('/about')
def about():
    return "This app uses AI to help CISOs when making decisions."

# page for the dashboard
@app.route('/dashboard')
def dashboard():
    return "This Dashboard consolidates all relevant information."

#route for the AI API
@app.route('/ask_ai')
def ask_ai():
    return "This is the response from the AI"

# route for organisation policies and legal frameworks
@app.route('/policies')
def policies():
    return "These are the policies to be aware of."

# route for keeping main goal in mind as a CISO within the Organisation
@app.route('/CISOs_purpose')
def CISOs_purpose():


# route for Organisation's assets
@app.route('/assets')
def assets():

    return "This is a list of all assets: budget etc."

# route for threat vectors
@app.route('/threats')
def threats():
    return "This is a list of all threat vectors: Malware, Phishing and Email"

# route for incidents
@app.route('/incidents')
def incidents():
    return "This is a list of all incidents that have occurred."

# route for reports
@app.route('/reports')
def reports():

@app.route('/industry/<sector>')
def industry_risks(sector):
    return f"Showing risks for {sector} sector"

# route to display on homepage
@app.route('/user/<name>')
def show_user(name):
    return f"Hello, {name}! This is your personalized page."

# runs app and checks errors
if __name__ == '__main__':
    app.run(debug=True)