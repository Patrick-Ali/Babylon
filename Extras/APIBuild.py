"""
Get
Post
Put
Patch
Head
Options
Delete
"""

import requests

class API_Call_Builder():

    def get(self, url, query, head, js, encoding=None, auth=None, ver=None, retry=None, timeout=None, ret_data=None):
        response = requests.get(url)
        if len(query) > 0  and len(head) > 0:
              response = requests.get(url,
                                params = query,
                                headers = head)
        if len(query) == 0  and len(head) > 0:
              response = requests.get(url,
                                headers = head)
        if len(query) > 0  and len(head) == 0:
              response = requests.get(url,
                                params = query)
      
        if encoding is not None:
            response.encoding = encoding
        if response.status_code == 200:
            if js == True:
                return response.json()
            else:
                return response.text
        else:
            if js == True:
                print(response.status_code)
                print(response.text)
                return {"status": "unsuccessful"}
            else:
                return "unsuccessful"
            
    def post(self, url, data, auth=None, ver=None, retry=None, timeout=None):
        response = requests.post(url, data=data)
        return response
        
    def put(self, url, data, auth=None, ver=None, retry=None, timeout=None):
        response = requests.put(url, data=data)
        
    def del_http(self, url, auth=None, ver=None, retry=None, timeout=None):
        response = requests.delete(url)
        
    def head(self, url, auth=None, ver=None, retry=None, timeout=None):
        response = requests.head(url)
        
    def patch(self, url, data, auth=None, ver=None, retry=None, timeout=None):
        response = requests.patch(url, data=data)
        
    def options(self, url, auth=None, ver=None, retry=None, timeout=None):
        response = requests.options(url)
    
    def get_head(self, response):
        #response = requests.get(url)
        return response.headers
    
    def get_head_specific(self, url, value):
        header = self.get_head(url)
        return header[value]

if __name__ == "__main__":
    hold = API_Call_Builder()
    #print(hold.get("https://httpbin.org/get", {}, {}, True))
    #print(hold.post("https://httpbin.org/post", {"key":"value"}).json())
    print(hold.get("https://api.github.com/repos/Patrick-Ali/Babylon/contents",{},{"Authorization": "token b2d2d0744ed81e3d7ec3ddf5075dfa4978a41990"}, True))
    ##Make a paste
    #4ca487b2ef36f16057c593ebf7ea68dd
    #print(hold.post("https://pastebin.com/api/api_post.php",) 
    ##Get a paste
    ##Authenticate a user
    #print(hold.get("https://httpbin.org/basic-auth/test/test", {}, {}, True))
    #https://httpbin.org/basic-auth/test/test
    #"body": "response = requests.get(<url>, params = query, headers = head)",
    #"b1": "response = requests.put(<url>, data = data)",
    #"b2": "response = requests.put(<url>, params = query, data = data)",
    #"b3": "response = requests.put(<url>, headers = head, data = data)",
    #"b4": "response = requests.put(<url>, params = query, headers = head, data = data)",
    #https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY    
