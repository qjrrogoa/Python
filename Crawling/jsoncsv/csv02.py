#csv파일 읽어오기
import csv
with open('dict.csv','r',encoding='utf8') as f:
    #f.read()로 읽으면 str
    reader=csv.reader(f)
    print(reader,type(reader),sep=' | ')
    print(dir(reader))#__iter__
    for record in reader:
        #print(record)#요소 하나가 [] 즉 csv의 한 라인이 하나의 리스트다
        for element in record:
            print("{}".format(element),end=' ')

        print()#줄바꿈