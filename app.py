import streamlit as st
from database import init_db

st.set_page_config(
    page_title="Smart Student Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Inject CSS directly ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    background: #f0f4ff !important;
}
[data-testid="stSidebarNav"], #MainMenu, footer, header,
[data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
.block-container { padding: 2rem 2.5rem 2rem !important; max-width: 1400px !important; }

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
    min-width: 260px !important;
}
[data-testid="stSidebar"] > div { padding: 0 !important; }
[data-testid="stSidebar"] .stMarkdown p { color: rgba(255,255,255,0.9) !important; font-size: 13px !important; }
[data-testid="stSidebar"] .stButton > button {
    background: transparent !important; border: none !important;
    color: rgba(255,255,255,0.65) !important; text-align: left !important;
    padding: 10px 20px !important; border-radius: 10px !important;
    font-size: 14px !important; font-weight: 500 !important;
    transition: all 0.18s ease !important; margin: 2px 12px !important;
    width: calc(100% - 24px) !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(99,102,241,0.18) !important; color: #fff !important; transform: translateX(3px) !important;
}
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.08) !important; margin: 12px 20px !important; }

/* HEADINGS */
h1 { font-size: 1.8rem !important; font-weight: 800 !important; color: #0f172a !important;
     letter-spacing: -0.03em !important; margin-bottom: 1.5rem !important;
     padding-bottom: 1rem !important; border-bottom: 2px solid #e2e8f0 !important; }
h2 { font-size: 1.2rem !important; font-weight: 700 !important; color: #1e293b !important; }
h3 { font-size: 1rem !important; font-weight: 600 !important; color: #334155 !important; }

/* METRIC CARDS */
[data-testid="stMetric"] {
    background: white !important; border-radius: 16px !important;
    padding: 1.25rem 1.5rem !important; border: 1px solid #e2e8f0 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 16px rgba(0,0,0,0.04) !important;
    position: relative !important; overflow: hidden !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="stMetric"]:hover { transform: translateY(-2px) !important; box-shadow: 0 4px 20px rgba(99,102,241,0.12) !important; }
[data-testid="stMetric"]::before {
    content: '' !important; position: absolute !important; top: 0; left: 0; right: 0 !important;
    height: 3px !important; background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
}
[data-testid="stMetricLabel"] { font-size: 12px !important; font-weight: 600 !important; color: #64748b !important; text-transform: uppercase !important; letter-spacing: 0.08em !important; }
[data-testid="stMetricValue"] { font-size: 2rem !important; font-weight: 800 !important; color: #0f172a !important; letter-spacing: -0.03em !important; }

/* BUTTONS */
.stButton > button, [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
    color: white !important; border: none !important; border-radius: 10px !important;
    padding: 10px 20px !important; font-weight: 600 !important; font-size: 13.5px !important;
    transition: all 0.2s ease !important; box-shadow: 0 2px 8px rgba(99,102,241,0.3) !important;
}
.stButton > button:hover { transform: translateY(-1px) !important; box-shadow: 0 4px 16px rgba(99,102,241,0.4) !important; }
[data-testid="stDownloadButton"] > button {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
    color: white !important; border: none !important; border-radius: 10px !important;
    padding: 10px 20px !important; font-weight: 600 !important;
    box-shadow: 0 2px 8px rgba(16,185,129,0.3) !important; transition: all 0.2s ease !important;
}
[data-testid="stDownloadButton"] > button:hover { transform: translateY(-1px) !important; box-shadow: 0 4px 16px rgba(16,185,129,0.4) !important; }

/* TABS */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: #f1f5f9 !important; border-radius: 12px !important;
    padding: 4px !important; gap: 2px !important; border: none !important;
}
[data-testid="stTabs"] [data-baseweb="tab"] {
    border-radius: 9px !important; font-weight: 600 !important; font-size: 13.5px !important;
    color: #64748b !important; padding: 8px 20px !important; border: none !important; transition: all 0.2s !important;
}
[data-testid="stTabs"] [aria-selected="true"] { background: white !important; color: #6366f1 !important; box-shadow: 0 1px 4px rgba(0,0,0,0.1) !important; }
[data-testid="stTabs"] [data-baseweb="tab-highlight"], [data-testid="stTabs"] [data-baseweb="tab-border"] { display: none !important; }

/* EXPANDERS */
[data-testid="stExpander"] {
    border: 1px solid #e2e8f0 !important; border-radius: 14px !important;
    background: white !important; box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
    margin-bottom: 10px !important; overflow: hidden !important;
    transition: box-shadow 0.2s, transform 0.2s !important;
}
[data-testid="stExpander"]:hover { box-shadow: 0 4px 20px rgba(99,102,241,0.1) !important; transform: translateY(-1px) !important; }
[data-testid="stExpander"] summary { font-weight: 600 !important; font-size: 14.5px !important; color: #1e293b !important; padding: 14px 18px !important; }

/* FORMS & INPUTS */
[data-testid="stForm"] {
    background: white !important; border-radius: 16px !important;
    padding: 1.5rem !important; border: 1px solid #e2e8f0 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
}
.stTextInput > div > div > input, .stNumberInput > div > div > input {
    border: 1.5px solid #e2e8f0 !important; border-radius: 10px !important;
    font-size: 14px !important; transition: border-color 0.2s, box-shadow 0.2s !important; background: #fafbff !important;
}
.stTextInput > div > div > input:focus, .stNumberInput > div > div > input:focus {
    border-color: #6366f1 !important; box-shadow: 0 0 0 3px rgba(99,102,241,0.1) !important; background: white !important;
}
.stTextInput label, .stNumberInput label, .stSelectbox label, .stFileUploader label {
    font-size: 13px !important; font-weight: 600 !important; color: #374151 !important; letter-spacing: 0.01em !important;
}

/* DATAFRAMES */
[data-testid="stDataFrame"] { border-radius: 14px !important; overflow: hidden !important; border: 1px solid #e2e8f0 !important; box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important; }

/* ALERTS */
[data-testid="stAlert"] { border-radius: 12px !important; border: none !important; font-weight: 500 !important; }

/* FILE UPLOADER */
[data-testid="stFileUploaderDropzone"] {
    border: 2px dashed #c7d2fe !important; border-radius: 14px !important;
    background: #fafbff !important; transition: all 0.2s !important;
}
[data-testid="stFileUploaderDropzone"]:hover { border-color: #6366f1 !important; background: #eef2ff !important; }

/* PROGRESS */
[data-testid="stProgressBar"] > div > div { background: linear-gradient(90deg, #6366f1, #8b5cf6) !important; border-radius: 4px !important; }

/* DIVIDER */
hr { border-color: #e2e8f0 !important; margin: 1.5rem 0 !important; }

/* CUSTOM COMPONENTS */
.sidebar-brand { padding: 28px 20px 20px; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 8px; }
.sidebar-brand h2 { color: white !important; font-size: 1.3rem !important; font-weight: 800 !important; letter-spacing: -0.02em !important; margin: 0 !important; border: none !important; padding: 0 !important; }
.sidebar-brand p { color: rgba(255,255,255,0.45) !important; font-size: 11px !important; text-transform: uppercase !important; letter-spacing: 0.12em !important; margin: 2px 0 0 !important; }
.user-pill { display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.08); border-radius: 50px; padding: 6px 14px 6px 6px; margin: 0 12px; }
.user-avatar { width: 28px; height: 28px; background: linear-gradient(135deg, #6366f1, #8b5cf6); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 13px; }
.user-name { color: white; font-size: 13px; font-weight: 600; }
.user-role { color: rgba(255,255,255,0.45); font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em; }
.section-card { background: white; border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-bottom: 1.25rem; }
.section-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.25rem; padding-bottom: 0.75rem; border-bottom: 1px solid #f1f5f9; }
.section-title { font-size: 15px; font-weight: 700; color: #1e293b; }
.stat-chip { background: #eef2ff; color: #6366f1; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
.nav-section { padding: 8px 20px 4px; font-size: 10px; font-weight: 700; color: rgba(255,255,255,0.25); text-transform: uppercase; letter-spacing: 0.12em; }
.demo-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-top: 1rem; }
.demo-card { background: #f8fafc; border-radius: 10px; padding: 10px; text-align: center; border: 1px solid #e2e8f0; font-size: 12px; }
.demo-role { font-weight: 700; color: #6366f1; font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; }
.demo-creds { color: #475569; margin-top: 4px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

init_db()

for k, v in {"logged_in": False, "role": None, "username": None, "student_id": None, "page": "Dashboard"}.items():
    if k not in st.session_state:
        st.session_state[k] = v


def logout():
    for k in ["logged_in", "username", "role", "student_id"]:
        st.session_state[k] = None
    st.session_state.logged_in = False
    st.rerun()


if not st.session_state.logged_in:
    st.markdown(
        """<style>[data-testid="stSidebar"]{display:none!important;}</style>""", unsafe_allow_html=True)
    from auth import login_page
    login_page()
else:
    with st.sidebar:
        initial = st.session_state.username[0].upper(
        ) if st.session_state.username else "U"
        st.markdown(f"""
        <div class="sidebar-brand">
            <div style="font-size:2rem;margin-bottom:8px">🎓</div>
            <h2>Smart SMS</h2>
            <p>Student Management System</p>
        </div>
        <div style="margin:16px 0 8px">
            <div class="user-pill">
                <div class="user-avatar">{initial}</div>
                <div>
                    <div class="user-name">{st.session_state.username}</div>
                    <div class="user-role">{st.session_state.role}</div>
                </div>
            </div>
        </div>
        <div class="nav-section">Main Menu</div>
        """, unsafe_allow_html=True)

        if st.button("📊  Dashboard",    use_container_width=True):
            st.session_state.page = "Dashboard"
        if st.button("👩‍🎓  Students",    use_container_width=True):
            st.session_state.page = "Students"
        if st.button("📚  Courses",      use_container_width=True):
            st.session_state.page = "Courses"

        if st.session_state.role in ["admin", "teacher"]:
            st.markdown('<div class="nav-section">Academic</div>',
                        unsafe_allow_html=True)
            if st.button("📅  Attendance", use_container_width=True):
                st.session_state.page = "Attendance"
            if st.button("📝  Marks",      use_container_width=True):
                st.session_state.page = "Marks"

        if st.session_state.role == "admin":
            st.markdown('<div class="nav-section">Admin</div>',
                        unsafe_allow_html=True)
            if st.button("👤  Users",      use_container_width=True):
                st.session_state.page = "Users"
            if st.button("📂  CSV Import / Export", use_container_width=True):
                st.session_state.page = "CSV"

        st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
        st.divider()
        if st.button("🚪  Sign Out",     use_container_width=True):
            logout()

    page = st.session_state.page
    if page == "Dashboard":
        import pages.dashboard as p
        p.show()
    elif page == "Students":
        import pages.students as p
        p.show()
    elif page == "Courses":
        import pages.courses as p
        p.show()
    elif page == "Attendance":
        import pages.attendance as p
        p.show()
    elif page == "Marks":
        import pages.marks as p
        p.show()
    elif page == "Users":
        import pages.users as p
        p.show()
    elif page == "CSV":
        import pages.csv_import_export as p
        p.show()
