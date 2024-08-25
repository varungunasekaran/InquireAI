from transformers import pipeline

# Load the pre-trained model for question-answering
qa_pipeline = pipeline("question-answering")

def answer_question(context, question):
    """Uses the Hugging Face pipeline to answer a question based on context."""
    result = qa_pipeline({
        'context': context,
        'question': question
    })
    return result['answer']
