from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Configure Gemini with API key from environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Flask app
app = Flask(__name__)

# Load Gemini model
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route("/", methods=["GET", "POST"])
def index():
    plan_blocks = []
    
    if request.method == "POST":
        goals = request.form.get("goals", "")
        total_time = request.form.get("total_time", "")

        prompt = f"""
You are a helpful AI Smart Planner.

Here are the user's goals: {goals}
Total available time: {total_time} hours.

1. Prioritize tasks logically.
2. Allocate time for each.
3. Present a beautiful daily plan.
4. Add a mental health tip.

Please generate the plan now:
"""

        try:
            response = model.generate_content(prompt)
            full_plan = response.text.strip()
            plan_blocks = full_plan.split('\n\n')
        except Exception as e:
            plan_blocks = [f"❌ Error: {str(e)}"]

    return render_template("index.html", plan_blocks=plan_blocks)

if __name__ == "__main__":
    app.run(debug=True)
