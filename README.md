# 🎓 Smart Student Management System

A full-stack Student Management System built with **Python + Streamlit + SQLite**.
Professional UI with role-based access, analytics dashboard, AI performance predictor, and CSV import/export.

---

## 🚀 Quick Start

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Run the app
```bash
streamlit run app.py
```

### Step 3 — Open in browser
```
http://localhost:8501
```

---

## 🔑 Demo Login Accounts

| Role    | Username | Password     | Access |
|---------|----------|--------------|--------|
| 🔴 Admin   | `admin`   | `admin123`   | Full access — all pages |
| 🔵 Teacher | `teacher` | `teacher123` | Students, Attendance, Marks, Courses |
| 🟢 Student | `rishi`   | `rishi123`   | Dashboard, Students (view only) |

---

## 📁 Project Structure

```
student management/
│
├── app.py                  ← Main entry point (run this)
├── auth.py                 ← Login / logout logic
├── database.py             ← SQLite DB setup, seed data & query helpers
├── requirements.txt        ← Python dependencies
├── README.md               ← This file
├── sms.db                  ← SQLite database (auto-created on first run)
│
└── pages/
    ├── __init__.py         ← Makes pages a Python package (empty file)
    ├── dashboard.py        ← KPI cards + attendance & course charts
    ├── students.py         ← Student CRUD, search, AI predictor, export CSV
    ├── attendance.py       ← Daily attendance marking + summary report
    ├── marks.py            ← Marks leaderboard + add/update marks
    ├── courses.py          ← Course cards with enrolled students
    ├── users.py            ← User account management
    └── csv_import_export.py← Bulk import from CSV + export all students
```

---

## ✅ Features

### 🔐 Authentication
- Secure login with hashed passwords (Werkzeug)
- Three roles: Admin, Teacher, Student
- Sidebar hidden on login page
- Role-based page access control

### 📊 Dashboard
- KPI metrics: Total Students, Courses, Today's Attendance %, Top Performer
- Bar chart: Attendance for last 7 days (Present vs Absent)
- Bar chart: Students enrolled per course
- Recent students table (ordered by ID)
- Quick attendance stats per student

### 👩‍🎓 Students
- View all students ordered by ID (ascending)
- Search by Name, ID, or Course
- Expandable student cards with attendance % and avg marks
- Add new student with form validation
- Edit student details inline
- Delete student (Admin only)
- AI Performance Predictor per student
- Export all students to CSV (one click)

### 📅 Attendance
- Mark attendance daily with Present / Absent toggle
- Mark All Present / Mark All Absent quick buttons
- Save attendance per date
- Attendance Report tab: percentage, total days, status badge

### 📝 Marks
- Leaderboard with 🥇🥈🥉 medals and grade badges (A+/A/B/C/D)
- Progress bar per student
- Subject-wise average bar chart
- Add or update marks per student per subject

### 📚 Courses
- Course cards with icon, duration, fees, enrolled count
- View enrolled students per course
- Add new courses (Admin only)

### 👤 Users (Admin only)
- View all user accounts with role badges
- Create new users (Admin / Teacher / Student)
- Link student users to student records

### 📂 CSV Import & Export
- **Export:** Preview table + download `students_export.csv` with all fields
- **Import:** Upload CSV, validate columns, check for duplicates
- Progress bar during import
- Summary: Imported ✅ / Skipped ⚠️ / Errors ❌
- Download CSV template for correct format

### 🤖 AI Performance Predictor
- Calculates score from Attendance (40%) + Marks (60%)
- Predicts Grade: A / B / C / D / F
- Shows Risk Level: Low / Low-Medium / Medium / High / Very High
- Gives personalized recommendations

---

## 🎨 UI Design

| Element | Design |
|---------|--------|
| Sidebar | Deep navy gradient (`#0f172a → #1e1b4b`) |
| Background | Soft blue-white (`#f0f4ff`) |
| Primary colour | Indigo (`#6366f1`) |
| Cards | White with subtle shadow + indigo top border |
| Buttons | Indigo gradient with glow on hover |
| Tabs | Pill style, white active background |
| Font | Inter (Google Fonts) |

---

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Frontend   | Streamlit + Custom CSS  |
| Backend    | Python 3.x              |
| Database   | SQLite (built-in)       |
| Auth       | Werkzeug password hashing |
| Charts     | Streamlit native charts |
| Data       | Pandas                  |

---

## 📦 Requirements

```
streamlit>=1.32.0
werkzeug>=3.0.0
pandas>=2.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Schema

```
students      → student_id, name, age, email, phone, course, enrolled_date
courses       → course_id, course_name, duration, fees
attendance    → attendance_id, student_id, date, status (Present/Absent)
marks         → mark_id, student_id, subject, marks, exam_date
users         → id, username, password_hash, role, student_id
```

Database is auto-created as `sms.db` on first run with 5 demo students,
4 courses, 30 days of attendance history, and marks data.

---

## 🔮 Future Enhancements

- PDF report card generation (`reportlab`)
- Email notifications (`smtplib`)
- Excel export (`openpyxl`)
- Real ML model for prediction (`scikit-learn`)
- QR code attendance (`qrcode` + `opencv`)
- Deploy to Streamlit Cloud / Railway / Render

---

## 👨‍💻 Built For

B.Sc. Data Science students who want a **full-stack + database + data analytics + AI** project for their resume.

**Skills demonstrated:** Python, SQL, Streamlit, Data Analysis, UI Design, Authentication, File Handling
