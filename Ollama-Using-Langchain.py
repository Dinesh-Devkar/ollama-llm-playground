from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



## simple chat ollama
# llm=ChatOllama(model='gemma3:4b')

# response=llm.invoke("who is the prime minister of india")
# print(response)


## ollama with chains

# prompt=PromptTemplate(template="""you are a most demotivational assistent who answer user queries in demotivational way : {query}""",
#                       input_variables=['query'])

# llm=ChatOllama(model='gemma3:4b')

# chain = prompt | llm

# response=chain.invoke('what is black hole')

# print(response)


## system messages and user messages

# messages=[
#     ('system','you are a funny assistent'),
#     ('user','tell me about python functions')
# ]

# messages=[
#     SystemMessage(content='you are a funny assistent'),
#     HumanMessage(content='what is solar system')
# ]

# llm=ChatOllama(model='gemma3:4b')

# response=llm.invoke(messages)

# print(response.content)


## Stream the response in real time

# llm=ChatOllama(model='gemma3:4b')
# for chunk in llm.stream("who is sachin tendulkar"):
#     print(chunk.content, end="", flush=True)

# print()


## Generate responses for multiple inputs using batch()

# llm = ChatOllama(model="gemma3:4b")

# questions = [
#     "What is Python? in two lines.",
#     "What is machine learning? in two lines",
#     "What is deep learning? in two lines"
# ]

# responses = llm.batch(questions)

# print(responses)

# for question, response in zip(questions, responses):
#     print("Question:", question)
#     print("Answer:", response.content)
#     print("-" * 50)


##  Use prompt templates and chains
llm = ChatOllama(model="gemma3:4b", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a tutor who explains topics in simple language."),
    ("human", "Explain {topic} for a {audience}.")
])

chain = prompt | llm | StrOutputParser()

result = chain.invoke({
    "topic": "decorators in Python",
    "audience": "beginner"
})

print(result)