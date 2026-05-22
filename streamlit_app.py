import streamlit as st

st.title("🎈 Aplikasi kinan")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.markdown("*Kinan* is **really** ***cute***.")
st.markdown('''
    :red[kinan] :orange[is] :green[really] :blue[cute] :violet[hii]
    :gray[pretty] :rainbow[<3,<3] and :blue-background[huhuhuu] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
