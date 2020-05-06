import time

from rest_framework.throttling import BaseThrottle,SimpleRateThrottle


VISTI_RECORD = {}
# class VisitThrottle(BaseThrottle):
#
#     def __init__(self):
#         self.history = None
#
#     def allow_request(self, request, view):
#         # 1.获取ip地址
#         # remote_addr = request.META.get('REMOTE_ADDR')
#         remote_addr = self.get_ident(request)
#         print(remote_addr)
#         ctime = time.time()
#
#
#         if remote_addr not in VISTI_RECORD:
#             VISTI_RECORD[remote_addr] = [ctime]
#             return True
#
#         history = VISTI_RECORD.get(remote_addr)
#         self.history = history
#
#
#         while history and history[-1] < ctime-60:
#             history.pop()
#
#         if len(history) < 3:
#             history.insert(0,ctime)
#             return True
#
#
#         # return True  # 可以继续访问
#         # return False # 访问频率太高 被限制
#
#     def wait(self):
#         ctime = time.time()
#         return 60 - (ctime-self.history[-1])




class VisitThrottle(SimpleRateThrottle):
    scope = 'james'
        
    def get_cache_key(self,request,view):
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
    scope = 'leborn'

    def get_cache_key(self, request, view):
        return request.user.username