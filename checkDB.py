from contentAPI import getContent
from django.template.loader import render_to_string
import os
from django.shortcuts import render, redirect
from Home.models import SearchQ



'''
if db.columnNameQuery.anyrow == query:
    return("/"+query)

from django.shortcuts import render
from .models import GeneratedPage

def check_query(request):
    if request.method == 'POST':
        query = request.POST.get('query')

        # Check if the query already exists in the database
        if GeneratedPage.objects.filter(query=query).exists():
            # Query already exists, handle accordingly
            return render(request, 'query_exists.html')

        # Query does not exist, proceed with the rest of the flow
        # ... (Code for API calls, content generation, etc.)

    # Render the form template for GET requests or when the query doesn't exist
    return render(request, 'form_template.html')
'''    
def getPage(request,query):    
    

    # Check if the query already exists in the database
    
    if SearchQ.objects.filter(query=query).exists():
        # Query already exists, handle accordingly
        print("Query exists")
        return "Exists, Done"
        
    else:
        print("Query does not exists")
        titlez,imgURL,content3 = getContent(query)
        contt = str(content3)
        # Step 1: Render the HTML template with the content variable
        print(contt)
        if contt != "No Articles found, try searching with other keywords":
            html_content = render_to_string('search.html', {'Content': contt,
                                                            'csrff': "{% csrf_token %}",
                                                            'Queried' : query,
                                                            'titlez' : titlez,
                                                            'imgUrl': imgURL}

                                            )
                                                            

            # Step 2: Choose a filename based on the query
            filename = f"{query}.html"  # Assuming query is a string without any special characters

            # Step 3: Save the rendered HTML content to the file
            file_path = os.path.join('G:\\Placement\\10 Days\\Django\\myproject1\\templates', filename)
            with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
                file.write(html_content)
            print("Done")
            return "Succesful, Done"
        
        else:
            
            return "No Articles"
        
       

    

    # Step 4: Optionally, create a database entry with the query and file path
    # ... (Code to save the query and file path to the database)
    