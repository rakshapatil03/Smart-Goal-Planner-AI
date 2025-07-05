# 🧠 Smart Goal Planner AI (Final Year Engineering Project)

This is a web-based AI-powered smart planner built using **Flask** and **Google Gemini AI**. It helps users prioritize daily tasks, allocate time efficiently, and even provides mental wellness tips — all based on their available hours and goals.

---

## 🚀 Features

- ✅ Inputs user's goals and total available time
- 🧠 Uses Gemini AI (`gemini-1.5-pro`) for smart time planning
- 🗓️ Suggests best times of the day (morning, afternoon, evening) for tasks
- 🧘 Mental health tip included in every plan
- 🎨 Clean, responsive, and aesthetic UI
- 🔐 API key is securely managed using `.env`

  ## 📁 Project Structure
  ├── app.py               # Flask backend with Gemini integration  
├── .env                 # Stores your Gemini API key securely (should not be uploaded)  
├── requirements.txt     # List of Python dependencies  
├── .gitignore           # Prevents uploading sensitive/unnecessary files like .env  
│
├── templates/           # HTML templates folder  
│   ├── index.html       # Homepage with task & time input  
│   └── result.html      # Displays the AI-generated plan  
│
├── static/              # CSS, JS, and other static assets  
    └── style.css        # Aesthetic and clean styling for the web pages  

---

## ⚙️ Setup Instructions

### 1. Clone this repo
git clone https://github.com/your-username/SmartGoalPlannerAI.git
cd SmartGoalPlannerAI

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add your Gemini API key
Create a .env file and add:
GEMINI_API_KEY=your_api_key_here

### 4. Run the app
python app.py
Then open http://127.0.0.1:5000/ in your browser.

### 🧠 Powered By
Gemini 1.5 Flash
Flask
HTML, CSS

### 📌 Topics
#AI #Flask #GeminiAPI #SmartPlanner #ProductivityAI #DailyGoalPlanner

### 🙌 Acknowledgments
Made with ❤️ for productivity lovers who want to use AI to plan smarter, not harder.
