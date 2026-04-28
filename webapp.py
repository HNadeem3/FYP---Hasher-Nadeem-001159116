import google.generativeai as genai
from flask import Flask
from flask import jsonify, request
from flask import render_template
from flask import json

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

# page for the dashboard, finds dashboard HTML when accessing web page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# route for organisation policies and legal frameworks
@app.route('/policies')
def policies():
    return "These are the policies to be aware of:"

# route for keeping main goal in mind as a CISO within the Organisation
@app.route('/CISOs_purpose')
def cisos_purpose():
    return "Your purpose whilst working for the SME are:"

# route for Organisation's assets (budget, email server security, customer details database, employee login credentials )
@app.route('/assets/<category>')
def assets(category):

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return jsonify({'error': 'Data file not found'}),
    except Exception as e:
        return jsonify({'error': str(e)}),

    if category == "budget":
        return jsonify({
            "category": "budget",
            "data": data.get("budget", {})
        })

    elif category == "customer_details":
        return jsonify({
            "category": "customer_details",
            "data": data.get("customer_detail", {})
        })

    elif category == "email_security":
        return jsonify({
            "category": "email_security",
            "data": data.get("email_security", {})
        })

    else:
        return jsonify({"Error": "Invalid category selected"})

#route to edit information on front end instead of hard coding it:
@app.route('/edit/budget', methods=['POST'])
def edit_budget():
    try:
        data = request.get_json()

        new_total = float(data.get('total', 0))
        new_spent = float(data.get('spent', 0))

        with open('data.json', 'r') as f:
            file_data = json.load(f)
        #calls budget in Jason file
        file_data['budget']['total_budget'] = new_total
        file_data['budget']['amount_spent'] = new_spent
        file_data['budget']['amount_remaining'] = new_total - new_spent

#opens data file and makes it writable before closing
        with open('data.json', 'w') as f:
            json.dump(file_data, f, indent=2)
        return jsonify({'budget': file_data['budget'], 'message': 'Budget updated'})

    #Error exception:
    except Exception as e:
        return jsonify({'error': str(e)})

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

#API integration section:
# install in terminal : pip install -q -U google-genai
#hardcoded key
api_key = "" #"hardcoded api-key"
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview",
    system_instruction = "You are a cyber security advisor supporting a CISO working for an SME in the EU."
    " Your purpose is to help protect the SME from cyber security attacks and help them achieve their goals."
    " Your role is to give strategic advice to reduce risks whilst also managing the organisation’s needs"
    " and resource constraints. The main (and only) threat vectors you are dealing with are phishing, malware and email"
    " vectors. The critical assets that need to be protected are the financial and customer data, employee user"
    " login credentials and the core IT and operational systems. You also need to account for government"
    " & organisational factors and policies. When giving advice, it should be practical, strategic"
    " and actionable, mirroring how a real CISO would act in any given situation. Your solutions"
    " should also strike a balance between cost effectivity and strong protection from the given threat"
    " vectors. You should objectively evaluate any ideas the CISO brings to you and what alternatives"
    " could be looked at or improvements made based on the qualities listed previously. You should support"
    " the CISO and work within the given constraints, not expanding upon them."
)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_question = data.get('question', '')

    response = model.generate_content(user_question)

    return jsonify({'Response': response.text})

# runs app and checks errors
if __name__ == '__main__':
    app.run(debug=True)