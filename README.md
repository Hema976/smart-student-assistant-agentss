# Smart Student Assistant (SSA)

A simple multi-agent system that helps students with:
- Study plan generation
- PDF notes summarization
- Doubt solving
- Master agent routing

### Agents Included
1. Planner Agent – Creates a 7-day weekly study plan  
2. Notes Agent – Extracts & summarizes text from PDF  
3. Doubt Solver Agent – Answers short academic questions  
4. Master Agent – Decides which agent to run

---

## Problem Statement
Students waste time:
- Planning weekly study
- Reading long PDFs
- Searching for small doubts

SSA automates these tasks using simple Python agents.

---

## Solution Summary

| Agent          | Responsibility                      |
|----------------|--------------------------------------|
| Planner Agent  | Weekly study plan                    |
| Notes Agent    | PDF extract + summary                |
| Doubt Agent    | Answers basic questions              |
| Master Agent   | Routes tasks correctly               |

---

## Architecture
User → Master Agent → (Planner / Notes / Doubt) → Output

---

## Code Overview
- planner.py → study plan generation  
- notes_agent.py → PDF extract + LexRank summary  
- doubt_solver.py → Q&A  
- master_agent.py → controller agent  

---

## How To Use (in Kaggle Notebook)
1. Upload code files or paste code  
2. Run:
