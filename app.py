import streamlit as st
from transformers import pipeline

# Load the HuggingFace GPT-2 model
with st.spinner("Loading AI model..."):
    generator = pipeline("text-generation", model="gpt2")

# Streamlit UI
st.title("📬 Smart Email Subject Line Generator (Free & Unlimited!)")

# User input for email content and tone
email_text = st.text_area("✉️ Enter your email content here:")
tone = st.selectbox("🎯 Choose a tone:", ["Professional", "Casual", "Friendly", "Urgent", "Promotional"])

# Generate subject lines when button is clicked
if st.button("🚀 Generate Subject Lines"):
    if not email_text.strip():
        st.warning("Please enter some email content first!")
    else:
        with st.spinner("Generating subject lines..."):
            prompt = f"Generate 3 {tone.lower()} email subject lines for this email:\n{email_text}\nSubject lines:"
            output = generator(
                prompt,
                max_length=80,
                num_return_sequences=3,
                temperature=0.9,
                do_sample=True
            )
            st.markdown("### ✨ Suggested Subject Lines:")
            for i, out in enumerate(output, 1):
                result = out['generated_text'].split("Subject lines:")[-1].strip()
                st.write(f"{i}. {result}")
