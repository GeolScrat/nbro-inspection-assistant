import streamlit as st

# Language selection
language = st.selectbox("Select your language / ඔබේ භාෂාව තෝරන්න", ["සිංහල", "English"])

# Sinhala content
sinhala_tasks = {
    "ඉඩමක් පරීක්ෂා කර ගැනීම": {
        "documents": [
            "ඉඩමේ මිනුම් සැලැස්ම",
            "ඉඩම් හිමිකරුගේ ජාතික හැඳුනුම්පත්පත"
        ],
        "form_link": "https://www.nbro.gov.lk/images/lrrmd/LAD.pdf"
    },
    "ගොඩනැගිලි සැළැස්මක් අනුමත කර ගැනීම": {
        "documents": [
            "ඉඩම් හිමිකරුගේ ජාතික හැඳුනුම්පත්පත",
            "චාර්ටඩ් සිවිල් ඉංජිනේරුවරයෙකුගේ අත්සමක් සහිත ගොඩනැගිලි සැලැස්ම",
            "ඉඩමේ මිනුම් සැලැස්ම"
        ],
        "form_link": "https://www.nbro.gov.lk/images/lrrmd/LAB.pdf"
    },
    "ව්‍යාපෘතියක් සඳහා වාර්තාවක් ලබා ගැනීම": {
        "documents": [
            "ඉඩමේ මිනුම් සැලැස්ම",
            "ව්‍යාපෘති යෝජනාව",
            "ඉඩම් හිමිකරුගේ ජාතික හැඳුනුම්පත්පත"
        ],
        "form_link": "https://www.nbro.gov.lk/images/lrrmd/LAP.pdf"
    }
}

# English content
english_tasks = {
    "Land inspection": {
        "documents": [
            "Survey plan of the land",
            "National Identity Card of the land owner"
        ],
        "form_link": "https://www.nbro.gov.lk/images/lrrmd/LAD.pdf"
    },
    "Approval for building plan": {
        "documents": [
            "National Identity Card of the land owner",
            "Building plan with a signature of chartered civil engineer",
            "Survey plan of the land"
        ],
        "form_link": "https://www.nbro.gov.lk/images/lrrmd/LAB.pdf"
    },
    "Report for a project": {
        "documents": [
            "Survey plan of the land",
            "Project proposal",
            "National Identity Card of the land owner"
        ],
        "form_link": "https://www.nbro.gov.lk/images/lrrmd/LAP.pdf"
    }
}

# Display title and instructions
if language == "සිංහල":
    st.title("NBRO පරීක්ෂණ සහායකය")
    st.write("කරුණාකර ඔබට අවශ්‍ය සේවාව තෝරන්න:")
    task = st.selectbox("ඔබට අවශ්‍ය සේවාව තෝරන්න", list(sinhala_tasks.keys()))
    st.subheader("අවශ්‍ය ලේඛන:")
    for doc in sinhala_tasks[task]["documents"]:
        st.markdown(f"- {doc}")
    st.subheader("පෝරමය බාගත කිරීම:")
    st.markdown(f"පෝරමය බාගත කරන්න")
else:
    st.title("NBRO Inspection Assistant")
    st.write("Please select the service you require:")
    task = st.selectbox("Select your service", list(english_tasks.keys()))
    st.subheader("Required Documents:")
    for doc in english_tasks[task]["documents"]:
        st.markdown(f"- {doc}")
    st.subheader("Download Form:")
    st.markdown(f"Download the form")
