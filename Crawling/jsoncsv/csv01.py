#파이썬 리스트를 csv파일로 저장하기
import csv
records=[
    [1,'가길동','KIM','1234','가산동',25],
    [2,'나길동','LEE','1234','나산동',15],
    [3,'다길동','PARK','1234','다산동',35]]
#newline='' 키워드인수가 빠지면 빈 라인이 추가된다
with open('list.csv','w',encoding='utf8',newline='') as f:#파일 생성됨
    #writer = f.writelines(records)#리스트의 각 요소는 str이어야 한다
    writer = csv.writer(f)#생성된 list.csv파일에 데이타를 쓰기 위한 writer객체 얻기
    print(writer,type(writer),sep=' | ')
    # csv의 헤더는 넣어도 되고 안넣어도 된다
    # writer타입은 writeheader()함수가 없다
    writer.writerow(['번호','이름','아이디','비번','주소','나이'])#csv파일의 타이틀(헤더) 작성
    '''
    for record in records:#한라인씩 작성
        writer.writerow(record)
    '''
    # 한꺼번에 작성
    writer.writerows(records)
#파이썬 딕셔너리를 csv파일로 저장하기
records=[
    {'번호':1,'이름':'가길동','아이디':'KIM','비번':'1234','주소':'가산동','나이':25},
    {'번호':2,'이름':'나길동','아이디':'LEE','비번':'1234','주소':'나산동','나이':35},
    {'번호':3,'이름':'다길동','아이디':'PARK','비번':'1234','주소':'다산동','나이':45}]
with open('dict.csv','w',encoding='utf8',newline='') as f:
    # 딕션너리 타입의 객체를 csv파일로 저장시 DictWriter()생성자 사용
    writer=csv.DictWriter(f,fieldnames=['번호','이름','아이디','비번','주소','나이'])
    print(writer, type(writer), sep=' | ')
    writer.writeheader()#csv의 헤더는 넣어도 되고 안넣어도 된다
    '''
    for record in records:#한라인씩 작성
        writer.writerow(record)
    '''
    # 한꺼번에 작성
    writer.writerows(records)
