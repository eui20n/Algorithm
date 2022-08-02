# 에라토스테네스의 체
소수를 판별하는 알고리즘 이다.   
특히 넓은 범위의 소수를 판별할 때 아주 유용하다.   
시간복잡도 O(n ** (1/2))
   
# 방식
1. 2부터 시작해서 2를 제외한 2의 배수인 것을 다 지워준다.   
2. 2를 했으면 3으로 한다.   
3. 3을 했으면 4로 한다.   
3-1. 이 때, 4는 2에서 제거가 되기 때문에 할 수 없다.   
4. 이와 같은 방식으로 위 과정을 반복을 한다.   
5. 그럼 소수만 남게 된다.   
   
# 그림으로 이해하기
(2 ~ 99 까지의 소수를 구하는 것으로 예시를 듬)   
먼저 아래와 같이 만들어 준다.   
<img src = "https://user-images.githubusercontent.com/74887218/182334001-3058b082-fbdd-42a8-85f5-d6b67132ebac.png" width="30%">   
<br>
1. 2부터 시작해서 2를 제외한 2의 배수인 것을 다 지워준다. => 지우는거 대신 색을 칠함   
<img src = "https://user-images.githubusercontent.com/74887218/182334744-73d6e228-14bf-4550-b7e5-fc4fa68b7fa5.png" width="30%"><br>
2. 2를 했으면 3으로 한다.   
<img src = "https://user-images.githubusercontent.com/74887218/182335271-7dd4705e-798b-443b-a7b3-bb552f07c736.png" width="30%"><br>
3. 3을 했으면 4를 해야하는데, 2에서 색이 칠해졌기 때문에 하지 않는다.
4. 5로 해준다.   
<img src = "https://user-images.githubusercontent.com/74887218/182335567-159aae94-79c9-4121-a9ea-d21d9480e0db.png" width="30%"><br>
5. 이렇게 하면 결국에 이렇게 색이 칠해진다.   
<img src = "https://user-images.githubusercontent.com/74887218/182335810-5bd49df8-a516-4316-9d4e-c2807aa266bf.png" width="30%"><br>
<br>
이렇게 하면 색이 안칠해져 있는 부분이 있는데, 그 부분이 소수이다.   
<br>

> <a href="https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4">위키백과</a>
