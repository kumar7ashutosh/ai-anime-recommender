from src.vectorstore import VectorStore
from src.recommender import recommend
from config.config import OPENAI_API_KEY,MODEL_NAME
from utils.custom_exception import CustomException
from utils.logger import get_logger
import os
logger=get_logger(__name__)

class recommendpipeline:
    def __init__(self,persist_dir="chroma_db"):
        logger.info("initializing recommendation pipeline")
        vector_build=VectorStore(csv_path="",persist_dir=persist_dir)
        retriever=vector_build.load_vectorstore().as_retriever()
        self.recommender=recommend(retriever=retriever,api_key=OPENAI_API_KEY,model_name=MODEL_NAME)
        logger.info("pipeline initialized")
        
    def recommend(self,query:str)->str:
        logger.info(f"received a query {query}")
        recommendation=self.recommender.get_recommendation(query)
        logger.info("Recommendation generated successfully...")
        return recommendation
    
    