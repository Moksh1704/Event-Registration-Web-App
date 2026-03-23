#  Event Registration Web App (Streamlit)

A simple and interactive **Event Registration System** built using **Python + Streamlit**.
This app allows users to browse events, view details, register, and submit feedback — all in a clean UI.

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

---

###  Registration Page

* Pre-selects event (if navigated from Home)
* User inputs:

  * Name
  * Email
  * Gender
  * Age
* Form validation:

  * Required fields
  * Email format check
  * Terms & conditions checkbox
* Success message on submission

---

###  Feedback Page

* Users can submit feedback about events
* Includes validation and confirmation message

---

##  Concepts Used

* Streamlit UI components (`st.columns`, `st.form`, `st.session_state`)
* State management using `session_state`
* Multi-page navigation simulation
* Dynamic rendering of components
* HTML + CSS styling inside Streamlit

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit, HTML, CSS
* **State Handling:** Streamlit Session State

---

##  Project Structure

```
project/
│
├── app.py          # Main Streamlit application
├── README.md       # Project documentation
```

---

##  How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate to the project folder:

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

* Add database (SQLite / MongoDB) for storing registrations
* User authentication (login/signup)
* Event filtering (by city/category)
* Admin dashboard for event management
* Email confirmation after registration

---

 share your feedback!
