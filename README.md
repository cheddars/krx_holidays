
python : 3.6+

KRX Holiday util

- KRX 사이트에서 xls 파일 다운로드후 data 디렉토리에 넣고 gen_code.py 실행해서 data.py 파일 생성
- 대한민국 공휴일 데이터는 2018년 데이터부터 있음 주의

## Installation

```bash
pip install krx-holidays==0.0.3
```

## Usage

```python
from datetime import datetime
from krxholidays import is_holiday_str, get_day_info, is_holiday

print(is_holiday(datetime(2021, 1, 1))) # True

dinfo = get_day_info(datetime(2021, 1, 4))
print(dinfo["desc"])        # "평일"
print(dinfo["week_name"])   # "월요일"
print(dinfo["is_holiday"])  # False
```

## Version History

### 0.0.3 (2024-07-06)
- 2024-07-06 일 기준 공휴일 업데이트
- 2028년 데이터 추가