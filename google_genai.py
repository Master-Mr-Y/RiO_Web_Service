from google import genai as gen

key = "AIzaSyBn6tCxD-X-GkvgtIoEFj-wDV5VFuJAcAM"

Client = gen.Client(api_key=key)

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

