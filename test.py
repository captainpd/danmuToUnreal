#json转化为str
#描述：dumps()将 Python 对象编码成 JSON 字符串

import json
hi = '你好'
j = {"accessToken": hi, "User-Agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_131)"}
str = json.dumps(j)
print(str)
print(str.encode())

j2 = json.loads(str)
print(j2['accessToken'])

