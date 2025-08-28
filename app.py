import streamlit as st

# Language selection
language = st.selectbox("Select your language / ඔබේ භාෂාව තෝරන්න", ["English", "සිංහල"])

# Define content in both languages
content = {
    "English": {
        "title": "NBRO Inspection Assistant",
        "intro": "Welcome! I can help you choose the correct inspection form and guide you through the process.",
        "form_options": ["Building", "Development", "Project"],
        "form_details": {
            "Building": [
                "Applicant and land owner details",
                "Land location and usage",
                "Building plan and associated structures"
            ],
            "Development": [
                "Land details",
                "Purpose of inspection",
                "Access route"
            ],
            "Project": [
                "Project type",
                "Land details",
                "Access route"
            ]
        },
        "submission": "Please submit the completed form to the NBRO office with all required documents."
    },
    "සිංහල": {
        "title": "භූ විනාශ අවදානම් තක්සේරු සහායකය",
        "intro": "ආයුබෝවන්! ඔබට නිවැරදි පරීක්ෂණ ආකෘතිය තෝරා ගැනීමට සහ ක්‍රියාවලිය පිළිබඳ මාර්ගෝපදේශ ලබා දිය හැක.",
        "form_options": ["ගොඩනැගිලි", "ඉදිකිරීම්", "ව්‍යාපෘතිය"],
        "form_details": {
            "ගොඩනැගිලි": [
                "අයදුම්කරු සහ ඉඩම් හිමිකරුගේ විස්තර",
                "ඉඩමේ ස්ථානය සහ භාවිතය",
                "ගොඩනැගිලි සැලැස්ම සහ අමුණා ඇති වස්තු"
            ],
            "ඉදිකිරීම්": [
                "ඉඩම් විස්තර",
                "පරීක්ෂණයේ අරමුණ",
                "ප්‍රවේශ මාර්ගය"
            ],
            "ව්‍යාපෘතිය": [
                "ව්‍යාපෘති වර්ගය",
                "ඉඩම් විස්තර",
                "ප්‍රවේශ මාර්ගය"
            ]
        },
        "submission": "කරුණාකර පිරවූ ආකෘතිය අවශ්‍ය ලේඛන සමඟ NBRO කාර්යාලයට ඉදිරිපත් කරන්න."
    }
}

# Display content
st.title(content[language]["title"])
st.write(content[language]["intro"])

form_type = st.selectbox("Select the type of inspection form / පරීක්ෂණ ආකෘතිය තෝරන්න", content[language]["form_options"])

st.subheader("Required Information / අවශ්‍ය තොරතුරු")
for item in content[language]["form_details"][form_type]:
    st.markdown(f"- {item}")

st.subheader("Submission Instructions / ඉදිරිපත් කිරීමේ උපදෙස්")
st.write(content[language]["submission"])
