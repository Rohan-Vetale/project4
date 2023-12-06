#GET https://newsapi.org/v2/everything?q=bitcoin&apiKey=4fccf9a9200744178deeb56b77c2cc2f
from newsapi import NewsApiClient
from openai import OpenAI
client = OpenAI(api_key="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")
# Init
newsapi = NewsApiClient(api_key='4fccf9a9200744178deeb56b77c2cc2f')

# /v2/top-headlines


# /v2/everything
'''all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)'''

# /v2/top-headlines/sources
#sources = newsapi.get_sources()
def getContent(query):
    

    try:
      print("Getting Headlines")
      top_headlines = newsapi.get_top_headlines(q=query)
      imgUrl2 = top_headlines['articles'][0]['urlToImage']
      titlezz = top_headlines['articles'][0]['title']
      titlez = str(titlezz)
      descriptions = [article['description'] for article in top_headlines['articles']][:8]
      descriptions[2]
      for i, description in enumerate(descriptions, start=1):
          #list of all articles
          global NewsCont1
          NewsCont1 = ""
          NewsCont1 += (f"Article {i}: {description}")
      
      response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "You have to only generate and reply a news blog of 2 page content body. The title, related articles, some content is provided by the user from trusted sources"},
          {"role": "user", "content": "Here it is "+str(NewsCont1)}
        ]
      )
      bablu = response2.choices[0].message.content
      return titlez,imgUrl2,bablu
        
    except:
        try:

          print("No Headlines found, using everything now")
          top_headlines = newsapi.get_everything(q=query)
          imgUrl2 = top_headlines['articles'][0]['urlToImage']
          titlezz = top_headlines['articles'][0]['title']
          titlez = str(titlezz)
          descriptions = [article['description'] for article in top_headlines['articles']][:3]
          descriptions[2]
          for i, description in enumerate(descriptions, start=1):
              #list of all articles
              global NewsCont
              NewsCont = ""
              NewsCont += (f"Article {i}: {description}")
          response2 = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": "The title, related articles, some content is provided by the user from trusted sources. You have to only generate and reply a news blog of 1 page content body only.Your reply will be pasted directly inside the body of article."},
            {"role": "user", "content": "Here it is "+str(NewsCont)}
          ]
          )
          bablu = response2.choices[0].message.content
          return titlez,imgUrl2,bablu

        except:
            a = "No Articles found, try searching with other keywords"
            b = "No Articles found, try searching with other keywords"
            c = "No Articles found, try searching with other keywords"
            return a,b,c


'''ActualCont = getContent(query="Cricket")
print(ActualCont)'''




#print("hello "+str({Articles}))
#print('You can also search for other articles!')


