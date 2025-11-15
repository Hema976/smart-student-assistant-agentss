from planner import generate_study_plan
from notes_agent import summarize_text, extract_text_from_pdf
from doubt_solver import answer_doubt

def smart_student_assistant(task, data=None):

    if task == "plan":
        return generate_study_plan(data)

    if task == "summary":
        return summarize_text(data)

    if task == "pdf_summary":
        text = extract_text_from_pdf(data)
        return summarize_text(text)

    if task == "doubt":
        return answer_doubt(data)

    return "Invalid task"
