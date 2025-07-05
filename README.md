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
  
SmartGoalPlannerAI/
│
├── app.py # Flask backend logic
├── .env # Your Gemini API key (keep secret)
├── requirements.txt # Python dependencies
├── .gitignore # Files/folders to ignore (e.g., .env)
│
├── templates/ # HTML files
│ ├── index.html # Home page with form inputs
│ └── result.html # AI-generated goal plan output
│
├── static/
│ └── style.css # Styling and layout 

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
