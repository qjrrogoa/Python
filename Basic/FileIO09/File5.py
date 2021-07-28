#바이너리모드로 읽고 쓰기
import pickle
print(dir(pickle))
print('[바이너리 모드로 쓰기]')
name='가길동';age=20;isMember=True
jumsu = {'국어':100,'영어':99,'수학':100}

with open('pickle.wb','wb') as f:
    pickle.dump(name,f)
    pickle.dump(age, f)
    pickle.dump(isMember, f)
    pickle.dump(jumsu, f)
print('[바이너리 모드로 읽기]')
with open('pickle.wb','rb') as f:
    name=pickle.load(f)
    age=pickle.load(f)
    isMember=pickle.load(f)
    jumsu=pickle.load(f)
    print(name,age,isMember,jumsu,sep=' | ')