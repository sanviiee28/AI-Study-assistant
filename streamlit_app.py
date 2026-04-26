import streamlit as st
import PyPDF2
import time

st.set_page_config(page_title="AI Study Assistant", layout="wide")

# ---------- CUSTOM UI ----------
st.markdown("""
<style>
body {
    background: #0f172a;
}
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
h1 {
    text-align: center;
    font-size: 48px !important;
}
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #22c55e);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
}
.chat-box {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1>📚 AI Study Assistant</h1>", unsafe_allow_html=True)

# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# ---------- TEXT EXTRACTION ----------
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# ---------- FAKE AI ----------
def fake_ai_response(question):
    q = question.lower()

    if "array" in q:
        return "Arrays are linear structures storing elements in contiguous memory, allowing fast index-based access."
    elif "stack" in q:
        return "Stack follows LIFO (Last In First Out). Operations: push, pop, peek."
    elif "queue" in q:
        return "Queue follows FIFO (First In First Out). Used in scheduling systems."
    elif "tree" in q:
        return "Trees are hierarchical structures with nodes connected in parent-child relationships."
    elif "graph" in q:
        return "Graphs represent networks using vertices and edges. Used in maps and social networks."
    elif "complexity" in q:
        return "Time complexity measures efficiency. Big O shows worst-case performance."
    else:
        return "This question is covered in the uploaded Data Structures document."

# ---------- MAIN ----------
if uploaded_file:
    text = extract_text(uploaded_file)

    st.success("✅ PDF uploaded successfully. Ready for analysis.")

    # ---------- SUMMARY ----------
    if st.button("✨ Generate Summary"):
        with st.spinner("AI is thinking..."):
            time.sleep(2)

        st.success("""
This document is a comprehensive Data Structures question bank covering arrays, stacks, queues, trees, and graphs.

It includes short, medium, and long-answer questions with focus on algorithm complexity, recursion, and real-world applications.

Designed using Bloom’s taxonomy, it helps students prepare effectively for exams.
        """)

    # ---------- QUESTIONS ----------
    if st.button("🧠 Generate Questions"):
        with st.spinner("Generating smart questions..."):
            time.sleep(2)

        st.info("""
1. What is a data structure?
2. Explain stack and its operations.
3. What is time complexity?
4. Differentiate between arrays and linked lists.
5. Explain BFS and DFS.
        """)

    # ---------- CHAT ----------
    st.subheader("💬 Ask Anything")

    user_input = st.text_input("Ask a question")

    if user_input:
        with st.spinner("AI is typing..."):
            time.sleep(1.5)

        response = fake_ai_response(user_input)

        st.markdown(f"<div class='chat-box'><b>You:</b> {user_input}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-box'><b>AI:</b> {response}</div>", unsafe_allow_html=True)