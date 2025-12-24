import streamlit as st
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
st.set_page_config(
    page_title="Productivity Predictor",
    layout="centered"
)
df = pd.read_csv("data/raw_data.csv")

X = df.drop("productivity_score", axis=1)
y = df["productivity_score"]

categorical_cols = ["mood", "task_type", "music_type"]
numerical_cols = ["sleep_hours", "focus_level"]
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=200,
            random_state=42
        ))
    ]
)

# Train on full dataset (demo purpose)
model.fit(X, y)
st.title("🎯 Productivity Predictor")

st.markdown(
    """
    Predict **session-level productivity** based on mood, sleep,
    focus level, task type, and music preference.
    """
)

with st.form("prediction_form"):
    mood = st.selectbox("Mood", df["mood"].unique())
    task = st.selectbox("Task Type", df["task_type"].unique())
    music = st.selectbox("Music Type", df["music_type"].unique())

    sleep = st.slider("Sleep Hours", 3.0, 9.0, 6.5)
    focus = st.slider("Focus Level", 1, 10, 6)

    submit = st.form_submit_button("Predict Productivity")
if submit:
    input_df = pd.DataFrame([{
        "mood": mood,
        "sleep_hours": sleep,
        "focus_level": focus,
        "task_type": task,
        "music_type": music
    }])

    prediction = model.predict(input_df)[0]

    st.metric(
        label="Predicted Productivity Score",
        value=f"{prediction:.1f} / 100"
    )

    if prediction >= 75:
        st.success("🔥 High productivity expected!")
    elif prediction >= 40:
        st.warning("⚖️ Moderate productivity expected.")
    else:
        st.error("⚠️ Low productivity expected.")
st.markdown("---")
st.caption("Built with Python, Scikit-learn, and Streamlit")
