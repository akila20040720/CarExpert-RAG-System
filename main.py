import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document

def load_car_expert_script(url, vehicle_model):
    response = requests.get(url)
    soup = BeautifulSoup(response.content , "html.parser")
    script_raw = soup.find("pre").get_text()

    return Document(page_content=script_raw, metadata={"title": vehicle_model})


def main():
    print("Hello from carexpert-rag-system!")


if __name__ == "__main__":
    main()
