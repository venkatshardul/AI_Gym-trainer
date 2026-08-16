import os
import streamlit as st
import base64


def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Failed to load CSS from {file_path}: {e}")
        return False
    return True

def inject_local_css_content(css_content):
    """
    Inject CSS from a string directly into the app.
    """
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    return True 

def inject_local_font(font_path, font_name):
    ext = font_path.rsplit(".", 1)[-1].lower()
    mime_map = {"ttf": "truetype", "otf": "opentype", "woff": "woff", "woff2": "woff2"}
    fmt = mime_map.get(ext, "truetype")

    try:
        with open(font_path, "rb") as f:
            font_data = f.read()
    except Exception as e:
        st.error(f"Failed to load font from {font_path}: {e}")
        return False

    st.markdown(f"""
    <style>
    @font-face {{
        font-family: "{font_name}";
        src: url(data:font/{ext};base64,{base64.b64encode(font_data).decode()}) format("{fmt}");
    }}
    </style>
    """, unsafe_allow_html=True)
    return True