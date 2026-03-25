from transformers import pipeline

def summarize_text(text):
    try:
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_input = input("Enter text to summarize:\n")
    
    if len(user_input.strip()) == 0:
        print("Please enter valid text.")
    else:
        result = summarize_text(user_input)
        print("\nSummary:\n", result)
