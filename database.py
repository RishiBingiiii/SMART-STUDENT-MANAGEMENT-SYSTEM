import sqlite3
import os
import random
from datetime import date, timedelta
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), "sms.db")


def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    return db


def query(sql, args=(), one=False):
    db = get_db()
    cur = db.execute(sql, args)
    rv = cur.fetchall()
    db.close()
    return (rv[0] if rv else None) if one else rv


def mutate(sql, args=()):
    db = get_db()
    cur = db.execute(sql, args)
    db.commit()
    lid = cur.lastrowid
    db.close()
    return lid


SCHEMA = """
CREATE TABLE IF NOT EXISTS courses (
    course_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    duration    TEXT,
    fees        REAL
);
CREATE TABLE IF NOT EXISTS students (
    student_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    age           INTEGER,
    email         TEXT UNIQUE NOT NULL,
    phone         TEXT,
    course        TEXT,
    enrolled_date TEXT
);
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id    INTEGER NOT NULL,
    date          TEXT NOT NULL,
    status        TEXT NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
);
CREATE TABLE IF NOT EXISTS marks (
    mark_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject    TEXT NOT NULL,
    marks      REAL NOT NULL,
    exam_date  TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
);
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role          TEXT NOT NULL,
    student_id    INTEGER
);
"""


def init_db():
    db = get_db()
    for stmt in SCHEMA.strip().split(";"):
        if stmt.strip():
            db.execute(stmt)
    db.commit()

    if db.execute("SELECT COUNT(*) FROM users").fetchone()[0] > 0:
        db.close()
        return

    # Seed courses
    courses = [
        ("Data Science", "1 Year", 50000),
        ("Artificial Intelligence", "1 Year", 60000),
        ("Web Development", "6 Months", 30000),
        ("Machine Learning", "8 Months", 45000),
    ]
    db.executemany(
        "INSERT INTO courses(course_name,duration,fees) VALUES(?,?,?)", courses)

    # Seed students
    today = date.today().isoformat()
    students = [
        ("Rishi Sharma",  21, "rishi@example.com",  "9876543210", "Data Science"),
        ("Rahul Verma",   22, "rahul@example.com",
         "9876543211", "Artificial Intelligence"),
        ("Priya Singh",   20, "priya@example.com",  "9876543212", "Web Development"),
        ("Anjali Patel",  21, "anjali@example.com",
         "9876543213", "Machine Learning"),
        ("Amit Kumar",    23, "amit@example.com",   "9876543214", "Data Science"),
    ]
    for s in students:
        db.execute(
            "INSERT INTO students(name,age,email,phone,course,enrolled_date) VALUES(?,?,?,?,?,?)",
            (*s, today)
        )
    db.commit()

    # Seed marks
    subj_map = {
        "Data Science":            ["Python", "Statistics", "ML Basics", "SQL"],
        "Artificial Intelligence": ["Deep Learning", "NLP", "Computer Vision", "Python"],
        "Web Development":         ["HTML/CSS", "JavaScript", "Flask", "Databases"],
        "Machine Learning":        ["Algorithms", "Python", "Mathematics", "Projects"],
    }
    random.seed(42)
    rows = db.execute("SELECT student_id, course FROM students").fetchall()
    for sid, course in rows:
        for subj in subj_map.get(course, ["Subject1", "Subject2"]):
            db.execute(
                "INSERT INTO marks(student_id,subject,marks,exam_date) VALUES(?,?,?,?)",
                (sid, subj, random.randint(60, 98), today)
            )

    # Seed attendance (last 30 days)
    for sid, _ in rows:
        for i in range(30):
            d = (date.today() - timedelta(days=i)).isoformat()
            status = "Present" if random.random() > 0.2 else "Absent"
            db.execute(
                "INSERT INTO attendance(student_id,date,status) VALUES(?,?,?)",
                (sid, d, status)
            )
    db.commit()

    # Seed users
    db.execute(
        "INSERT INTO users(username,password_hash,role) VALUES(?,?,?)",
        ("admin", generate_password_hash("admin123"), "admin")
    )
    db.execute(
        "INSERT INTO users(username,password_hash,role) VALUES(?,?,?)",
        ("teacher", generate_password_hash("teacher123"), "teacher")
    )
    rishi_id = db.execute(
        "SELECT student_id FROM students WHERE name='Rishi Sharma'"
    ).fetchone()[0]
    db.execute(
        "INSERT INTO users(username,password_hash,role,student_id) VALUES(?,?,?,?)",
        ("rishi", generate_password_hash("rishi123"), "student", rishi_id)
    )
    db.commit()
    db.close()
