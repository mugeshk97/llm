from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Input
input_text = input("Enter your question: ")

# LLM Model
llm = Ollama(model="mistral")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Generating Response
response = chain.invoke({"question": input_text})

print(response)
