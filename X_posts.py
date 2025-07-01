import schedule
import time
from datetime import datetime
import tweepy



daily_messages = {
    'Monday': "Start the week strong! 💪 #MondayMotivation",
    'Tuesday': "Keep grinding! You're doing great. 🔥 #TuesdayThoughts",
    'Wednesday': "Midweek check-in: How are you doing? 💬 #WellnessWednesday",
    'Thursday': "Almost there! Stay focused. 💼 #ThursdayVibes",
    'Friday': "It's Friday! Celebrate your wins! 🎉 #FridayFeeling",
    'Saturday': "Take time to relax and recharge. 😌 #SelfCareSaturday",
    'Sunday': "Reflect, plan, and prepare for the week ahead. ✍️ #SundayReflection"
}


def post_to_x(text_content: str) -> bool:
    if not text_content.strip():
        print(" Cannot post empty content.")
        return False

    try:
        client = tweepy.Client(
            consumer_key=X_API_KEY,
            consumer_secret=X_API_SECRET,
            access_token=X_ACCESS_TOKEN,
            access_token_secret=X_ACCESS_TOKEN_SECRET
        )

        print(f" Posting to X: {text_content}")
        response = client.create_tweet(text=text_content)

        if response.data and 'id' in response.data:
            print(f" Post successful! Tweet ID: {response.data['id']}")
            return True
        else:
            print(f" Unexpected response: {response}")
            return False
    except Exception as e:
        print(f" Failed to post to X: {e}")
        return False

# --- Daily Post Scheduler ---
def daily_fixed_post():
    today = datetime.now().strftime('%A')
    message = daily_messages.get(today)
    if message:
        print(f"\n Posting scheduled message for {today}")
        post_to_x(message)
    else:
        print(f" No message set for {today}.")

# --- Schedule ---
schedule.every().day.at("10:38").do(daily_fixed_post)

print(" AI agent running. Will post every day at 10:38 AM...\n")

# --- Keep Running ---
while True:
    schedule.run_pending()
    time.sleep(30)
