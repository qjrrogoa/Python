#GET방식으로 요청 보내기
#방법1:requests.get(요청url)
#방법2:requests.request('GET',요청url)
import requests

url='https://abluestore.com/web/product/big/202012/ab0919b9a7600fb3aacd70305de2ecb9.jpg'
#res=requests.get(url) # 파일크기 0
#방법1
#res = requests.get(url,headers={'User-agent':'Mozilla/5.0'})
#방법2
res = requests.request('GET',url,headers={'User-agent':'Mozilla/5.0'})
content = res.content

print('[요청 방식]',res.request.method,sep='\n')
print('[요청 헤더]',res.request.headers['User-agent'],sep='\n')
#위 바이너리데이타를 이미지로 저장: 이미지 스크래핑
with open('scrapping.png','wb') as f:
    f.write(content)
