import streamlit as st

# Language selection
language = st.selectbox("Select your language / ඔබේ භාෂාව තෝරන්න", ["English", "සිංහල"])

# Define content in both languages
content = {
    "English": {
        "title": "NBRO Inspection Assistant",
        "intro": "Welcome! I can help you choose the correct inspection form and guide you through the process.",
        "client_needs": [
            "Constructing a building",
            "Buying or selling land",
            "Getting a loan or permit",
            "Starting a large-scale project"
        ],
        "form_mapping": {
            "Constructing a building": "Building",
            "Buying or selling land": "Development",
            "Getting a loan or permit": "Development",
            "Starting a large-scale project": "Project"
        },
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
        "client_needs": [
            "ගොඩනැගිල්ලක් ඉදිකිරීම",
            "ඉඩමක් මිලදී ගැනීම හෝ විකුණා දැමීම",
            "ණය හෝ අවසරපත් ලබා ගැනීම",
            "විශාල ව්‍යාපෘතියක් ආරම්භ කිරීම"
        ],
        "form_mapping": {
            "ගොඩනැගිල්ලක් ඉදිකිරීම": "ගොඩනැගිලි",
            "ඉඩමක් මිලදී ගැනීම හෝ විකුණා දැමීම": "ඉදිකිරීම්",
            "ණය හෝ අවසරපත් ලබා ගැනීම": "ඉදිකිරීම්",
            "විශාල ව්‍යාපෘතියක් ආරම්භ කිරීම": "ව්‍යාපෘතිය"
        },
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

# Display title and intro
st.title(content[language]["title"])
st.write(content[language]["intro"])

# Ask user what they need help with
client_need = st.selectbox(
    "What do you need assistance with? / ඔබට මාර්ගෝපදේශ අවශ්‍ය කාර්යය තෝරන්න",
    content[language]["client_needs"]
)

# Recommend the appropriate form
recommended_form = content[language]["form_mapping"][client_need]
st.success(f"We recommend using the **{recommended_form}** inspection request form.")

# Show required information
st.subheader("Required Information / අවශ්‍ය තොරතුරු")
for item in content[language]["form_details"][recommended_form]:
    st.markdown(f"- {item}")

# Show submission instructions
st.subheader("Submission Instructions / ඉදිරිපත් කිරීමේ උපදෙස්")
st.write(content[language]["submission"])
