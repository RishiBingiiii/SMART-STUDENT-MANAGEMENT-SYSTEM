import streamlit as st
from werkzeug.security import check_password_hash
from database import query


def login_page():
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)

        # Logo & Title
        st.markdown("""
        <div style="text-align:center; margin-bottom:2rem;">
            <div style="font-size:3.5rem;">🎓</div>
            <h1 style="font-size:2rem;font-weight:800;color:#0f172a;margin:8px 0 4px;
                       border:none;padding:0;">Smart SMS</h1>
            <p style="color:#64748b;font-size:14px;margin:0;">
                Student Management System — Sign in to continue
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Login form
        with st.form("login_form"):
            username = st.text_input(
                "Username", placeholder="Enter your username")
            password = st.text_input(
                "Password", placeholder="Enter your password", type="password")
            submitted = st.form_submit_button(
                "🔐  Sign In", use_container_width=True)

        if submitted:
            user = query("SELECT * FROM users WHERE username=?",
                         [username], one=True)
            if user and check_password_hash(user["password_hash"], password):
                st.session_state.logged_in = True
                st.session_state.username = user["username"]
                st.session_state.role = user["role"]
                st.session_state.student_id = user["student_id"]
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

        # Demo accounts
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:14px;padding:16px;">
            <p style="font-size:11px;font-weight:700;color:#94a3b8;text-transform:uppercase;
                      letter-spacing:0.1em;text-align:center;margin:0 0 12px;">Demo Accounts</p>
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;">
                <div style="background:white;border:1px solid #e2e8f0;border-radius:10px;
                            padding:10px;text-align:center;">
                    <div style="font-size:10px;font-weight:700;color:#dc2626;text-transform:uppercase;
                                letter-spacing:0.06em;">Admin</div>
                    <div style="font-size:12px;color:#475569;margin-top:4px;font-family:monospace;">
                        admin<br>admin123</div>
                </div>
                <div style="background:white;border:1px solid #e2e8f0;border-radius:10px;
                            padding:10px;text-align:center;">
                    <div style="font-size:10px;font-weight:700;color:#2563eb;text-transform:uppercase;
                                letter-spacing:0.06em;">Teacher</div>
                    <div style="font-size:12px;color:#475569;margin-top:4px;font-family:monospace;">
                        teacher<br>teacher123</div>
                </div>
                <div style="background:white;border:1px solid #e2e8f0;border-radius:10px;
                            padding:10px;text-align:center;">
                    <div style="font-size:10px;font-weight:700;color:#059669;text-transform:uppercase;
                                letter-spacing:0.06em;">Student</div>
                    <div style="font-size:12px;color:#475569;margin-top:4px;font-family:monospace;">
                        rishi<br>rishi123</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
