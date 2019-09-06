# 모듈 검색 경로
# 파이썬은 임포트할 파일을 어디에서 찾을까? 디렉터리 이름의 리스트와 표준 sys모듈에 저장되어 있는
# ZIP 아카이브 파일을 변수 PATH로 사용한다. 이 리스트를 접근하여 수정 할 수 있다. 

import sys

for place in sys.path:
	print(place)