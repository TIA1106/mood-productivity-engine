import random
import pandas as pd


def get_sleep_penalty(sleep):
    if sleep < 4:
        return -25
    elif sleep < 5:
        return -15
    elif sleep < 6:
        return -8
    return 0


def get_mood_adjustment(mood):
    if mood == "calm":
        return 10
    if mood == "happy":
        return 5
    if mood == "anxious":
        return -10
    if mood == "stressed":
        return -15
    if mood == "sad":
        return -12
    return 0


def get_task_adjustment(task, mood):
    if task == "coding" and mood == "calm":
        return 8
    if task == "coding" and mood in ["anxious", "stressed"]:
        return -10
    if task == "creative" and mood == "happy":
        return 8
    return 0


def get_music_adjustment(music, task, mood):
    if music == "instrumental" and task == "coding":
        return 5
    if music == "lyrical" and task == "coding":
        return -8
    if music == "lofi":
        return 3
    if music == "silence" and mood in ["anxious", "stressed"]:
        return 6
    return 0


def apply_sleep_caps(score, sleep):
    if sleep < 4:
        return min(score, 50)
    if sleep < 5:
        return min(score, 65)
    return score


def calculate_productivity(mood, sleep, focus, task, music):
    score = focus * 10
    score += get_sleep_penalty(sleep)
    score += get_mood_adjustment(mood)
    score += get_task_adjustment(task, mood)
    score += get_music_adjustment(music, task, mood)
    score = apply_sleep_caps(score, sleep)
    return max(0, min(100, score))

def main():
    moods = ["calm", "happy", "anxious", "stressed", "sad"]
    tasks = ["coding", "study", "creative", "routine"]
    music_types = ["instrumental", "lofi", "lyrical", "silence"]

    rows = []

    for _ in range(1000):
        mood = random.choice(moods)
        task = random.choice(tasks)
        music = random.choice(music_types)
        sleep = round(random.uniform(3, 9), 1)
        focus = random.randint(1, 10)
        productivity = calculate_productivity(mood=mood,sleep=sleep,focus=focus,task=task,music=music)
        rows.append([mood,sleep,focus,task,music,productivity])
    df = pd.DataFrame(rows, columns=["mood","sleep_hours","focus_level","task_type","music_type","productivity_score"])
    df.to_csv("data/raw_data.csv", index=False)
    print("Dataset generated: data/raw_data.csv")
if __name__ == "__main__":
    main()
