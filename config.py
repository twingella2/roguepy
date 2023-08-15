import json

with open('config.json') as f:
    config = json.load(f)

screen_width = config['screen_width']
# 他の設定も同様に読み込む
