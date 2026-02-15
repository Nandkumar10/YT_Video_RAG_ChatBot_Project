from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import re
from dotenv import load_dotenv
load_dotenv()

def extract_video_id(url: str) -> str:
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)

    if not match:
        raise ValueError("Invalid YouTube URL")

    return match.group(1)


def ask_video(youtube_url: str, question: str):


        #url = "LPZh9BOjkQs"
        video_id = extract_video_id(youtube_url)

        try:
                Fetched = YouTubeTranscriptApi().fetch(video_id=video_id, languages=["en"])
                transcript_list = Fetched.to_raw_data()
                
                transcript = " ".join(chunk['text'] for chunk in transcript_list)
                #print(transcript)

        except  TranscriptsDisabled:
                print("No captions available for this video")

        splitter = RecursiveCharacterTextSplitter(
                chunk_size=250,
                chunk_overlap=50
        )
        chunks = splitter.create_documents([transcript])
        print("The length of the chunks:" ,len(chunks))


        embedding = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

        vector_store = FAISS.from_documents(chunks, embedding)
        #print(vector_store.index_to_docstore_id)

        retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
                "k": 3,
        }
        )


        llm = HuggingFaceEndpoint(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        task="conversational"
        )

        model = ChatHuggingFace(llm=llm)


        prompt = PromptTemplate(
                template= """
        You are a helpfull youtube video assistent .
        Ans from the provided video transcript context in simple way.
        If the context is insufficient, just say don't know.

        {context}

        Question: {question}""",
        input_variables= ['context', 'question']
        )


        def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)


        parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
        })

        parser = StrOutputParser()
        main_chain = parallel_chain | prompt | model | parser
        return main_chain.invoke(question)
