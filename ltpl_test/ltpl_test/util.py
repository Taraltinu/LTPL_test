from rest_framework.response import Response

class APIResponse(Response):
    
    def __init__(self, data="", code=1, message=""):
        print('IIIIIIIII')
        super().__init__({'code':code, 'data':data,'message':message})