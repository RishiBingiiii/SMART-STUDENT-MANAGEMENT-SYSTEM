# 🎓 Smart Student Management System — Streamlit Version

## 🚀 Setup & Run

```bash
pip install streamlit werkzeug pandas
streamlit run app.py
```

Browser opens automatically at `http://localhost:8501`

---

## 🔑 Demo Login Accounts

| Role    | Username | Password    |
|---------|----------|-------------|
| Admin   | admin    | admin123    |
| Teacher | teacher  | teacher123  |
| Student | rishi    | rishi123    |

---

## 📁 File Structure

```
sms_streamlit/
├── app.py            ← Main entry point (run this)
├── auth.py           ← Login / logout logic
├── database.py       ← SQLite DB setup & helpers
├── requirements.txt
└── pages/
    ├── __init__.py
    ├── dashboard.py  ← KPI cards + charts
    ├── students.py   ← CRUD + AI predictor
    ├── attendance.py ← Mark & report
    ├── marks.py      ← Leaderboard + add marks
    ├── courses.py    ← Course cards
    └── users.py      ← User management
```

---

## ✅ Features

- Role-based login (Admin / Teacher / Student)
- Student CRUD with search
- Daily attendance marking & summary report
- Marks management with leaderboard 🥇🥈🥉
- AI Performance Predictor (grade + risk level)
- Analytics dashboard with bar charts
- Course management
- SQLite database (auto-created on first run)
