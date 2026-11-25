from pathlib import Path

import streamlit as st


ROOT = Path(__file__).parent

st.set_page_config(
    page_title="Renald | A little about me",
    page_icon="✳️",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    .stApp {
        background:
            radial-gradient(ellipse at 87% 4%, #263f35 0, transparent 30%),
            #101713;
        color: #f3f0e7;
        font-family: 'DM Sans', sans-serif;
    }
    .block-container {
        max-width: 1080px;
        padding: 3rem 1.5rem 4rem;
    }
    h1, h2, h3 {
        color: #f3f0e7;
        font-family: 'Space Grotesk', sans-serif;
    }
    .kicker, .section-label {
        color: #c9d977;
        font-size: 0.74rem;
        font-weight: 700;
        letter-spacing: 0.19em;
        text-transform: uppercase;
    }
    .hero-title {
        color: #f3f0e7;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(3.2rem, 8vw, 6.4rem);
        font-weight: 700;
        letter-spacing: -0.08em;
        line-height: 0.98;
        margin: 0.5rem 0 1.4rem;
    }
    .hero-copy {
        color: #c2c9c1;
        font-size: 1.08rem;
        line-height: 1.85;
        max-width: 34rem;
    }
    .stImage img {
        border: 1px solid rgba(201, 217, 119, 0.35);
        border-radius: 24px;
        box-shadow: 14px 14px 0 #28392e;
    }
    .profile-card {
        background: #19221c;
        border: 1px solid #2b382e;
        border-radius: 18px;
        height: 100%;
        padding: 1.35rem 1.5rem;
    }
    .card-title {
        color: #c9d977;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .card-copy {
        color: #c2c9c1;
        font-size: 0.95rem;
        line-height: 1.7;
        margin: 0;
    }
    .quote {
        background: #19221c;
        border-left: 3px solid #c9d977;
        border-radius: 0 18px 18px 0;
        margin-top: 2rem;
        padding: 1.35rem 1.6rem;
    }
    .quote-copy {
        color: #f3f0e7;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(1.25rem, 3vw, 1.8rem);
        line-height: 1.5;
        margin: 0.6rem 0 0;
    }
    .footer {
        color: #89958b;
        font-size: 0.82rem;
        margin-top: 2.2rem;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

photo_col, intro_col = st.columns([0.85, 1.3], gap="large", vertical_alignment="center")

with photo_col:
    st.image(ROOT / "gwapo.jpeg", use_container_width=True)

with intro_col:
    st.markdown('<div class="kicker">A little corner of the internet</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-title">Hey, I’m<br>Renald<span style="color:#c9d977">.</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p class="hero-copy">
            Welcome to my profile—a small space for good energy, meaningful
            moments, and the things that make life feel a little more vivid.
            Take a pause, stay curious, and enjoy the soundtrack.
        </p>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-label">A few things to know</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

card1, card2, card3 = st.columns(3, gap="medium")
with card1:
    st.markdown(
        """
        <div class="profile-card">
            <div class="card-title">The mindset</div>
            <p class="card-copy">Stay curious, keep growing, and remember that progress is made one small step at a time.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with card2:
    st.markdown(
        """
        <div class="profile-card">
            <div class="card-title">The good stuff</div>
            <p class="card-copy">Good company, genuine laughs, memorable moments, and finding reasons to enjoy the little things.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with card3:
    st.markdown(
        """
        <div class="profile-card">
            <div class="card-title">The reminder</div>
            <p class="card-copy">There’s no need to have everything figured out. Keep showing up and let the next chapter unfold.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
media_col, quote_col = st.columns([0.9, 1.3], gap="large", vertical_alignment="center")

with media_col:
    st.image(
        ROOT / "loki.gif",
        caption="A little dose of mischief and magic.",
        use_container_width=True,
    )
    st.markdown('<div class="section-label">A moment to listen</div>', unsafe_allow_html=True)
    st.audio(ROOT / "yearner.mp3")

with quote_col:
    st.markdown(
        """
        <div class="quote">
            <div class="section-label">On yearning</div>
            <p class="quote-copy">“Yearning is a compass for the heart: let it point toward what matters, then take one brave step.”</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="footer">Thanks for stopping by ✳</div>', unsafe_allow_html=True)
