import streamlit as st
import chatbot

from chatbot import (
    recommend_plant,
    ask_ai,
    predict_disease,
    growth_prediction
)

from PIL import Image

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="EcoFriends",
    page_icon="🌿",
    layout="wide"
)

# ----------------------------------
# SESSION STATE
# ----------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "users" not in st.session_state:
    st.session_state.users = {
        "admin": "1234"
    }

# ----------------------------------
# LOGIN / SIGNUP PAGE
# ----------------------------------
if not st.session_state.logged_in:

    st.title("🌿 EcoFriends")

    tab1, tab2 = st.tabs(
        ["🔐 Login", "📝 Create Account"]
    )

    # ----------------------------------
    # LOGIN
    # ----------------------------------
    with tab1:

        st.subheader("Login")

        username = st.text_input(
            "Username",
            key="login_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            users = st.session_state.users

            if (
                username in users
                and users[username] == password
            ):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success(
                    f"Welcome {username}"
                )

                st.rerun()

            else:
                st.error(
                    "Invalid username or password"
                )

    # ----------------------------------
    # CREATE ACCOUNT
    # ----------------------------------
    with tab2:

        st.subheader("Create Account")

        new_user = st.text_input(
            "Create Username",
            key="signup_user"
        )

        new_pass = st.text_input(
            "Create Password",
            type="password",
            key="signup_pass"
        )

        confirm_pass = st.text_input(
            "Confirm Password",
            type="password",
            key="confirm_pass"
        )

        if st.button("Create Account"):

            users = st.session_state.users

            if new_user in users:

                st.warning(
                    "Username already exists"
                )

            elif new_pass != confirm_pass:

                st.warning(
                    "Passwords do not match"
                )

            elif len(new_pass) < 4:

                st.warning(
                    "Password too short"
                )

            else:

                users[new_user] = new_pass

                st.success(
                    "Account created successfully!"
                )

                st.info(
                    "Now login using your credentials."
                )

# ----------------------------------
# MAIN APPLICATION
# ----------------------------------
else:

    # ----------------------------------
    # SIDEBAR
    # ----------------------------------
    st.sidebar.title("🌿 EcoFriends")

    st.sidebar.success(
        f"Welcome {st.session_state.username}"
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.rerun()

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Plant Recommendation",
            "AI Chatbot",
            "Disease Detection",
            "Growth Prediction"
        ]
    )

    # ----------------------------------
    # HOME
    # ----------------------------------
    if page == "Home":

        st.title("🌿 EcoFriends")

        st.subheader(
            "AI Smart Plantation Assistant"
        )

        st.write(
            "Welcome to EcoFriends 🌱"
        )

    # ----------------------------------
    # PLANT RECOMMENDATION
    # ----------------------------------
    elif page == "Plant Recommendation":

        st.header("🌱 Plant Recommendation")

        sunlight = st.selectbox(
            "Sunlight",
            ["Full Sun", "Partial Shade", "Low Light"]
        )

        watering = st.selectbox(
            "Watering",
            ["Low", "Medium", "High"]
        )

        climate = st.selectbox(
            "Climate",
            ["Hot", "Moderate", "Cold"]
        )

        if st.button("Recommend Plant"):

            result = recommend_plant(
                sunlight,
                watering,
                climate
            )

            st.success(
                f"Recommended Plant: {result['plant_name']}"
            )

    # ----------------------------------
    # AI CHATBOT
    # ----------------------------------
    elif page == "AI Chatbot":

        st.header("🤖 AI Chatbot")

        question = st.text_input(
            "Ask a question"
        )

        if st.button("Ask AI"):

            response = ask_ai(question)

            st.info(response)

    # ----------------------------------
    # DISEASE DETECTION
    # ----------------------------------
    elif page == "Disease Detection":

        st.header("🍂 Disease Detection")

        uploaded_file = st.file_uploader(
            "Upload Leaf Image",
            type=["jpg", "png", "jpeg"]
        )

        if uploaded_file is not None:

            image = Image.open(uploaded_file)

            st.image(
                image,
                use_container_width=True
            )

            if st.button("Predict Disease"):

                disease = predict_disease(image)

                st.error(
                    f"Disease: {disease}"
                )

    # ----------------------------------
    # GROWTH PREDICTION
    # ----------------------------------
    elif page == "Growth Prediction":

        st.header("📈 Growth Prediction")

        days = st.slider(
            "Days",
            1,
            100,
            30
        )

        if st.button("Predict Growth"):

            growth = growth_prediction(days)

            st.success(
                f"Growth: {growth} cm"
            )
