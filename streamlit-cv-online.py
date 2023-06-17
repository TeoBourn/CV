from pathlib import Path  # gia na vrw paths
import streamlit as st
from PIL import Image

# https://emojipedia.org/objects

current_dir=Path.cwd()
resume_file=current_dir/'CV english.pdf'
profile_pic=current_dir/'pic.JPG'

page_title='Digital CV of Theodoros A. Bournelis'
page_icon=":pizza:"
name='Theodoros A. Bournelis'
info="A Physicist (mostly) and a tango student (a bit) that also chants with byzantine music. Learns about python and Data Analysis in free time. Likes pizza and pasta (in this order)."

email='bournelisth@mail.ntua.gr'

social_networks={
    'Facebook':'https://www.facebook.com/teo.noobis',
    'LinkedIn':'https://www.linkedin.com/in/theodoros-bournelis-346631171/',
    'GitHub':'https://github.com/TeoBourn'
}

projects={
    '👀 Paper on Wave-Particle interactions':'https://iopscience.iop.org/article/10.1088/1402-4896/ac96d6'
}

st.set_page_config(page_title=page_title,page_icon=page_icon)

# pdf & Profile picture

with open(resume_file,'rb') as pdf_file:
    PDFbyte=pdf_file.read()

profilepic=Image.open(profile_pic)

st.divider()   # ή st.write('...')

col1,col2=st.columns(2,gap='small')

with col1:
    st.image(profilepic,width=230)

with col2:
    st.title(name)
    st.write(info)
    st.download_button(
        label='🤐 Download Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream'
    )
    st.write('💫', email)

# social networks
st.write("---")
st.write('\n')

cols=st.columns(len(social_networks)) # ftiaxnw tosa columns osa kai to plh8os twn social networks

# edw ftiaxnw mia for gia na pairnw 3 stoixeia, to deikth, to kleidi kai to item toy leksikou
for index,(platform,link) in enumerate(social_networks.items()):
    cols[index].write(f'[{platform}]({link})')

# experience
st.divider()
st.write('\n')
st.subheader('Experience')
st.write("""
- Years of experience in fusion plasma research
- Taken and taught multiple laboratory classes in undergraduate physics students
""")

# skills
st.divider()
st.write('\n')
st.subheader('Hard Skills')
st.write("""
- 🎱 Strong knowledge in Matlab and Office, learning knowledge in Python
""")

# Studies
st.write("---")
st.write('\n')
st.subheader('Studies')
st.write('- PhD student/Researcher in Physics and Mechanics (2018-Present). PhD Thesis entitled "Nonlinear particle dynamics and momentum transport under interaction with electromagnetic waves in plasmas"')
st.write('- MSc in Advanced Physics (2015-2017). Masters Thesis in fusion plasma entitled "Colliding shock waves in magnetized fusion plasma"')
st.write('- BSc in Physics (2011-2015). Diploma Thesis in General Relativity entitled "Exuct solutions of Einsteins Equations: the case of spherical symmetric fluid"')

# Projects & Accomplishments
st.write("---")
st.write('\n')
st.subheader('Projects & Accomplishments')

for project,link in projects.items():
    st.write(f'[{project}]({link})')

st.write("-Scholarship in MSc (1st seed in Departments' BSc students graduation list in 09/2015)")
