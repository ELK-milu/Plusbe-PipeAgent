import requests

url = "http://127.0.0.1:3421/input"

headers = {
    "Authorization": "",
    "Content-Type": "application/json"
}

'''
POST:
```json
{
    streamly:boolean,
    user:string,
    Input:string,
    text: text,
    temperature:number,
    max_length:integer
}
```
'''


class PostChat:
    def __init__(self,streamly,user,text):
        self.payload = {
            "streamly": streamly,
            "user": user,
            "Input": text,
            "text": text,
            "temperature": 1,
            "max_length": 1024,
        }
        self.streamly = streamly
        self.response = requests.request("POST", url, json=self.payload, headers=headers,stream=streamly)
        self.response.encoding = 'utf-8'


    def GetResponse(self):
        return self.response
    def PrintAnswer(self):
        return self.text  # 返回存储的响应内容

if __name__ == "__main__":
    # 启动 main 服务
    ps = PostChat(streamly=True,user="user",
             text="你好啊").GetResponse()
    for chunk in ps.iter_content(chunk_size=None):
        print(str(chunk))