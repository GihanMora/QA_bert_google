from transformers import pipeline

# Open and read the article
question = "What is the capital of the Netherlands?"
context = r"The four largest cities in the Netherlands are Amsterdam, Rotterdam, The Hague and Utrecht.[17] Amsterdam is the country's most populous city and nominal capital,[18] while The Hague holds the seat of the States General, Cabinet and Supreme Court.[19] The Port of Rotterdam is the busiest seaport in Europe, and the busiest in any country outside East Asia and Southeast Asia, behind only China and Singapore."

# Generating an answer to the question in context
qa = pipeline("question-answering")#utilizes the DistilBERT model fine-tuned to SQuAD.
answer = qa(question=question, context=context)

# Print the answer
print(f"Question: {question}")
print(f"Answer: '{answer['answer']}' with score {answer['score']}")