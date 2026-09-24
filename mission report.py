# Sentiment Spy - Mission Report

positive_words = ["good", "great", "happy", "love", "amazing", "excellent"]
negative_words = ["bad", "sad", "hate", "angry", "terrible", "awful"]

history = []
positive = 0
negative = 0
neutral = 0

def analyze_sentiment(text):
    words = text.lower().split()

    pos = sum(word in positive_words for word in words)
    neg = sum(word in negative_words for word in words)

    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"


print("Sentiment Spy Chatbot")
print("Type 'help' to see commands.")
print("Type 'exit' to finish.")

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("\n--- Final Sentiment Report ---")
        print("Positive:", positive)
        print("Negative:", negative)
        print("Neutral:", neutral)
        print("Total messages:", len(history))
        break

    elif user.lower() == "help":
        print("Commands:")
        print("  stats   - Show sentiment statistics")
        print("  history - Show conversation history")
        print("  reset   - Reset the data")
        print("  exit    - Exit and show final report")

    elif user.lower() == "stats":
        print("\nSentiment Statistics:")
        print("Positive:", positive)
        print("Negative:", negative)
        print("Neutral:", neutral)

    elif user.lower() == "history":
        print("\nConversation History:")
        for message, sentiment in history:
            print(message, "->", sentiment)

    elif user.lower() == "reset":
        history.clear()
        positive = 0
        negative = 0
        neutral = 0
        print("All data has been reset.")

    else:
        sentiment = analyze_sentiment(user)

        history.append((user, sentiment))

        if sentiment == "positive":
            positive += 1
        elif sentiment == "negative":
            negative += 1
        else:
            neutral += 1

        print("Sentiment:", sentiment)
