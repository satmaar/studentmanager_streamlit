"""Streamlit student grade manager for the Week 1, Day 4 assignment."""

from __future__ import annotations

import streamlit as st


def get_grade(mark: int) -> str:
    """Return the Day 2 letter grade for a whole-number mark from 0 to 100."""
    if isinstance(mark, bool) or not isinstance(mark, int):
        raise ValueError("Mark must be a whole number.")
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")

    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


def main() -> None:
    """Render the grade manager and keep its roster across Streamlit reruns."""
    st.set_page_config(page_title="Student Grade Manager", page_icon="🎓", layout="centered")
    st.title("Student Grade Manager")
    st.caption("Add student marks, view their grades, and track class results.")

    if "students" not in st.session_state:
        st.session_state.students = []

    with st.form("add_student", clear_on_submit=True):
        name = st.text_input("Name", placeholder="e.g. Divya")
        mark = st.number_input("Mark", min_value=0, max_value=100, value=0, step=1)
        submitted = st.form_submit_button("Add student", type="primary", use_container_width=True)

    if submitted:
        cleaned_name = name.strip()
        if not cleaned_name:
            st.error("Enter a student name before adding a result.")
        else:
            student_mark = int(mark)
            st.session_state.students.append(
                {"Name": cleaned_name, "Mark": student_mark, "Grade": get_grade(student_mark)}
            )
            st.success(f"Added {cleaned_name}.")

    students = st.session_state.students
    if students:
        st.subheader("Class results")
        st.table(students)

        marks = [student["Mark"] for student in students]
        average_col, highest_col, lowest_col = st.columns(3)
        average_col.metric("Class average", f"{sum(marks) / len(marks):.1f}")
        highest_col.metric("Highest mark", max(marks))
        lowest_col.metric("Lowest mark", min(marks))
    else:
        st.info("No students yet. Add the first student using the form above.")


if __name__ == "__main__":
    main()
