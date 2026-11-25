import streamlit as st

from helpers import LOGO_FILE

st.set_page_config(
    page_title="Milo&Pals",
    page_icon=LOGO_FILE,
    layout="wide",
)

# CSS is injected BEFORE pages.run() so the styling is there when the page renders.
# Colours: pistachio green #93C572, banana yellow #F6C945, forest #1F3A2B, mint #EAF4DF.
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito+Sans:wght@400;600;700&display=swap');

html, body, .stApp, [data-testid="stAppViewContainer"] {
    font-family: 'Nunito Sans', system-ui, sans-serif;
    color: #1F3A2B;
    background: #FFFFFF;
}

/* Top navigation bar */
[data-testid="stHeader"] { background: #93C572; }
[data-testid="stHeader"] a,
[data-testid="stHeader"] span,
[data-testid="stHeader"] p { color: #1F3A2B !important; font-weight: 700; }

.block-container { max-width: 1200px; padding-top: 4.5rem; padding-bottom: 3rem; }

/* Headings and text */
.mp-h1 { font-family: 'Fredoka', sans-serif; font-weight: 700; font-size: clamp(2.2rem, 5vw, 4rem);
         line-height: 1.05; margin: 0 0 16px 0; color: #1F3A2B; }
.mp-h2 { font-family: 'Fredoka', sans-serif; font-weight: 600; font-size: clamp(1.8rem, 3.5vw, 2.75rem);
         line-height: 1.1; margin: 0 0 8px 0; color: #1F3A2B; }
.mp-h3 { font-family: 'Fredoka', sans-serif; font-weight: 600; font-size: 1.6rem;
         line-height: 1.15; margin: 0 0 8px 0; color: #1F3A2B; }
.mp-lead { font-size: 1.25rem; line-height: 1.5; max-width: 520px; margin: 0 0 16px 0; }
.mp-body { font-size: 1.1rem; line-height: 1.6; margin: 0 0 12px 0; max-width: 560px; }
.mp-sub  { font-size: 1.1rem; color: #3E5A49; margin: 0 0 16px 0; }
.mp-price { font-family: 'Fredoka', sans-serif; font-weight: 700; font-size: 1.9rem; margin: 4px 0; }

/* Hero (homepage) */
.st-key-hero { background: #93C572; border-radius: 32px; padding: 48px !important; }
.mp-logo { margin: 0 auto; }
.mp-logo img { width: 100%; display: block; border-radius: 50%; }

/* Page links styled as buttons */
[data-testid="stPageLink-NavLink"] { border-radius: 999px; min-height: 48px; justify-content: center; }
.st-key-hero [data-testid="stPageLink-NavLink"] { background: #1F3A2B; }
.st-key-hero [data-testid="stPageLink-NavLink"] p { color: #FFFFFF !important; font-weight: 700; }

/* Story band */
.st-key-story { background: #F6C945; border-radius: 32px; padding: 48px !important; }
.mp-mini { background: #FFFFFF; border-radius: 20px; padding: 20px; margin-bottom: 12px; }
.mp-mini b { font-family: 'Fredoka', sans-serif; font-size: 1.35rem; display: block; margin-bottom: 4px; }

/* Product cards */
[class*="st-key-product_card"] { background: #EAF4DF; border-radius: 24px; padding: 24px !important; }
.mp-photo { aspect-ratio: 4 / 3; border-radius: 16px; display: flex; align-items: center; justify-content: center;
            text-align: center; padding: 16px; font-weight: 700; margin-bottom: 8px; }

/* Disclaimer box */
.mp-disclaimer { background: #C62828; color: #FFFFFF; border-radius: 16px; padding: 18px 24px;
                 font-size: 1.1rem; line-height: 1.5; margin: 0 0 24px 0; }

.mp-disclaimer a { color: #FFFFFF; font-weight: 700; }

/* Basket */
.st-key-basket .mp-basket-note a { color: #FFFFFF; font-weight: 700; }
.st-key-basket [data-testid="stLinkButton"] a { background: #F6C945; border: none; border-radius: 999px;
                                                min-height: 48px; padding: 0 24px; }
.st-key-basket [data-testid="stLinkButton"] a p { color: #1F3A2B !important; font-weight: 700; }
.st-key-basket { background: #1F3A2B; border-radius: 24px; padding: 28px !important; color: #FFFFFF; }
.mp-row { display: flex; justify-content: space-between; gap: 16px; font-size: 1.15rem; padding: 4px 0; color: #FFFFFF; }
.mp-total { font-size: 1.4rem; font-weight: 700; border-top: 1px solid #4E6F5C; margin-top: 8px; padding-top: 12px; }
.mp-basket-note { color: #D9EBC9; font-size: 1rem; margin: 6px 0; }

/* Team cards */
.mp-team { border-radius: 20px; padding: 24px; min-height: 250px; margin-bottom: 16px; }
.mp-team p { margin: 0 0 8px 0; line-height: 1.5; }

/* Footer */
.mp-footer { background: #1F3A2B; border-radius: 24px; padding: 28px 32px; margin-top: 48px;
             display: flex; flex-wrap: wrap; gap: 16px; justify-content: space-between; align-items: center; }
.mp-footer .brand { font-family: 'Fredoka', sans-serif; font-weight: 700; font-size: 1.5rem; color: #FFFFFF; }
.mp-footer .note { color: #D9EBC9; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

home_page = st.Page("homepage.py", title="Home", default=True)
products_page = st.Page("products.py", title="Our products")
about_page = st.Page("about.py", title="Our team")

# position="top" needs Streamlit 1.46 or newer. On an older version, remove it to use the sidebar.
pages = st.navigation([home_page, products_page, about_page], position="top")
pages.run()

st.markdown(
    '<div class="mp-footer"><div class="brand">Milo&amp;Pals</div>'
    '<div class="note">A Young Enterprise company. Contact: '
    '<a href="mailto:miloandpals17@gmail.com" style="color:#FFFFFF;">miloandpals17@gmail.com</a></div></div>',
    unsafe_allow_html=True,
)
