import wikipedia
import nltk

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Set Wikipedia language (optional)
wikipedia.set_lang("en")

# Function to fetch answer from Wikipedia
def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your question is a bit broad. Maybe try: {e.options[0]}"
    except wikipedia.exceptions.PageError:
        return "I couldn't find anything on that. Try rephrasing your question."
    except Exception as e:
        return f"Oops! Something went wrong: {e}"

# Chat loop
print("Hi! I'm a general knowledge bot powered by Wikipedia. Ask me anything!")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Bot: Goodbye! Come back for more quick facts anytime.")
        break
    else:
        response = get_wikipedia_summary(user_input)
        print("Bot:", response)
