import base64
import glob
import io
import os

import streamlit as st
from PIL import Image

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

images = [
    {"file": "front cover.jpg", "caption": "Front Cover"},
    {"file": "back cover.jpg", "caption": "Back Cover"},
]

if "image_index" not in st.session_state:
    st.session_state.image_index = 0

price_book = 7.99
price_keychain = 1.50
price_pencils = 0.99
# Bundle = 1 book + 1 keychain + 1 box of pencils. Change this number to set your bundle price.
price_bundle = 9.99


def photo_placeholder(text, tint):
    return f'<div class="mp-photo" style="background:{tint};">{text}</div>'


def find_image(*names, keyword=None):
    """Look for an image by exact file name, then by a word in the file name (e.g. 'pencil')."""
    for name in names:
        path = os.path.join(CURRENT_DIR, name)
        if os.path.exists(path):
            return path
    if keyword:
        for path in glob.glob(os.path.join(CURRENT_DIR, "*")):
            if keyword in os.path.basename(path).lower() and path.lower().endswith(
                (".png", ".jpg", ".jpeg", ".webp")
            ):
                return path
    return None


def photo_box(path, alt_text, tint):
    """Show an image in a 4:3 box (shrunk first so the page stays fast), or a placeholder if it's missing."""
    if path is None:
        return photo_placeholder(f"Add {alt_text} photo", tint)
    try:
        img = Image.open(path).convert("RGBA")
        img.thumbnail((700, 700))
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        data = base64.b64encode(buffer.getvalue()).decode()
    except Exception:
        return photo_placeholder(f"Add {alt_text} photo", tint)
    return (
        '<div class="mp-photo" style="background:#FFFFFF;">'
        f'<img src="data:image/png;base64,{data}" alt="{alt_text}" '
        'style="width:100%;height:100%;object-fit:contain;">'
        "</div>"
    )


st.markdown(
    '<h2 class="mp-h2">Our products</h2>'
    '<p class="mp-sub">Choose how many of each you would like and your basket updates below.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="mp-disclaimer"><b>Disclaimer:</b> we haven\'t finished the final draft of our products yet, '
    "so we can't sell them at the moment. If you would like to reserve a product, you can email us at "
    '<a href="mailto:miloandpals17@gmail.com">miloandpals17@gmail.com</a>.</div>',
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(key="product_card_book"):
        sub_l, sub_img, sub_r = st.columns([1, 3, 1], vertical_alignment="center")

        with sub_l:
            if st.button("‹", key="prev_btn", use_container_width=True):
                st.session_state.image_index = (st.session_state.image_index - 1) % len(images)
                st.rerun()

        with sub_r:
            if st.button("›", key="next_btn", use_container_width=True):
                st.session_state.image_index = (st.session_state.image_index + 1) % len(images)
                st.rerun()

        with sub_img:
            current_item = images[st.session_state.image_index]
            shown = False
            for name in (current_item["file"], current_item["file"].replace(".jpg", ".jpeg")):
                path = os.path.join(CURRENT_DIR, name)
                if os.path.exists(path):
                    st.image(Image.open(path), use_container_width=True)
                    shown = True
                    break
            if not shown:
                st.markdown(photo_placeholder("Add book cover photo", "#F6C945"), unsafe_allow_html=True)

        st.markdown(
            '<h3 class="mp-h3">Milo the mischievous monkey puzzle + colouring book</h3>'
            "<p>This book contains a premium mix of Where's Wally style puzzles and colouring pages for your "
            "kids to enjoy instead of being glued to their screens all day!</p>"
            f'<div class="mp-price">£{price_book:.2f}</div>',
            unsafe_allow_html=True,
        )
        qty_book = st.number_input("Quantity (Book)", min_value=0, value=0, key="qty_b")

with col2:
    with st.container(key="product_card_keychain"):
        keychain_path = find_image("keychain.png", keyword="keychain")
        st.markdown(photo_box(keychain_path, "keychain", "#C3B1E1"), unsafe_allow_html=True)
        st.markdown(
            '<h3 class="mp-h3">Milo Keychain</h3>'
            "<p>Take Milo wherever you go with our high-quality custom keychains.</p>"
            f'<div class="mp-price">£{price_keychain:.2f}</div>',
            unsafe_allow_html=True,
        )
        qty_keychain = st.number_input("Quantity (Keychain)", min_value=0, value=0, key="qty_k")

with col3:
    with st.container(key="product_card_pencils"):
        pencils_path = find_image(
            "colouring pencils.png", "colouring_pencils.png", "pencils.png", keyword="pencil"
        )
        st.markdown(photo_box(pencils_path, "colouring pencils", "#FBCAE0"), unsafe_allow_html=True)
        st.markdown(
            '<h3 class="mp-h3">Box of Colouring Pencils</h3>'
            "<p>A box of colouring pencils, ready for every page of Milo's book.</p>"
            f'<div class="mp-price">£{price_pencils:.2f}</div>',
            unsafe_allow_html=True,
        )
        qty_pencils = st.number_input("Quantity (Pencils)", min_value=0, value=0, key="qty_p")

with col4:
    with st.container(key="product_card_bundle"):
        st.markdown(photo_placeholder("Photo coming soon", "#93C572"), unsafe_allow_html=True)
        st.markdown(
            '<h3 class="mp-h3">Bundle</h3>'
            "<p>One Milo puzzle + colouring book, one Milo keychain and one box of colouring pencils.</p>"
            f'<div class="mp-price">£{price_bundle:.2f}</div>',
            unsafe_allow_html=True,
        )
        qty_bundle = st.number_input("Quantity (Bundle)", min_value=0, value=0, key="qty_bundle")

st.write("")

# Basket
basket = [
    ("Milo Puzzle &amp; Colouring Book", qty_book, price_book),
    ("Milo Keychain", qty_keychain, price_keychain),
    ("Box of Colouring Pencils", qty_pencils, price_pencils),
    ("Bundle", qty_bundle, price_bundle),
]
total_items = sum(q for _, q, _ in basket)
total_cost = sum(q * p for _, q, p in basket)

with st.container(key="basket"):
    st.markdown('<h3 class="mp-h3" style="color:#FFFFFF;">Your basket</h3>', unsafe_allow_html=True)
    if total_items > 0:
        word = "item" if total_items == 1 else "items"
        rows = "".join(
            f'<div class="mp-row"><span>x{q} {name}</span><span>£{q * p:.2f}</span></div>'
            for name, q, p in basket
            if q > 0
        )
        st.markdown(
            f'<div class="mp-basket-note">You have selected {total_items} {word} from our range:</div>'
            f"{rows}"
            f'<div class="mp-row mp-total"><span>Total</span><span>£{total_cost:.2f}</span></div>'
            '<div class="mp-basket-note">To reserve these items, email '
            '<a href="mailto:miloandpals17@gmail.com">miloandpals17@gmail.com</a>.</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="mp-basket-note">Your basket is empty. Add something above.</div>',
            unsafe_allow_html=True,
        )

    st.link_button("Visit our Trading Station page", "https://www.ye-tradingstation.org.uk/company/19702")
