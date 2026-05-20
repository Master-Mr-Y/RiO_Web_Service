from google import genai 

key = "AIzaSyBUVYakgIP5sJe4vT2GU1ksiVrQ-cisRiY"

Client = genai.Client(api_key=key)

chat_session = Client.chats.create(
    model = "gemini-2.5-flash",
    config = {
        "system_instruction" : """
        
        speak only tamil no tanglish,
        call the user "Macha"
        
        """
    }
)

def engine(qurry):
    
    response = chat_session.send_message(qurry)
    
    return response.text





