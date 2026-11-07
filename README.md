# Student Grade Manager

A single-file Streamlit app for the Week 1, Day 4 assignment. It uses the Day 2 grading scale,
stores the roster in `st.session_state`, shows a result table, and calculates class average,
highest, and lowest marks.

## Set up and run

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run grade_app.py
```

Marks are whole numbers from 0 to 100. The interface prevents values outside that range and the
form rejects blank names.

## Verify

```bash
python -m pip install -r requirements-dev.txt
pytest -q
```

The automated checks cover the Day 2 grade boundaries, invalid marks, session-state persistence,
class metrics, and blank-name validation. Browser evidence is in `evidence/`.

## Submission notes

The assignment asks for a screenshot with several students and a one-line note about the issue
before using `st.session_state`. Suggested note: “A normal Python list reset on every Streamlit
rerun, so earlier students disappeared; storing the list in `st.session_state` kept it between
interactions.”
