from typing import List
from langchain.text_splitter import CharacterTextSplitter


class Transformer:

    def __init__(self, path):
        self.path = path

    def chunkify(self, text: str) -> List[str]:
        """
        Chunkify the text into paragraphs.

        Parameters:
            text (str): The input text.

        Returns:
            List[str]: The list of paragraphs.
        """

        text_splitter = CharacterTextSplitter(
            separator="\n\n",
            chunk_size=256,
            chunk_overlap=20
        )
        docs = text_splitter.create_documents([text])
        return docs

    def get_embeddings(self):
        pass
