import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 1. Metin dosyasını yüklüyoruz
loader = TextLoader("docs/bigi.txt", encoding="utf-8")
documents = loader.load()

# 2. Metni parçalara bölüyoruz
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# 3. Embedding ve LLM modellerini tanımlıyoruz (Modeli Llama3 yaptık!)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = ChatOllama(model="llama3", temperature=0.1)

# 4. Vektör tabanını oluşturuyoruz
vectorstore = Chroma.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 5. Prompt şablonunu hazırlıyoruz
template = """Yalnızca aşağıdaki bağlamı kullanarak soruyu kısa ve net bir şekilde Türkçe yanıtla. Bağlamda yoksa "Bilmiyorum" de.

Bağlam:
{context}

Soru: {question}
Cevap:"""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# RAG zincirini kuruyoruz
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("RAG Sistemi Hazir!")

# 6. İnteraktif Soru-Cevap Döngüsü
print("\n--- Gaziantep RAG Asistanı Aktif (Llama 3)! Çıkmak için 'q' yazabilirsin. ---\n")

while True:
    soru = input("Sorunuz: ")
    if soru.lower() == 'q':
        print("Sistemden çıkılıyor...")
        break
    
    cevap = rag_chain.invoke(soru)
    print(f"Cevap: {cevap}\n" + "-"*50)