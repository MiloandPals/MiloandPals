import streamlit as st

from helpers import logo_html

# Hero
with st.container(key="hero"):
    left, right = st.columns([3, 2], vertical_alignment="center", gap="large")
    with left:
        st.markdown(
            '<h1 class="mp-h1">Puzzles, colouring and fun with Milo the monkey</h1>'
            '<p class="mp-lead">Milo&amp;Pals is a Young Enterprise company making screen-free fun for kids: '
            "a puzzle and colouring book, a keychain and colouring pencils.</p>",
            unsafe_allow_html=True,
        )
        st.page_link("products.py", label="Shop Milo")
        st.page_link("about.py", label="Meet the team")
    with right:
        st.markdown(logo_html("400px"), unsafe_allow_html=True)

st.write("")

# Story
with st.container(key="story"):
    text_col, cards_col = st.columns([3, 2], vertical_alignment="center", gap="large")
    with text_col:
        st.markdown(
            '<h2 class="mp-h2">Fun that gets kids off their screens</h2>'
            '<p class="mp-body">Milo the mischievous monkey hides on every page of our book. Kids search for him '
            "in Where's Wally style puzzles, then colour the page in. It keeps them busy and creative instead of "
            "glued to a screen all day.</p>"
            '<p class="mp-body">Take Milo with you on a custom keychain, and grab a box of colouring pencils '
            "to bring every page to life. Or get all three in our bundle.</p>",
            unsafe_allow_html=True,
        )
    with cards_col:
        st.markdown(
            '<div class="mp-mini"><b>Puzzle</b>Spot Milo among the crowd.</div>'
            '<div class="mp-mini"><b>Colour</b>Fill every page with your own colours.</div>'
            '<div class="mp-mini"><b>Carry</b>Milo on your bag, wherever you go.</div>',
            unsafe_allow_html=True,
        )
