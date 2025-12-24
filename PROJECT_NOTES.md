# Mood–Sleep–Focus–Task–Music → Productivity Decision Engine

## 1. Problem Statement

People often choose tasks and music based on intuition, without understanding how their
**mood, sleep, focus, task type, and music environment** affect productivity.

This project builds a **decision-support system** that:
- Predicts session-level productivity
- Explains *why* productivity is high or low
- Helps users choose suitable task difficulty and music type

The goal is **not just prediction**, but **interpretable decision-making**.

---

## 2. Scope of the Project

- Models **short work sessions (2–4 hours)**
- Focuses on individual productivity per session
- Does not model long-term burnout or health outcomes
- Designed for:
  - Coding
  - Studying
  - Creative work
  - Routine tasks

---

## 3. What One Row of Data Represents

> One row represents **one work session of a person on a given day**.

Each row captures:
- Mental state
- Physical readiness
- Task context
- Environmental influence
- Final productivity outcome

---

## 4. Dataset Columns

| Column Name | Description |
|------------|-------------|
| `mood` | Emotional state of the user |
| `sleep_hours` | Hours of sleep before the session |
| `focus_level` | Self-reported focus (1–10) |
| `task_type` | Type of task being performed |
| `music_type` | Music environment during the session |
| `productivity_score` | Final productivity score (0–100) |

---

## 5. Assumptions

- Mood and focus are self-reported and subjective
- Productivity score is an approximate indicator, not absolute truth
- Sleep affects **endurance**, not initial sharpness
- Focus represents short-term attention
- Music changes cognitive load differently for different tasks

---

## 6. Core Rules Used to Generate Data

### 6.1 Mood Rules

| Mood | Effect |
|-----|-------|
| Calm | High mental stability, best for analytical tasks |
| Happy | Motivating, better for creative tasks |
| Anxious | Reduces clarity and consistency |
| Stressed | High effort but higher error rate |
| Sad | Lower motivation and engagement |

---

### 6.2 Sleep Rules

| Sleep Hours | Effect on Productivity |
|------------|------------------------|
| < 4 hrs | Severe productivity drop |
| 4–5 hrs | Strong penalty |
| 5–6 hrs | Mild penalty |
| 6–8 hrs | Optimal range |
| > 8 hrs | No additional benefit |

**Key insight:**  
Sleep caps the *maximum achievable productivity*.

---

### 6.3 Focus Rules

| Focus Level | Interpretation |
|------------|----------------|
| 1–3 | Distracted |
| 4–6 | Average |
| 7–8 | Strong focus |
| 9–10 | Hyperfocus (unstable) |

High focus improves productivity **only when sleep is sufficient**.

---

### 6.4 Task Type Rules

| Task Type | Characteristics |
|----------|----------------|
| Coding | Requires calm mood and good sleep |
| Study | Requires focus and emotional stability |
| Creative | Tolerates low sleep better |
| Routine | Least affected by mood |

---

### 6.5 Music Rules

| Music Type | Effect |
|-----------|--------|
| Instrumental | Best for coding |
| Lofi | Supports long sessions |
| Lyrical | Increases cognitive load |
| Silence | Helps during anxiety or overstimulation |

---

## 7. Interaction Rules (Critical Logic)

These rules model **real-world trade-offs**.

### Sleep × Focus
- High focus cannot fully compensate for low sleep
- Low sleep caps productivity even if focus is high

### Mood × Task
- Calm + coding → strong positive effect
- Happy + creative → strong positive effect
- Anxious + analytical tasks → negative effect

### Music × Task
- Lyrical music harms analytical tasks
- Instrumental music supports coding tasks

### Sleep × Task
- Creative tasks tolerate low sleep better than analytical tasks

---

## 8. Productivity Score Construction Logic

### Step 1: Base Score from Focus

base_score = focus_level × 10

---

### Step 2: Sleep Adjustment
sleep < 4 hrs → −25 

4–5 hrs → −15

5–6 hrs → −8

≥ 6 hrs → 0

---

### Step 3: Mood Adjustment

calm → +10

happy → +5

neutral → 0

anxious → −10

stressed → −15

sad → −12

---

### Step 4: Task Suitability Adjustment (Examples)

coding + calm → +8

coding + anxious → −10

creative + happy → +8

routine tasks → 0


---

### Step 5: Music Adjustment

instrumental + coding → +5

lofi → +3

lyrical + coding → −8

silence + anxious → +6

---

### Step 6: Caps and Constraints

- If `sleep_hours < 5` → productivity ≤ 65
- If `sleep_hours < 4` → productivity ≤ 50
- Final score constrained between 0 and 100

---

### Final Formula

productivity_score =
base_score + sleep_adjustment + mood_adjustment + task_adjustment + music_adjustment

---

## 9. Productivity Score Interpretation

| Score Range | Meaning |
|------------|---------|
| 80–100 | Highly productive session |
| 60–79 | Good session |
| 40–59 | Average / struggling |
| < 40 | Poor session |

---

## 10. Modeling Philosophy

Machine learning models are **not treated as oracles**.

They are combined with:
- Rule-based constraints
- Domain logic
- Explainability

This improves realism, trust, and decision usefulness.

---

## 11. Limitations

- Dataset is simulated
- Mood and focus are subjective
- Long-term fatigue not modeled
- Individual personalization not included

---

## 12. Future Improvements

- User-level personalization
- Real-world data collection
- Time-series modeling
- Adaptive learning from past sessions

---

## Why This Project Is Strong

- Clear assumptions
- Human-realistic logic
- Explicit interaction rules
- Explainable productivity decisions
- Industry-relevant reasoning
