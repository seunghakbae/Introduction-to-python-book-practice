# 패키지

# 모듈을 패키지라는 파일 계층구조에 구성할 수 있다. 

from sources import daily, weekly

print('Daily forecast:', daily.forecast())
print("Weekly forecast:")


# for문에서 enumerate() 함수는 리스트와 리스트 항목의 시작 인덱스를 취한다. 각 리스트의 항목의 
# 인덱스는 1씩 증가한다. 
for number, outlook in enumerate(weekly.forecast(),3): # 옆의 숫자는 몇번째 인덱스 부터 시작하는 지 알려준다. 
	print(number, outlook)