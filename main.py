# main.py (place this in C:\Users\ASUS\Downloads\mlproject\)
import sys
import os

# Add src to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    print("Starting ML Project...")
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()
    print(f"Data ingestion completed!")
    print(f"Train data: {train_path}")
    print(f"Test data: {test_path}")