from langchain.chat_models import init_chat_model
from src.prompt_template import get_anime_prompt

class recommend:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm=init_chat_model(model=model_name,temperature=0)
        self.prompt=get_anime_prompt()
        self.retriever=retriever
        self.chain=({
                "context": lambda x: self.retriever.invoke(x["question"]),
                "question": lambda x: x["question"]
            }
            | self.prompt
            | self.llm)
    def get_recommendation(self,question:str):
        return self.chain.invoke({"question":question}).content
        