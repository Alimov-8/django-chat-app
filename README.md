# Chat Application System 💬
[Django Channels Documentation](https://channels.readthedocs.io/en/stable/introduction.html)
  ### Development Porcess
    📌 Add Channels to your project
    📌 Build a WebSocket consumer and appropriate routing
    📌 Implement a WebSocket client
    📌 Enable a channel layer with Redis
    📌 Make your consumer fully asynchronous
    📌 Models to save and load data by some attribute
    📌 JS onopen, onclick and etc.

  ### Resources 
    🔗 https://channels.readthedocs.io/en/stable/tutorial/part_1.html
    🔗 Django3 by examples Book
    🔗 https://www.youtube.com/watch?v=xrKKRRC518Y
 #
 ### Getting Started
    • Setup Dev Environment
    • Setup django, redis:5, channels and redis-channel with given requirment, docker
   
   
   #
   ##### ↪️ Commits:
    • auth and chats created | asgi modified 
        ASGI, which can handle WebSocket requests as well. ASGI is the emerging Python
        standard for asynchronous web servers and applications.
        The Django Channels request/response cycle
         
    • Writing consumer | routing | asgi
        Consumers are the equivalent of Django views for asynchronous applications.
        Channels provides routing classes that allow you to combine
        and stack consumers to dispatch based on what the connection is. You can think
        of them as the URL routing system of Django for asynchronous applications.
        Add routings to config routings
    
    • Implementing the WebSocket client
    
    • Setting up a channel layer with Redis
          channels-redis
          CHANNEL_LAYERS for config
    
    • Enabling a channel layer (Should be modified)
        Every user have unique channel then they can join channel groups
        
    • DateTime added to the msg
    
    • Save message into database
        Created Message Model and fetch and new message functions added  
        fetch function - # Load previous messages from database (On Open condition)
        new message function - # Creates new message (On Click new message submit button)
        get_last_20_messages function from models.py
    
    • Load/Output data from database
        On Open condition data loaded from database and prnt in room.html using JS script
        
    • Room name added
        room_name coulm added into Message Module to connect messages with room
    
    
  ### 📸 Chat Application
  
  #### Registration Page
  
  <img src="media/photos/Registration.jpg" alt="" >
  
  #### Dashboard
  
  <img src="media/photos/Dashboard.jpg" alt="" >
  
  #### Search
  
  <img src="media/photos/Search.jpg" alt="" >
  
  #### Room "lobby"
  
  <img src="media/photos/Lobby.jpg" alt="" >
    
