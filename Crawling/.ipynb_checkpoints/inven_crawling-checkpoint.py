{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7e085998",
   "metadata": {},
   "source": [
    "주의 사항\n",
    "1) selenium driver 업데이트 권장드립니다 -> !pip install selenium --upgrade  \n",
    "2) 크롬창 우측 상단 점 3개 클릭 - 도움말 - chrome 정보에서 chrome 버전 확인하시고 거기에 맞는 웹드라이버 사용 부탁드립니다.  \n",
    "3) 제가 직접 올린 웹드라이버는 1.16버전으로, 최신 1.15 크롬에서 원할하게 돌아감을 확인했습니다.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "85eb0f3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.11.2\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import time\n",
    "\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "import selenium\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "import re\n",
    "print(selenium.__version__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "7195ff8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "service = Service()\n",
    "options = webdriver.ChromeOptions()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "38e25e5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def crawl(url):\n",
    "    driver = webdriver.Chrome(service=service, options=options)\n",
    "    driver.get(url)\n",
    "    driver.maximize_window()\n",
    "    comment_list = []\n",
    "    \n",
    "    soup = BeautifulSoup(driver.page_source,'lxml')\n",
    "    data_box = soup.find_all('a',attrs = {'class':'subject-link'})\n",
    "    \n",
    "    for index, data in enumerate(data_box):\n",
    "        \n",
    "        print(index+1,\"번째 게시글에서 댓글을 추출중입니다...\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "        \n",
    "        link = data.attrs['href']\n",
    "        driver.get(link)\n",
    "        time.sleep(5)\n",
    "        \n",
    "        soup = BeautifulSoup(driver.page_source,'lxml')\n",
    "        comment_box = soup.find_all('span',attrs = {'class':'content cmtContentOne'})\n",
    "        \n",
    "        for index, comment in enumerate(comment_box):\n",
    "            comment_text = comment.get_text(strip=True)\n",
    "            comment_list.append(comment_text)\n",
    "\n",
    "        ## 성능 테스트 위해 리미터 걸었습니다.\n",
    "        if len(comment_list) > 10:\n",
    "            break;\n",
    "    \n",
    "    print(\"댓글 추출이 완료되었습니다!\")\n",
    "    print(\"-------------------------------------------------------\")\n",
    "    driver.close()\n",
    "    return comment_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "19f0069f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def query():\n",
    "\n",
    "    while(True):\n",
    "        print(\"인벤 코드를 이용해서 검색해주세요\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "        print(\"리그 오브 레전드 :              0\")\n",
    "        print(\"메이플스토리     :              1\")\n",
    "        print(\"피파온라인 4     :              2\")\n",
    "        print(\"디아블로 4       :              3\")\n",
    "        print(\"로스트아크       :              4\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "    \n",
    "        try:\n",
    "            game = int(input(\"코드 입력 \"))\n",
    "            if game < 0 or game > 4:\n",
    "                raise ValueError()\n",
    "    \n",
    "        except ValueError:\n",
    "            print(\"잘못된 입력입니다. 코드를 확인해주세요.\")\n",
    "            print(\"-------------------------------------------------------\")\n",
    "        \n",
    "        except Exception as e:\n",
    "            print(\"알 수 없는 예외가 발생했습니다:\", e)\n",
    "            print(\"-------------------------------------------------------\")\n",
    "        else:\n",
    "            break\n",
    "            \n",
    "    print(\"-------------------------------------------------------\")\n",
    "    if game == 0:\n",
    "        print(\"리그 오브 레전드 인벤의 오늘의 화제글을 불러옵니다.\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "        url = \"https://www.inven.co.kr/board/lol/4625?my=chuchu\"\n",
    "        result = crawl(url)\n",
    "        \n",
    "    elif game == 1:\n",
    "        print(\"메이플스토리 인벤의 30추글 목록을 불러옵니다.\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "        url = \"https://www.inven.co.kr/board/maple/5974?my=chuchu\"\n",
    "        result = crawl(url)\n",
    "        \n",
    "    elif game == 2:\n",
    "        print(\"피파온라인 4 인벤의 오늘의 화제글을 불러옵니다.\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "        url = \"https://www.inven.co.kr/board/fifaonline4/3146?my=chu\"\n",
    "        result = crawl(url)\n",
    "        \n",
    "    elif game == 3:\n",
    "        print(\"디아블로 4 인벤의 30추글 목록을 불러옵니다.\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "        url = \"https://www.inven.co.kr/board/diablo4/6025?my=chuchu\"\n",
    "        result = crawl(url)\n",
    "        \n",
    "    elif game == 4:\n",
    "        print(\"로스트아크 인벤의 30추글 목록을 불러옵니다.\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "        url = \"https://www.inven.co.kr/board/lostark/4811?my=chuchu\"\n",
    "        result = crawl(url)\n",
    "        \n",
    "    df_result = pd.DataFrame(result, columns=['comments'])\n",
    "    return df_result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "6eac8c4d",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "인벤 코드를 이용해서 검색해주세요\n",
      "-------------------------------------------------------\n",
      "리그 오브 레전드 :              0\n",
      "메이플스토리     :              1\n",
      "피파온라인 4     :              2\n",
      "디아블로 4       :              3\n",
      "로스트아크       :              4\n",
      "-------------------------------------------------------\n",
      "코드 입력 안녕하세요\n",
      "잘못된 입력입니다. 코드를 확인해주세요.\n",
      "-------------------------------------------------------\n",
      "인벤 코드를 이용해서 검색해주세요\n",
      "-------------------------------------------------------\n",
      "리그 오브 레전드 :              0\n",
      "메이플스토리     :              1\n",
      "피파온라인 4     :              2\n",
      "디아블로 4       :              3\n",
      "로스트아크       :              4\n",
      "-------------------------------------------------------\n",
      "코드 입력 100\n",
      "잘못된 입력입니다. 코드를 확인해주세요.\n",
      "-------------------------------------------------------\n",
      "인벤 코드를 이용해서 검색해주세요\n",
      "-------------------------------------------------------\n",
      "리그 오브 레전드 :              0\n",
      "메이플스토리     :              1\n",
      "피파온라인 4     :              2\n",
      "디아블로 4       :              3\n",
      "로스트아크       :              4\n",
      "-------------------------------------------------------\n",
      "코드 입력 1\n",
      "-------------------------------------------------------\n",
      "메이플스토리 인벤의 30추글 목록을 불러옵니다.\n",
      "-------------------------------------------------------\n",
      "1 번째 게시글에서 댓글을 추출중입니다...\n",
      "-------------------------------------------------------\n",
      "2 번째 게시글에서 댓글을 추출중입니다...\n",
      "-------------------------------------------------------\n",
      "댓글 추출이 완료되었습니다!\n",
      "-------------------------------------------------------\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>comments</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>키보드 마우스 컨트롤이 딸리는가보지</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>동체시력하고 손 컨은 다르지</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>카이스트 자쿰 갓원기님님님</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>정보) 6차 쇼케직후에는 금손은손판매도 쉴드쳤다</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>6개먄 직원이 친거 아님? ㅋㅋㅋ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>근데 드립거르고 비슷한 나이대에 게임 잘만하는 사람 많은데..</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>사스케 애비도 그것 못찾을듯 ㅋㅋ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>안쓰면 또 존나 손해보는거같아서 무조건 어딘가 돌리는데 개망함</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>난 그래서 레전하프 사서 쌍메도박함</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>성공한 적 없지만..</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>저거때문에 억지로 있지도 않은 부캐템 만드는중</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>안쓰면 또 존나 손해보는거같아서 무조건 어딘가 돌리는데 개망함</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>난 꾸역꾸역 에픽이라도 찾아서 돌림 결과는 잡옵</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>ㅋㅋㅋㅋㅋ이거진짜 안돌리면 너무 손해같아</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>난 그래서 레전하프 사서 쌍메도박함</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>성공한 적 없지만..</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>안돌리면 개손해같아서 메소 메포 바꾸고 3세트 정도랑 저거랑24퍼 골클벨에 박았는데...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>원기가 레큐를 뿌리고 그걸 유저가 사용하고 스펙 하락해서 복구하는데 쓰이는 큐브 비...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>ㅋㅋ나도 레전하프나 그리드펜던트 돌림</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>에픽에 돌리고 스펙하락함... 럭키 장큐임</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>그래서 골드애플에서 나오는 잡유닠 얼장에 버려버림세줄이나 레전뜨면 ㄱㅇㄷ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>이벤트로 조금씩 뿌리는게 ㄹㅇ 악질임</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>걍 유닠 얼장 사놓고 교불장큐,레큐 주는거 돌리는중</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>블라인드 된 코멘트입니다.[내용보기]레전천장도 500개나 필요해서 ㄹㅇ 쓸모없음</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>앗 비추 실수 ㅈㅅㅈㅅ;; 새류고침 누른 줄 알았음</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>난 다들 비공 누르길래 같이 눌렀어</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>노딱 너가 죽였어</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>파딱도 나빠</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>결국 블라먹음 ㅋㅋㅋㅋㅋ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>블라 댓글 차단 완료</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>주보돌이한테나 주는거지 ㄹㅇㅋㅋ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>리부트를 하시면 천장으로 확정등업 시키고 쓰시면 됩니다</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>블큐는 장식이 아니엥ㅅ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>레큐 쓸모없으면 카유잠 쓰고 유니크 15퍼 만들때 ㄱㄱ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>내 위로 저능아들 몇 보이네</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>오늘 명성치 50만 쌓였길래 첫째 보공 둘째 상추 잠구고에픽 벞지갈고 유니크 뽑을려...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             comments\n",
       "0                                 키보드 마우스 컨트롤이 딸리는가보지\n",
       "1                                     동체시력하고 손 컨은 다르지\n",
       "2                                      카이스트 자쿰 갓원기님님님\n",
       "3                          정보) 6차 쇼케직후에는 금손은손판매도 쉴드쳤다\n",
       "4                                  6개먄 직원이 친거 아님? ㅋㅋㅋ\n",
       "5                  근데 드립거르고 비슷한 나이대에 게임 잘만하는 사람 많은데..\n",
       "6                                  사스케 애비도 그것 못찾을듯 ㅋㅋ\n",
       "7                  안쓰면 또 존나 손해보는거같아서 무조건 어딘가 돌리는데 개망함\n",
       "8                                 난 그래서 레전하프 사서 쌍메도박함\n",
       "9                                         성공한 적 없지만..\n",
       "10                          저거때문에 억지로 있지도 않은 부캐템 만드는중\n",
       "11                 안쓰면 또 존나 손해보는거같아서 무조건 어딘가 돌리는데 개망함\n",
       "12                         난 꾸역꾸역 에픽이라도 찾아서 돌림 결과는 잡옵\n",
       "13                             ㅋㅋㅋㅋㅋ이거진짜 안돌리면 너무 손해같아\n",
       "14                                난 그래서 레전하프 사서 쌍메도박함\n",
       "15                                        성공한 적 없지만..\n",
       "16  안돌리면 개손해같아서 메소 메포 바꾸고 3세트 정도랑 저거랑24퍼 골클벨에 박았는데...\n",
       "17  원기가 레큐를 뿌리고 그걸 유저가 사용하고 스펙 하락해서 복구하는데 쓰이는 큐브 비...\n",
       "18                               ㅋㅋ나도 레전하프나 그리드펜던트 돌림\n",
       "19                            에픽에 돌리고 스펙하락함... 럭키 장큐임\n",
       "20           그래서 골드애플에서 나오는 잡유닠 얼장에 버려버림세줄이나 레전뜨면 ㄱㅇㄷ\n",
       "21                               이벤트로 조금씩 뿌리는게 ㄹㅇ 악질임\n",
       "22                       걍 유닠 얼장 사놓고 교불장큐,레큐 주는거 돌리는중\n",
       "23       블라인드 된 코멘트입니다.[내용보기]레전천장도 500개나 필요해서 ㄹㅇ 쓸모없음\n",
       "24                       앗 비추 실수 ㅈㅅㅈㅅ;; 새류고침 누른 줄 알았음\n",
       "25                                난 다들 비공 누르길래 같이 눌렀어\n",
       "26                                          노딱 너가 죽였어\n",
       "27                                             파딱도 나빠\n",
       "28                                      결국 블라먹음 ㅋㅋㅋㅋㅋ\n",
       "29                                                   \n",
       "30                                        블라 댓글 차단 완료\n",
       "31                                  주보돌이한테나 주는거지 ㄹㅇㅋㅋ\n",
       "32                     리부트를 하시면 천장으로 확정등업 시키고 쓰시면 됩니다\n",
       "33                                       블큐는 장식이 아니엥ㅅ\n",
       "34                     레큐 쓸모없으면 카유잠 쓰고 유니크 15퍼 만들때 ㄱㄱ\n",
       "35                                    내 위로 저능아들 몇 보이네\n",
       "36  오늘 명성치 50만 쌓였길래 첫째 보공 둘째 상추 잠구고에픽 벞지갈고 유니크 뽑을려..."
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "query()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
