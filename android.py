import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

chat_history = []


def detect_sentiment(message):
    score = sia.polarity_scores(message)

    compound = score['compound']

    if compound >= 0.5:
        sentiment = "Positive 😊"
    elif compound <= -0.5:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return sentiment, score

def detect_intent(message):

    message = message.lower()

    if any(word in message for word in ["hello","hi","hey"]):
        return "greeting"

    elif any(word in message for word in ["refund","return"]):
        return "refund"

    elif any(word in message for word in ["order","delivery","track"]):
        return "order"

    elif any(word in message for word in ["bad","poor","angry","complaint","issue","problem"]):
        return "complaint"

    elif any(word in message for word in ["thanks","thank you"]):
        return "thanks"

    elif any(word in message for word in ["bye","exit","quit"]):
        return "goodbye"

    return "general"

def chatbot(message):

    sentiment, score = detect_sentiment(message)
    intent = detect_intent(message)

    if intent == "greeting":
        reply = "Hello! 👋 Welcome to Customer Support. How can I assist you today?"

    elif intent == "order":

        if "Negative" in sentiment:
            reply = ("I'm sorry your order isn't meeting expectations. "
                     "Please provide your Order ID and I'll help you immediately.")
        else:
            reply = "Sure! Please provide your Order ID to check the latest status."

    elif intent == "refund":

        if "Negative" in sentiment:
            reply = ("I completely understand your frustration. "
                     "I'll help you begin the refund process.")
        else:
            reply = "I'd be happy to assist with your refund request."

    elif intent == "complaint":

        reply = ("I'm really sorry for the inconvenience you've experienced. "
                 "Your feedback is important to us, and I'll do my best to resolve this issue.")

    elif intent == "thanks":

        reply = "You're most welcome! 😊 We're always here to help."

    elif intent == "goodbye":

        reply = "Thank you for contacting us. Have a wonderful day! 👋"

    else:

        if "Positive" in sentiment:
            reply = "That's wonderful to hear! 😊 How else can I assist you today?"

        elif "Negative" in sentiment:
            reply = ("I'm sorry you're feeling this way. "
                     "Please tell me more so I can help resolve the issue.")

        else:
            reply = "Could you please explain your request in a little more detail?"

    return reply, sentiment, score, intent

print("="*70)
print(" AI CUSTOMER SUPPORT CHATBOT ")
print("="*70)
print("Type 'exit' anytime to stop.\n")

while True:

    user = input("You : ")

    if user.lower() == "exit":
        print("\nBot : Goodbye! 👋")
        break

    response, sentiment, score, intent = chatbot(user)

    timestamp = datetime.now().strftime("%H:%M:%S")

    chat_history.append({
        "time": timestamp,
        "user": user,
        "intent": intent,
        "sentiment": sentiment,
        "confidence": round(score["compound"],2),
        "bot": response
    })

    print("\n----------- Analysis -----------")
    print("Intent      :", intent)
    print("Sentiment   :", sentiment)
    print("Confidence  :", round(score["compound"],2))
    print("--------------------------------")
    print("Bot :", response)
    print()

# Save Chat History

with open("chat_history.txt","w",encoding="utf-8") as file:

    for chat in chat_history:

        file.write(f"\n[{chat['time']}]\n")
        file.write(f"User      : {chat['user']}\n")
        file.write(f"Intent    : {chat['intent']}\n")
        file.write(f"Sentiment : {chat['sentiment']}\n")
        file.write(f"Confidence: {chat['confidence']}\n")
        file.write(f"Bot       : {chat['bot']}\n")
        file.write("-"*60+"\n")

print("Chat history saved as chat_history.txt")