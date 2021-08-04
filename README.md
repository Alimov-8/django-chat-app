# django-chat-app

  ### Creating Chat Application:
    📌 Add Channels to your project
    📌 Build a WebSocket consumer and appropriate routing
    📌 Implement a WebSocket client
    📌 Enable a channel layer with Redis
    📌 Make your consumer fully asynchronous

  ### Resources: 
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
    
    
  ##### ❗️ TODO:
    📌 Database to save messages
    📌 Style for chat application
