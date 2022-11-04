# PY_OPENCV

## 설치
- 우분투
```bash
$ sudo apt-get update
```

- pip3이 설치되어 있지 않으면 아래 명령으로 설치
```bash
$ sudo apt install python3-pip
```
- matplotlib에 대비하여 tk 모듈 설치
```bash
$ sudo apt-get install python3-tk
```

- 전역에서 사용되는 pip를 미리 업그레이드(우분투, 터미널에 입력)
```bash
$ sudo -H pip3 install --upgrade --ignore-installed pip setuptools
```
#### pip 업그레이드
```bash
$ sudo pip3 install --upgrade pip
```

#### 가상환경 생성
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

#### pip 업그레이드
```bash
(가상환경이름)$ pip install --upgrade pip
```
#### 버전 및 설치 확인(pip의 경로가 가상환경 경로와 일치해야함)
```bash
(가상환경이름) $ pip -V
(가상환경이름) $ pip install –upgrade pip
```

#### 가상환경 비활성화
```bash
(가상환경이름)$ Deactivate
```

## 파이썬 버전 3.10으로 설치
- apt 업데이트 및 업그레이드
```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt dist-upgrade
```
- 새 저장소 추가
```bash
$ sudo apt install software-properties-common -y
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

$ sudo add-apt-repository ppa:deadsnakes/ppa
```

- 파이썬 3.10 설치
```bash
$ sudo apt install python3.10
$ sudo apt-get install python3.10-venv
//$ sudo apt install python3-pip

$ sudo apt-get install python3.10-tk
```
- 설치 확인
```bash
$ python3.10 -V
$ pip3 -V
//$ pip3.10 -V
```

- 가상환경 생성
```bash
$ python3.10 -m venv venv
```

- 메모장으로 .bashrc 파일을 열어 가장 아래에 내용 추가
```bash
$ sudo gedit ~/.bashrc
// 추가할 내용 (저장)
alias python3=’python3.10’
```

- 커널에 적용
```bash
$ source ~/.bashrc
// 확인
$ python3 -V
```
- 확인
```bash

```

#### opencv 및 관련 패키지 설치

- 이하 가상환경 안에서 opencv 설치 (파이썬 3.10 이상)
```bash
$ pip install opencv-contrib-python
```
- 파이썬 3.6 이하
```bash
$ pip install opencv-contrib-python==3.4.1.15
```
- matplotlib 설치
```bash
$ pip install matplotlib
//matplotlib이 동작안할때 (에러메시지에 xcb 어쩌구..)
(가상환경) $ pip install opencv-python-headless
```

- pafy, youtube-dl 설치
```bash
$ pip install pafy youtube-dl
```