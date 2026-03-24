#  Event Registration Web App (Streamlit)

A responsive and interactive **Event Registration System** built using **Python and Streamlit**.
This application allows users to explore events, register seamlessly, and provide feedback — with a clean UI and smooth navigation.

---

##  Features

###  Home Page

* Displays events in a **card-based grid layout**
* Shows:

  * Event Name
  * Date
  * Location
* Expandable **View Details** section
* **Register button** redirects to registration page
* Quick Navigation Buttons for mobile-friendly access

---

###  Registration Page

* Automatically selects event when navigated from Home
* User inputs:

  * Name
  * Email
  * Gender
  * Age
* Validation:

  * Required fields
  * Email format check
  * Terms & conditions
* Displays confirmation message

---

###  Feedback Page

* Users can submit feedback or complaints
* Input validation and confirmation message

---

##  Key Concepts Used

* Streamlit components (`st.columns`, `st.form`, `st.button`)
* **Session State (`st.session_state`) for state management**
* Multi-page navigation using sidebar + state
* Dynamic UI rendering
* HTML + CSS styling inside Streamlit
* Mobile-friendly navigation improvements

---

##  Tech Stack

* **Frontend:** Streamlit, HTML, CSS
* **State Management:** Streamlit Session State

---

##  Project Structure

```
project/
│
├── app.py          # Main Streamlit application
├── README.md       # Documentation
```

---
## Deployed at 

- https://eventsregistration.streamlit.app/
---

##  How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate to project folder:

```
cd your-repo-name
```

3. Install dependencies:

```
pip install streamlit
```

4. Run the app:

```
streamlit run app.py
```

---

##  Future Improvements

* Database integration (SQLite / MongoDB)
* User authentication (Login/Signup)
* Event filtering (city/category)
* Admin dashboard
* Email confirmation system

---
