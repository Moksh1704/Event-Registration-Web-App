import streamlit as st


st.set_page_config(page_title="Know Your City", layout="centered")


if "page" not in st.session_state:
    st.session_state.page = "Home"

if "selected_event_name" not in st.session_state:
    st.session_state.selected_event_name = None

if "selected_event" not in st.session_state:
    st.session_state.selected_event = None

#Data
event_data = [
    {
        "id": "e1",
        "name": "Tech Conference 2024",
        "date": "2024-09-15",
        "location": "AU Convention Center",
        "description": "A conference showcasing the latest in technology.",
        "map_link": "https://maps.google.com/?q=AU+Convention+Center",
        "time": "09:00 AM - 05:00 PM",
        "slots": 100
    },
    {
        "id": "e2",
        "name": "Music Festival 2024",
        "date": "2024-10-20",
        "location": "City Park",
        "description": "An outdoor music festival with top artists.",
        "map_link": "https://maps.google.com/?q=City+Park",
        "time": "12:00 PM - 11:00 PM",
        "slots": 500
    },
    {
        "id": "e3",
        "name": "Art Exhibition 2024",
        "date": "2024-11-05",
        "location": "Downtown Art Gallery",
        "description": "Explore contemporary art from global artists.",
        "map_link": "https://maps.google.com/?q=Downtown+Art+Gallery",
        "time": "10:00 AM - 06:00 PM",
        "slots": 200
    },
    {
        "id": "e4",
        "name": "Food Festival 2024",
        "date": "2024-12-15",
        "location": "Central Market",
        "description": "Taste dishes from around the world.",
        "map_link": "https://maps.google.com/?q=Central+Market",
        "time": "11:00 AM - 09:00 PM",
        "slots": 300
    },
    {
        "id": "e5",
        "name": "Film Festival 2025",
        "date": "2025-01-10",
        "location": "City Cinema",
        "description": "Watch independent and international films.",
        "map_link": "https://maps.google.com/?q=City+Cinema",
        "time": "02:00 PM - 10:00 PM",
        "slots": 150
    },
    {
        "id": "e6",
        "name": "Sports Tournament 2025",
        "date": "2025-02-20",
        "location": "Sports Complex",
        "description": "Exciting matches across multiple sports.",
        "map_link": "https://maps.google.com/?q=Sports+Complex",
        "time": "09:00 AM - 08:00 PM",
        "slots": 400
    },
    {
        "id": "e7",
        "name": "Stand-up Comedy Night",
        "date": "2025-03-15",
        "location": "Comedy Club",
        "description": "Enjoy hilarious performances.",
        "map_link": "https://maps.google.com/?q=Comedy+Club",
        "time": "08:00 PM - 11:00 PM",
        "slots": 250
    },
    {
        "id": "e8",
        "name": "Book Fair",
        "date": "2025-04-10",
        "location": "City Library",
        "description": "Discover books and meet authors.",
        "map_link": "https://maps.google.com/?q=City+Library",
        "time": "10:00 AM - 06:00 PM",
        "slots": 350
    },
    {
        "id": "e9",
        "name": "Pottery Workshop",
        "date": "2025-05-20",
        "location": "Art Studio",
        "description": "Create your own pottery pieces.",
        "map_link": "https://maps.google.com/?q=Art+Studio",
        "time": "01:00 PM - 05:00 PM",
        "slots": 50
    }
]


pages = ["Home", "Register Event", "Feedback"]

page = st.sidebar.selectbox(
    "Menu",
    pages,
    index=pages.index(st.session_state.page)
)
st.session_state.page = page


#Registration Form
def registration_form():
    with st.form("registration_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        age = st.number_input("Age", min_value=0)
        agree = st.checkbox("I agree to the terms and conditions")

        submit = st.form_submit_button("Submit")

        if submit:
            return name, email, gender, age, agree
    return None

#Feedback Form
def feedback_form():
    with st.form("feedback_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        feedback_text = st.text_area("Your Feedback")
        agree = st.checkbox("I agree to the terms")

        submit = st.form_submit_button("Submit")

        if submit:
            return name, email, feedback_text, agree
    return None


#Home Page
def home():
    st.title("Home page")

    st.write("Explore upcoming events in your city.")
    st.write("Click on 'View Details' to learn more and register.")

    colA, colB = st.columns(2)

    with colA:
        if st.button("Go to Register Page"):
            st.session_state.page = "Register Event"
            st.rerun()

    with colB:
        if st.button("Give Feedback"):
            st.session_state.page = "Feedback"
            st.rerun()

    col1, col2, col3 = st.columns(3)

    for i, event in enumerate(event_data):
        col = [col1, col2, col3][i % 3]

        with col:
            is_selected = st.session_state.selected_event == event["id"]

            border = "2px solid #4CAF50" if is_selected else "1px solid #ddd"
            bg = "#e8f5e9" if is_selected else "#fafafa"

            st.markdown(f"""
                <div style="
                    min-height:200px;
                    border:{border};
                    background-color:{bg};
                    padding:15px;
                    border-radius:12px;
                    margin-bottom:10px;
                ">
                <h4>{event['name']}</h4>
                <p>📅 {event['date']}</p>
                <p>📍 {event['location']}</p>
                </div>
            """, unsafe_allow_html=True)

            if st.button("View Details", key=event["id"]):
                st.session_state.selected_event = (
                    None if is_selected else event["id"]
                )
                st.rerun()

            if st.session_state.selected_event == event["id"]:
                st.markdown(f"""
                    <div style="
                        padding:10px;
                        border:1px solid #ccc;
                        border-radius:10px;
                        margin-bottom:10px;
                        background-color:#ffffff;
                    ">
                    <p><b>{event['description']}</b></p>
                    <p>{event['time']}</p>
                    <p><b>Slots:</b> {event['slots']}</p>
                    <a href="{event['map_link']}" target="_blank">📍 View on Map</a>
                    </div>
                """, unsafe_allow_html=True)

                if st.button("Register", key=f"reg_{event['id']}"):
                    st.session_state.selected_event_name = event["name"]
                    st.session_state.page = "Register Event"
                    st.rerun()


#Registration Page
def register_event():
    st.title("Register Event")

    event_names = [e["name"] for e in event_data]
    default_event = st.session_state.selected_event_name or event_names[0]

    event_choice = st.selectbox(
        "Select Event",
        event_names,
        index=event_names.index(default_event)
    )

    form_data = registration_form()

    if form_data:
        name, email, gender, age, agree = form_data

        if not name or not email:
            st.error("Name & Email required")
            return

        if not email.lower().endswith("@gmail.com"):
            st.error("Email must be a Gmail address")
            return

        if age < 1:
            st.error("Enter valid age")
            return

        if not agree:
            st.error("Accept terms")
            return

        st.success(f"{name}, Registration Successful for {event_choice}. See you there!")


#Feedback Page
def feedback():
    st.title("Feedback")
    st.write("Your feedback helps us improve.")

    form_data = feedback_form()

    if form_data:
        name, email, feedback_text, agree = form_data

        if not name or not email:
            st.error("Fill details")
            return

        if not email.lower().endswith("@gmail.com"):
            st.error("Invalid email")
            return

        if not feedback_text:
            st.error("Feedback cannot be empty")
            return

        if not agree:
            st.error("Accept terms")
            return

        st.success("Feedback submitted!")


if st.session_state.page == "Home":
    home()
elif st.session_state.page == "Register Event":
    register_event()
elif st.session_state.page == "Feedback":
    feedback()
