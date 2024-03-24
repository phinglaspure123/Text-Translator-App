import streamlit as st
from googletrans import Translator,LANGUAGES
translator = Translator()

st.set_page_config(layout='wide',page_title='Text translator App')

languges=list(LANGUAGES.values())

st.title("Text translator App")
st.markdown("---")
st.markdown(
    """
<style>
    [data-testid="StyledLinkIconContainer"] {
        margin: auto;
        text-align: center;
}
[data-testid="stAppViewBlockContainer"] {
        padding: 1rem 5rem 10rem;

}


</style>
""",
    unsafe_allow_html=True,
)


col1_repl, col2_repl ,col3_repl=st.columns(3)

with col1_repl:
    text=st.text_area("Enter text to be translated")

with col2_repl:
    dest_lang=st.selectbox("Translate to",sorted(languges))
    col1, col2 ,col3= st.columns(3)
    with col2:
        button=st.button("Translate")
with col3_repl:
    # st.caption("Translated text")
    try:
        if button:
            translated = translator.translate(text, dest=dest_lang)
            st.text_area(label="Translated text",value=translated.text)
        else:
            st.text_area(label="Translated text",value="")
    except:
        st.text_area(label="Translated text",value="")