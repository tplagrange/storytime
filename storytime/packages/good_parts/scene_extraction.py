from transformers import pipeline

# Use a summarization or zero-shot classification pipeline to get the main scene
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def scene_from_text(raw_text):
    # Summarize the text to get the main scene description
    summary = summarizer(raw_text, max_length=50, min_length=5, do_sample=False)[0]['summary_text']
    
    prompt = f"A water-color style chidlren's book illustration of the following scene: {summary}"
    return prompt