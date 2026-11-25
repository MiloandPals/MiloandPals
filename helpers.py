import base64
import os

import streamlit as st

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO_FILE = os.path.join(HERE, "logo.png")


@st.cache_data
def logo_b64():
    with open(LOGO_FILE, "rb") as f:
        return base64.b64encode(f.read()).decode()


def logo_html(max_width="400px"):
    """The Milo&Pals logo (a PNG with transparent corners)."""
    return (
        f'<div class="mp-logo" style="max-width:{max_width};">'
        f'<img src="data:image/png;base64,{logo_b64()}" alt="Milo&amp;Pals logo">'
        f"</div>"
    )
