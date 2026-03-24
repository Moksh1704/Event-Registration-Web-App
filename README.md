#  Event Registration Web App (Streamlit)

A responsive and interactive **Event Registration System** built using **Python and Streamlit**.
This application allows users to explore events, view details, register seamlessly, and provide feedback — all within a clean and user-friendly interface.

---

##  Features

### Home Page

* Displays events in a **card-based grid layout**
* Each card shows:

  * Event Name
  * Date
  * Location
* **View Details toggle** to expand event information
* **Dynamic card highlighting** when selected
* **Register button** redirects to registration page
* Quick navigation buttons (mobile-friendly)

---

###  Registration Page

* Automatically selects event when navigated from Home
* User inputs:

  * Name
  * Email
  * Gender
  * Age
* Form validation:

  * Required fields
  * Email format check
  * Terms & conditions
* Success message after submission

---

###  Feedback Page

* Submit feedback or complaints
* Input validation and confirmation message

---

##  Key Concepts Used

* Streamlit components:

  * `st.columns`, `st.button`, `st.selectbox`, `st.form`
* **Session State (`st.session_state`)**

  * Used for navigation and UI persistence
* Multi-page navigation using state
* Conditional rendering of UI
* HTML + CSS styling inside Streamlit
* Mobile-friendly UX improvements

---

##  Tech Stack

* **Frontend:** Streamlit, HTML, CSS
* **State Management:** Streamlit Session State

---

## Project Structure

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
git clone https://github.com/your-username/Event-Registration-Web-App.git
```

2. Navigate to the project folder:

```
cd Event-Registration-Web-App
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
* Event filtering (by city/category)
* Admin dashboard
* Email confirmation system

---

