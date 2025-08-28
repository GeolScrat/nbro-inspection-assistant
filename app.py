
import streamlit as st

# Set page config
st.set_page_config(page_title="NBRO Inspection Assistant", layout="centered")

# Language selection
language = st.radio("Select your language / ඔබේ භාෂාව තෝරන්න", ["English", "සිංහල"])

# Define prompts and responses
if language == "English":
    st.title("NBRO Inspection Assistant")
    st.write("Welcome! I can help you choose the correct inspection form and guide you through the process.")
    
    form_type = st.selectbox("What type of inspection do you need?", ["Building", "Development", "Project"])
    
    if form_type == "Building":
        st.write("You selected **Building Inspection**.")
        st.write("This form is used for landslide risk assessment before constructing buildings.")
        st.write("Required documents include:")
        st.markdown("- Applicant and land owner details
- Land location and usage
- Building plan and associated structures")
    
    elif form_type == "Development":
        st.write("You selected **Development Inspection**.")
        st.write("This form is used for land inspections before purchase, sale, or subdivision.")
        st.write("Required documents include:")
        st.markdown("- Land details
- Purpose of inspection
- Access route")
    
    elif form_type == "Project":
        st.write("You selected **Project Inspection**.")
        st.write("This form is used for large-scale projects like roads, hydro-power, mining, etc.")
        st.write("Required documents include:")
        st.markdown("- Project type
- Land details
- Access route")

    st.write("Once completed, submit the form to NBRO with the required documents.")

else:
    st.title("NBRO පරීක්ෂණ සහායකය")
    st.write("ආයුබෝවන්! ඔබට නිවැරදි පරීක්ෂණ පෝරමය තෝරා ගැනීමට සහ ක්‍රියාවලිය පිළිබඳ මාර්ගෝපදේශ ලබා දීමට මම උදව් කරමි.")
    
    form_type = st.selectbox("ඔබට අවශ්‍ය පරීක්ෂණ වර්ගය කුමක්ද?", ["ගොඩනැගිලි", "ඉදිකිරීම්", "ව්‍යාපෘතිය"])

    if form_type == "ගොඩනැගිලි":
        st.write("ඔබ තෝරාගෙන ඇති පරීක්ෂණය: **ගොඩනැගිලි පරීක්ෂණය**")
        st.write("මෙම පෝරමය ගොඩනැගිලි ඉදිකිරීමට පෙර භූමි නායය අවදානම් පරීක්ෂා කිරීම සඳහා භාවිතා වේ.")
        st.write("අවශ්‍ය ලේඛන:")
        st.markdown("- අයදුම්කරු සහ භූමි හිමිකරුගේ විස්තර
- භූමි පිහිටීම සහ භාවිතය
- ගොඩනැගිලි සැලැස්ම සහ අමුණුකම්")

    elif form_type == "ඉදිකිරීම්":
        st.write("ඔබ තෝරාගෙන ඇති පරීක්ෂණය: **ඉදිකිරීම් පරීක්ෂණය**")
        st.write("මෙම පෝරමය භූමි මිලදී ගැනීම, විකුණුම්, හෝ බෙදා හැරීම සඳහා පරීක්ෂණ සඳහා භාවිතා වේ.")
        st.write("අවශ්‍ය ලේඛන:")
        st.markdown("- භූමි විස්තර
- පරීක්ෂණයේ අරමුණ
- පිවිසුම් මාර්ගය")

    elif form_type == "ව්‍යාපෘතිය":
        st.write("ඔබ තෝරාගෙන ඇති පරීක්ෂණය: **ව්‍යාපෘති පරීක්ෂණය**")
        st.write("මෙම පෝරමය මාර්ග, ජල විදුලි, පතල්, කෘෂිකර්ම වැනි විශාල ව්‍යාපෘති සඳහා භාවිතා වේ.")
        st.write("අවශ්‍ය ලේඛන:")
        st.markdown("- ව්‍යාපෘති වර්ගය
- භූමි විස්තර
- පිවිසුම් මාර්ගය")

    st.write("පෝරමය පිරවූ පසු, අවශ්‍ය ලේඛන සමඟ NBRO වෙත ඉදිරිපත් කරන්න.")
