from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
#import dotenv

#Load environment variables from .env file
#dotenv.load_dotenv()
#OPENAI_API_KEY = dotenv.get_key(dotenv.find_dotenv(), "OPENAI_API_KEY") 

#ChatOpenAI initialization
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=OPENAI_API_KEY, temperature=0.7)

#Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

#Output string parser
output_parser = StrOutputParser()

#LLM chain
chain = prompt | llm | output_parser

#Title
st.title("인공지능 시인")

#시 주제 입력 필드
content = st.text_input("시의 주제를 제시해주세요")
st.write("시의 주제는", content)

#시 작성 요청하기
if st.button("시 작성 요청하기"):
    with st.spinner("시를 작성하는 중입니다..."):
        result = chain.invoke({"input": content + "에 대한 시를 써줘"})
        st.write(result)
