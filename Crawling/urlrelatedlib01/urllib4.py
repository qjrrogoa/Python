#GET방식(쿼리스트링으로 으로 파라미터 전달)
#urlopen(요청URL) 즉 파라미터를 쿼리스트링으로 url에 문자열로 연결
import urllib.request as request
import urllib.parse as parse
#딕션너리를 쿼리스트링 형태로 인코딩
query = parse.urlencode({'q':'python','oq':'python'})#->q=python&oq=python
headers={'User-agent':'Mozilla/5.0'}
url="https://www.google.com/search?{}".format(query)
req=request.Request(url,headers=headers)
res=request.urlopen(req)
htmlSource = res.read().decode('utf-8')
print(htmlSource)