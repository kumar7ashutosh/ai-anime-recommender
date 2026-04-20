from src.data_loader import DataLoader
from src.vectorstore import VectorStore
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException
load_dotenv()

logger=get_logger(__name__)

def main():
    logger.info("starting to build pipeline...")
    loader=DataLoader(old_file="data/anime_with_synopsis.csv",new_file="data/updated.csv")
    processed_csv=loader.load_and_process()
    logger.info("data loaded and processed")
    vectorstore_builder=VectorStore(csv_path="data/updated.csv",persist_dir="chroma_db")
    vectorstore_builder.build_and_save_vectorstore()
    logger.info("vector store built successfully")
    logger.info("pipeline built successfully")
    
if __name__=="__main__":
    main()
    