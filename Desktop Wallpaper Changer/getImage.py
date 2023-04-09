import requests
import json 


def imageDownloader (queries,api_key) :

    api_url = f"https://api.unsplash.com/search/photos/?page=1&query={queries}&client_id={api_key}"

    response = requests.get(api_url,stream=True)
    
    if response.status_code == 200:
            
            json_content = json.loads(response.content)
            
            result = json_content['results']

            data = result[0]

            data = (data['urls']['full'])

            print (data)


            with open ("wallpaper.jpg","wb") as file :
                  
                  r = requests.get(data,stream=True)

                  file.write(r.content)




# imageDownloader(query,UNSPLASH_ACCESS_KEY)
