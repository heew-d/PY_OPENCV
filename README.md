# PY_OPENCV

## 설치
#### 전역에서 사용되는 pip를 미리 업그레이드
- 우분투, 터미널에 입력
```bash
$ sudo -H pip3 install --upgrade --ignore-installed pip setuptools
```
- pip3이 설치되어 있지 않으면 아래 명령으로 설치
```bash
$ sudo apt install python3-pip
```

#### 가상환경 생성
```bash
$ python -m venv venv
```

#### 우분투에서 파이썬3을 사용할때
```bash
$ python3 -m venv venv
```

#### 우분투에선 가상환경명령(venv) 설치
```bash
$ sudo apt-get install python3-venv
```

#### 가상환경 활성화
- 우분투,맥
```bash
$ source ./venv/bin/activate
```

#### 가상환경 비활성화
```bash
(가상환경이름)$ Deactivate
```

#### opencv 설치하기
-  우분투에서 설치하기 (파이썬 3.6버전)
```bash
$ pip install opencv-contrib-python==3.4.1.15
```
- matplotlib 설치
```bash
$ pip install matplotlib
```