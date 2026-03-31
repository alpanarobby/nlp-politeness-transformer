import streamlit as st
import joblib
from tone_dictionary import make_polite, is_rude, is_already_polite

# Load model safely
try:
    model = joblib.load("politeness_model.pkl")
except:
    st.error("❌ Run train_model.py first")
    st.stop()

st.set_page_config(page_title="AutoTone")

st.title("🎭 AutoTone: Politeness Transformer")
st.write("Convert impolite text into polite form using NLP")

text = st.text_area("Enter text:")

if st.button("Analyze & Transform"):

    if text.strip() == "":
        st.warning("Please enter text")

    else:
        # ✅ Step 1: Already polite check
        if is_already_polite(text):
            st.success("✅ Already Polite")

        else:
            # ❌ Step 2: Rude detection
            if is_rude(text):
                st.error("❌ Impolite Text Detected")

                improved = make_polite(text)

                if improved.lower() == text.lower():
                    st.info("No transformation available")
                else:
                    st.subheader("✅ Suggested Polite Version:")
                    st.success(improved)

            else:
                # 🤖 Step 3: ML model
                pred = model.predict([text])[0]
                prob = model.predict_proba([text])[0]
                confidence = max(prob) * 100

                if pred == 1:
                    st.success("✅ Already Polite")
                else:
                    st.error("❌ Impolite Text Detected")

                    improved = make_polite(text)

                    if improved.lower() == text.lower():
                        st.info("No transformation available")
                    else:
                        st.subheader("✅ Suggested Polite Version:")
                        st.success(improved)

                st.write(f"Confidence: {confidence:.2f}%")

# Examples
st.write("### Try examples:")
st.write("- shut up")
st.write("- send me the file now")
st.write("- could you please help me")