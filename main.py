import streamlit as streamLit
from MultiModalRetriever import MultiModalSearch

streamLit.set_page_config(
    layout="wide"
)

def main():
    streamLit.markdown("<h1 style='text-align: center; color: green;'>Fashion Cloth Search App</h1>", unsafe_allow_html=True)

    multiModalSearch = MultiModalSearch()

    query = streamLit.text_input("What type of Clothes you would like to see?") 
    if streamLit.button("Search"):
        if len(query) >0:
            results = multiModalSearch.search(query)
            streamLit.warning("Your inquiry is about - " + query)
            streamLit.subheader("Search Result:")
            col1, col2, col3 = streamLit.columns([1,1,1])
            with col1:
                streamLit.write(f"Score: {round(results[0].score*100,2)}%")
                streamLit.image(results[0].content, use_column_width=True)
            with col2:
                streamLit.write(f"Score: {round(results[1].score*100,2)}%")
                streamLit.image(results[1].content, use_column_width=True)
            with col3:
                streamLit.write(f"Score: {round(results[2].score*100,2)}%")
                streamLit.image(results[2].content, use_column_width=True)
        else:
            streamLit.warning("Please enter your query.")

if __name__== "__main__":
        main()