
def load_and_chunk_document():
    with open("knowledge_base/disk_troubleshooting.md","r") as file:
        document= file.read()
    cleaned_chunks=[]
    chunks= document.split("##")
   


    for chunk in chunks[1:]:
        
        cleaned_chunks.append(chunk.strip())
       

    return cleaned_chunks   
