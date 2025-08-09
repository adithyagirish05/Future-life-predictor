import random
import time

futures = [
    "You will own a flying car and live on Mars.",
    "Robots will make you breakfast every day.",
    "You’ll have an AI personal assistant smarter than Einstein.",
    "Virtual reality will be your new workplace.",
    "You will have a pet dinosaur cloned from DNA.",
    "Your house will be completely automated, including mood-based lighting.",
    "You will teleport to work instead of commuting."
]

def futuristic_typing(text):
    """Simulate typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def predict_future(name):
    futuristic_typing(f"🔮 Hello {name}, scanning your future...")
    time.sleep(2)
    prediction = random.choice(futures)
    futuristic_typing(f"✨ Prediction: {prediction}")

if __name__ == "__main__":
    futuristic_typing("Welcome to the Future Life Predictor 3000 🚀")
    user_name = input("Enter your name: ")
    predict_future(user_name)
