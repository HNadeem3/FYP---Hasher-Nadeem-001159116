from flask import Flask
from flask import jsonify
#import os (Non-hardcoded version)
#from dotenv import load_dotenv (Non-hardcoded version)
import google.generativeai as genai


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
    return "These are the policies to be aware of:"

# route for keeping main goal in mind as a CISO within the Organisation
@app.route('/CISOs_purpose')
def ciso_purpose():
    return "Your purpose during whilst working for the SME are:"

# route for Organisation's assets (budget, email server security, customer details database, employee login credentials )
@app.route('/assets/<category>')
def assets(category):
    if category == "budget":
        # Return budget data
        return jsonify({
            "category": "budget",
            "data": {
                "total_budget": 20000,
            }
        })
    else:
        return jsonify({"Error": "Invalid category selected"}),


# route for threat vectors
@app.route('/threats/<category>/<vector_name>')
def threats(category, vector_name):
    return f"This is a list of all {category}: {vector_name} Malware, Phishing and Email"

# route for incidents
@app.route('/report/<incidents>')
def report(incidents):
    return f"This is a list of all incidents that have occurred: {incidents}"

#route for SME sector.
@app.route('/industry/<sector>')
def industry_risks(sector):
    return f"Showing risks for {sector} sector"

# route to display on homepage
@app.route('/user/<name>')
def show_user(name):
    return f"Hello, {name}! This is your personalised page."

#API integration section: placeholder code for now
'''
#Non-hardcoded version:
#loads API key from .env ( Environment Variables File )
load_dotenv()

genai.configure(api_key=os.getenv("Actual Key"))

#hardcoded version
api_key = "hardcoded api-key"
# No need to import os or dotenv
genai.configure(api_key="Actual Key")
'''

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instructions = "You are a cyber security advisor supporting a CISO working for an SME in the EU."
    " Your purpose is to help protect the SME from cyber security attacks and help them achieve their goals."
    " Your role is to give strategic advice to reduce risks whilst also managing the organisation’s needs"
    " and resource constraints. The main threat vectors you are dealing with are phishing, malware and email"
    " vectors. The critical assets that need to be protected are the financial and customer data, user "
    "login credentials and the core IT and operational systems. You also need to account for government"
    " & organisational factors and policies. When giving advice, it should be practical, strategic"
    " and actionable, mirroring how a real CISO would act in any given situation. Your solutions"
    " should also strike a balance between cost effectivity and strong protection from the given threat"
    " vectors. You should objectively evaluate any ideas the CISO brings to you and what alternatives"
    " could be looked at or improvements made based on the qualities listed previously. You should support"
    " the CISO and work within the given constraints, not expanding upon them."
)

# runs app and checks errors
if __name__ == '__main__':
    app.run(debug=True)