import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Manjunadh Portfolio",
    page_icon="🔥",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.main {
    background-color: #0f172a;
    color: white;
}

h1,h2,h3,h4,p {
    color: white;
}

.stButton>button {
    background-color: #38bdf8;
    color: black;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

.skill-box {
    background-color: #1e293b;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    margin: 5px;
}

.project-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.title("🔥 MANJUNADH PORTFOLIO")

st.subheader(
    "Python Developer | Machine Learning Enthusiast | Data Analyst"
)

st.write("""
Passionate about AI, Machine Learning,
Backend Development, Data Analytics,
and modern technologies.
""")

st.markdown("---")

# ABOUT SECTION
st.header("👨‍💻 About Me")

st.write("""
I am a B.Tech student passionate about:

- Python Development
- Machine Learning
- Backend Development
- AI Tools
- Data Analytics
- Unity Game Development

Currently building real-world projects
through internships and self-learning.
""")

st.markdown("---")

# SKILLS SECTION
st.header("🚀 Skills")

skills = [
    "Python",
    "Machine Learning",
    "Data Analytics",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Scikit-learn",
    "Flask",
    "Django",
    "SQL",
    "GitHub",
    "Unity"
]

cols = st.columns(4)

for index, skill in enumerate(skills):
    cols[index % 4].markdown(
        f"<div class='skill-box'>{skill}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")

# PROJECTS SECTION
st.header("📂 Internship Projects")

# FUTURE INTERNS
st.subheader("🔥 Future Interns Projects")

st.markdown("""
<div class='project-card'>

<h3>🎫 Support Ticket Classification & Prioritization</h3>

<p>
Machine Learning + NLP based system that:
</p>

<ul>
<li>Classifies support tickets</li>
<li>Predicts priority levels</li>
<li>Improves support efficiency</li>
</ul>

<p>
Technologies Used:
Python, NLP, Scikit-learn, Pandas
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='project-card'>

<h3>📈 Sales Forecasting</h3>

<p>
Built forecasting models to predict
future sales trends using machine learning.
</p>

<ul>
<li>Data preprocessing</li>
<li>Visualization</li>
<li>Prediction models</li>
</ul>

<p>
Technologies Used:
Python, Pandas, Matplotlib
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='project-card'>

<h3>👥 Customer Segmentation</h3>

<p>
Clustered customers using KMeans algorithm.
</p>

<ul>
<li>Behavior analysis</li>
<li>Data visualization</li>
<li>Customer grouping</li>
</ul>

<p>
Technologies Used:
Python, KMeans, Scikit-learn
</p>

</div>
""", unsafe_allow_html=True)

# PRODIGY INFOTECH
st.subheader("🚀 Prodigy Infotech Projects")

st.markdown("""
<div class='project-card'>

<h3>📊 Customer Segmentation using KMeans</h3>

<p>
Performed customer segmentation using
unsupervised machine learning.
</p>

<ul>
<li>KMeans Clustering</li>
<li>Elbow Method</li>
<li>Data Visualization</li>
</ul>

<p>
Technologies Used:
Python, Pandas, Matplotlib, Scikit-learn
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='project-card'>

<h3>📉 Exploratory Data Analysis</h3>

<p>
Performed EDA and extracted insights
from datasets.
</p>

<ul>
<li>Data Cleaning</li>
<li>Visualization</li>
<li>Insights Extraction</li>
</ul>

<p>
Technologies Used:
Python, Pandas, Seaborn
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# CERTIFICATES SECTION
st.header("🏆 Certificates")

st.write("""
✅ Deloitte Data Analytics Virtual Internship

✅ Future Interns Machine Learning Internship

✅ Prodigy Infotech Internship

✅ Cognizant Certifications
""")

st.info("Add your certificate images in the project folder.")

st.markdown("---")

# GITHUB SECTION
st.header("💻 GitHub")

st.write("Upload all internship projects to GitHub.")

st.code("""
GitHub Repositories:
- ML Projects
- Data Analytics Projects
- Python Projects
- Internship Tasks
""")

st.markdown("---")

# CONTACT SECTION
st.header("📞 Contact")

st.write("📧 Email: mademanjunadh@gmail.com")

st.write("💼 LinkedIn: https://www.linkedin.com/in/manjuanadh-prakash-madem-3ba71636a?utm_source=share_via&utm_content=profile&utm_medium=member_android")

st.write("💻 GitHub: https://github.com/manjunadh1810-del")

st.button("🔥 Hire Me")

st.markdown("---")

# FOOTER
st.write("Made with ❤️ using Python & Streamlit")
