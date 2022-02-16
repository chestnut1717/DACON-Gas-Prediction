# Comp-Covid-visualization


## Description
- DACON 가스공급량 수요예측 모델개발 대회 참가
- 회귀분석과 LSTM을 통한 향후 3개월간 시간대별로 가스공급량 예측

## Environment
- Python == 3.8
- XGBoost == 1.5

## Files
- EDA.ipynb : 데이터 전처리 과정 및 인사이트 도출
- LSTM : LSTM 예측 모델 
- LinearRegression.ipynb : 국내 도시가스 개발 시간대별 수요예측 논문 참고 선형회귀 모델
- TimeSeriesAnalysis.ipynb : 시계열 분석(ARIMA, 지수평활법)
- Weather_Crawling.ipynb : 1시간 단위 온도를 설명변수로 놓고자 크롤링
- XGBoost.ipynb : 시간 관련 변수와 공급량의 시간대별 평균, 표준편차 등을 설명변수로 한 XGBoost 예측 모델
- Ainergy_발표자료.pdf : 발표자료

## Explanation
- 시간대별로 수요 예측량을 LSTM 모델 하는것은 실패(bias가 누적되어서 시간대가 갈수록 오차가 커짐)
- XGBoost가 가장 성능이 좋았음(public score기준 MAPE = 11.77) 

## Feedback / Complement
1. LSTM에 합성곱 신경망을 추가해 입력한 시계열 데이터 평활화 시도
2. 벡터 자동 회귀 분석 시도

