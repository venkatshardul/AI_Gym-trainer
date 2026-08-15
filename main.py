import streamlit as st
from service.auth.login_wall import render_login_wall
from service.state.session_default import initial_session_defaults

def main():
    
    st.set_page_config(
        page_icon="💪",
        page_title="GymSync",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    if not render_login_wall():
        return

    initial_session_defaults()

    # Sidebar
    with st.sidebar:
        st.title("GymSync")
        

        if st.session_state.username:
            st.caption(f"Login as: {st.session_state.username}")
            
        else:
            st.caption("Not logged in")
    
    
    st.write(f"welcome to the app {st.session_state.username}")

if __name__ == "__main__":
    main()