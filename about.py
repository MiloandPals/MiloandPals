import streamlit as st

team = [
    {
        "dept": "Management",
        "tint": "#FFCCCC",
        "people": "Sadelu Medagamage, Managing Director · Ciaran Howes, Deputy",
        "aim": "Making Milo&amp;Pals the best team Young Enterprise has ever had through leadership and communication, "
               "with board meetings run well and every task supervised to completion.",
    },
    {
        "dept": "Digital and Technology",
        "tint": "#D3D3D3",
        "people": "Alex Saunders, Director · Nicole Mapunzira" ,
        "aim": "Built this website and runs our social media to bring Milo&amp;Pals as much engagement and popularity as possible and to insure our online image through social media is held up to an exceptional standard, also that we are seen as overall positive from an online viewpoint.",
    },
    {
        "dept": "Sales",
        "tint": "#F3EBD3",
        "people": "Richard Maamoun, Director · Ollie Yates, Deputy · Daisy Swanick, Deputy",
        "aim": "Understanding our products and selling them as well as we can. Both Olly and Daisy work alongside Richard to help ensure the business is efficient in our sales strategies",
    },
    {
        "dept": "Marketing",
        "tint": "#FFD580",
        "people": "Amy Hayes, Director · Marlei Mai Wilson, Deputy (design) · Belal Sha, Deputy (digital)",
        "aim": "Creating fun, entertaining designs for our products, and a targeted website that makes the business popular.",
    },
    {
        "dept": "Finance",
        "tint": "#C6EFCE",
        "people": "Evan Trow, Director · Jason Collier, Deputy",
        "aim": "Managing cash flow sustainably and making sure everyone gets a fair share of what we worked hard for.",
    },
    {
        "dept": "Administration",
        "tint": "#CCE5FF",
        "people": "Ruby Nightingale, Director · Amber Jordi, Deputy",
        "aim": "Keeping the business organised and the team informed of the tasks to complete, for a smooth working environment.",
    },
    {
        "dept": "Human Resources",
        "tint": "#FBCAE0",
        "people": "Grace Hamilton, Director · Hattie Wallis, Deputy",
        "aim": "Supporting wellbeing, helping everyone feel included and heard, and taking every idea into account.",
    },
    {
        "dept": "Operations",
        "tint": "#C3B1E1",
        "people": "Julia Sommer, Director · Isabella Cupertino, Deputy",
        "aim": "Finding reliable manufacturers and managing the day to day running of the business so it stays smooth and efficient.",
    },
]

st.markdown(
    '<h2 class="mp-h2">Meet the team</h2>'
    '<p class="mp-sub">Milo&amp;Pals is run by a team of students, split into eight departments.</p>',
    unsafe_allow_html=True,
)

for i in range(0, len(team), 3):
    cols = st.columns(3)
    for col, member in zip(cols, team[i:i + 3]):
        with col:
            st.markdown(
                f'<div class="mp-team" style="background:{member["tint"]};">'
                f'<h3 class="mp-h3">{member["dept"]}</h3>'
                f'<p><b>{member["people"]}</b></p>'
                f'<p>{member["aim"]}</p>'
                f"</div>",
                unsafe_allow_html=True,
            )
