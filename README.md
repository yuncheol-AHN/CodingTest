# 📘 Python

### 입력
- input() : 문자열이다, 입력할 때 마다 버퍼에 문자 입력
- sys.stdin.readline() : 문자열이다, 입력이 완료되면 한번에 버퍼에 입력

<br/>

### 문자열

- 문자열 → 리스트 :

→ list(string) → 모든 문자로 쪼개기

→ list.split(’’) → 쪼개는 데 기준이 될 문자 입력

- 문자열 뒤집기 string = string[::-1]

<br/>

### 리스트

- 리스트 → 문자열 : ‘’.join(list), ‘ ‘.join(list)
- 마지막 요소 접근 : [-1]
- 제거 : pop(Index), remove(value, 맨 앞 요소만 제거), clear(모두 제거)
- 리스트의 특정 값을 모두 제거하고 싶을 때

```python
arr = [10, 20, 20, 30, 30, 30, 30, 50]
arr[:] = (value for value in arr if value != 30)

print(arr) # [10, 20, 20, 50]
```

<br/>

### 집합

- set(string), set(list) → 중복 제거
- different : 차집합, intersection : 교집합, union : 합집합

<br/>

### 조건문

- Switch 사용 불가
- if ~ elif ~ elif ~ else

<br/>

### 반복문

- for
- while

### 📌 Tip

- global : 지역변수를 전역변수로 사용, nonlocal : 지역변수를 비지역변수(모함수의 변수)로 사용
