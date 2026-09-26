# from fastapi import FastAPI
# import requests 
# from bs4 import BeautifulSoup


# app = FastAPI()

# @app.get("/home")
# def get_news(page : int = 1 , limit : int = 5):

#     url = "https://news.ycombinator.com"

#     response = requests.get(url)

#     soup = BeautifulSoup(response.text , "html.parser")

#     title = []

#     start = (page - 1) * limit
#     end = start + limit 


#     for item in soup.find_all("span" , class_="sitebit comhead"):

#         title.append(item.text.strip())

#     return {
#         "page" : page,
#         "limit" : limit,
#         "total" : len(title),
#         "data" : title[start:end]

            
#      }
    



# from fastapi import FastAPI
# import requests
# from bs4 import BeautifulSoup


# app = FastAPI()


# @app.get("/news")
# def get_news(page : int = 1 , limit : int = 5):
#     url = "https://news.ycombinator.com"

#     response = requests.get(url)
#     soup = BeautifulSoup(response.text , "html.parser")

#     title= []

#     for item in soup.find_all("span" , class_="sitebit comhead"):
#         title.append(item.text.strip())

#     start = (page - 1)* limit 

#     end = start + limit 

#     return {
#         "page" : page ,
#         "limit" : limit,
#         "total" : len(title),
#         "data" : title[start:end]
#      }

     




#cacheing data




# from fastapi import FastAPI
# import requests

# from bs4 import BeautifulSoup 
# import time 

# app = FastAPI()

# cache_data = []
# last_fetch = 0
# @app.get("/news")

# def get_news():
#     global  cache_data , last_fetch 

#     start = time.time()

#     if time.time() - last_fetch > 60 :
#         print("fetching fresh data")

#         url = "https://news.ycombinator.com"
#         response = requests.get(url)

#         soup = BeautifulSoup(response.text , "html.parser")

#         cache_data = [
#             item.text for item in soup.find_all("span" , class_="sitebit comhead")
#         ]

#         last_fetch = time.time()

#     else:
#         print("using catche data")


#     end = time.time()

#     time_taken = round(end-start, 4)

#     print("time taken : " , time_taken)

#     return {
#         "time_taken" : time_taken,
#         "data" : cache_data[:5]
#     }
