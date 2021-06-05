import streamlit as st
import altair as alt
import json
from PIL import Image

# Constants
SOLICITS_FEEDBACK = ["2 B", "3 A", "5 A", "7 A", "8 B", "10 B",
                     "12 B", "14 B", "16 A", "20 A"]
GIVES_FEEDBACK = ["1 A", "4 B", "6 B", "9 B", "11 B", "13 A", "15 A",
                  "17 B", "18 B", "19 B"]
NUM_QUESTIONS = 20

def get_score(all_scores, indices):
    score = 0
    for x in indices:
        i, ans = int(x.split()[0]), x.split()[-1]
        if ans == "A":
            score += (5-all_scores[i])
        elif ans == "B":
            score += all_scores[i]
    return score

with open('data/questions.json', 'r') as f:
    questions_dict = json.load(f)
qscore = [0 for _ in range(NUM_QUESTIONS+1)] # Keeping a dummy zero for ease of indexing

st.title("Johari Window")
st.write("### Instructions: ")
st.write("Read the questions thoroughly and move the slider towards \
         the answer where you feel most inclined. For example, if you  \
         find answer A most in line with your thoughts, move the slider \
         all the way to the left, i.e., number 0. Number 2 signifies slight \
         inclination towards option A and 3 signifies slight inclination \
         towards option B. Similarly, number 5 signifies that you completely \
         agree with option B.")

with st.form("Johari Window Form"):
    for i in range(1,NUM_QUESTIONS+1):
        st.write("## Question {}".format(i))
        st.write(questions_dict["Q"+str(i)])
        st.write("> **A** ) {}".format(questions_dict["Q" + str(i) + "a"]))
        st.write("> **B** ) {}".format(questions_dict["Q" + str(i) + "b"]))
        qscore[i] = st.slider("Answer:", 0, 5, step=1, key=str(i))
    submitted = st.form_submit_button("Check Results!")

    solicit_score = get_score(qscore, SOLICITS_FEEDBACK)
    give_score = get_score(qscore, GIVES_FEEDBACK)

    if submitted:
        st.write("Solicits Feedback:", solicit_score)
        st.write("Gives Feedback:", give_score)

meaning_image = Image.open('images/johari_explanation.png')
action_image = Image.open('images/johari_actions.jpg')
st.write("## Explanation")
st.image(meaning_image, caption="The image explains what different quadrants mean in the johari \
    window. The scores would be shown after you click the submit button")

st.image(action_image, caption="This image shows the actions that you need to take to expand your window. \
    Self-discovery is the way to self-evolution.")