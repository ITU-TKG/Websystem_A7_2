import random
from pprint import pprint
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# 仮データ作成
weather_data = [0, 1, 2]
route_data = ["a", "b", "c", "d"]  # ラベル

data = []

maxlength = 10000
for i in range(maxlength):
    weather = random.choice(weather_data)
    time = random.randint(0, 7200)
    route = random.choice(route_data)
    road = random.randint(0, 100)
    package = random.randint(0, 100)
    data.append({"features": [weather, time, road, package], "labels": route})

# 特徴量とラベルを分離
features = [item["features"] for item in data]
labels = [item["labels"] for item in data]

# データをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

# ランダムフォレストモデルのトレーニング
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# テストデータを使った予測
y_pred = model.predict(X_test)

# モデルの評価
print(classification_report(y_test, y_pred, target_names=route_data))

# モデルの保存
joblib.dump(model, "../結果データ/route_model.pkl")