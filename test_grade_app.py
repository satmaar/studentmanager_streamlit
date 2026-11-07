from streamlit.testing.v1 import AppTest

from grade_app import get_grade


def test_day_two_grading_scale_boundaries() -> None:
    assert [get_grade(mark) for mark in (0, 59, 60, 69, 70, 79, 80, 89, 90, 100)] == [
        "E", "E", "D", "D", "C", "C", "B", "B", "A", "A"
    ]


def test_grade_rejects_out_of_range_and_non_integer_marks() -> None:
    for mark in (-1, 101, 82.5, True):
        try:
            get_grade(mark)  # type: ignore[arg-type]
        except ValueError:
            continue
        raise AssertionError(f"Expected {mark!r} to be rejected")


def test_app_keeps_students_and_updates_results_after_form_submissions() -> None:
    app = AppTest.from_file("grade_app.py", default_timeout=10).run()
    assert len(app.info) == 1

    for name, mark in (("Priya", 92), ("Arun", 78), ("Divya", 59)):
        app.text_input[0].set_value(name)
        app.number_input[0].set_value(mark)
        app.button[0].click().run()

    assert len(app.session_state["students"]) == 3
    assert [student["Grade"] for student in app.session_state["students"]] == ["A", "C", "E"]
    assert len(app.table) == 1
    assert [metric.label for metric in app.metric] == ["Class average", "Highest mark", "Lowest mark"]
    assert [metric.value for metric in app.metric] == ["76.3", "92", "59"]


def test_blank_name_is_rejected() -> None:
    app = AppTest.from_file("grade_app.py", default_timeout=10).run()
    app.text_input[0].set_value("   ")
    app.number_input[0].set_value(83)
    app.button[0].click().run()

    assert app.session_state["students"] == []
    assert any("Enter a student name" in error.value for error in app.error)
