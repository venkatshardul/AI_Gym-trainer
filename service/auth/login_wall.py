import streamlit as st

def render_login_wall():
   if st.session_state.get("username") is not None:
    return True 
   st.title("Ai real-time pose estimation AI Coach")
   st.markdown("""
   ## How it works?
   - Upload a video 
   """)
   with st.form('login-form', clear_on_submit=False ):
    username = st.text_input("Username")
    
    submit = st.form_submit_button("Start Session")
   if submit:
    if not username:
        st.error("Please enter a username")
        return False
    else:
        st.session_state.username = username
        # st.session_state.user_id = f"user-{uuid.uuid4().hex}"
        st.rerun()
   return False
