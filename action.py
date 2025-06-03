import datetime
import speak
import webbrowser
import weather
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
import google.generativeai as genai

def open_youtube_video(video_name):
    api_key = ""
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=video_name
    )
    response = request.execute()

    if 'items' in response:
        video_id = response['items'][0]['id']['videoId']
        url = f"https://www.youtube.com/watch?v={video_id}"
        webbrowser.open(url)
    else:
        print("Video not found")

load_dotenv()
genai.configure(api_key=os.environ[""])
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

def Action(send) :   
  
    data_btn  = send.lower()
    command  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play" in data_btn or "song" in data_btn:
        open_youtube_video(data_btn[5:])
        speak.speak("Playing "+data_btn[5:]+" on Youtube")                   
        return "Playing "+data_btn[5:]+" on Youtube"

    elif 'open calculator' in data_btn or 'calculator'  in data_btn:
        os.system("calc")
        speak.speak("Calculator open")  
        return "Calculator open"
    
    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans
        
            
    elif 'open chrome' in command:
        speak.speak("Opening "+command[5:])
        webbrowser.open("www.google.com")
    
    elif "open" in command:
        speak.speak("Opening "+command[5:])
        webbrowser.open("www."+command[5:]+".com")
    
    elif "search" in command:
        speak.speak("searching "+command[7:]+" on google")
        webbrowser.open("https://www.google.com/search?q="+command[7:])
    
    elif any(word in command for word in ["who", "what", "when", "where", "how", "should", "why", "will", "would", "can", "could", "do", "does", "is", "are", "am", "was", "were", "have", "has", "had", "which",]):
        response = chat_session.send_message(command)
        speak.speak(response.text)
        
                
                
    else :
        speak.speak( "I'm unable to understand!")
        return "i'm unable to understand!"       

