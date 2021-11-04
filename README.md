# filler-visualizer

![demo](https://github.com/tacomea/filler-visualizer/blob/master/gif/filler-visualizer.gif)

42 filler のログをビジュアライズしてスポーツさながら楽しむことができます！

## Usage
（標準入力で`visualize.py`に渡せばALL OK）
### 1. 既にあるログをビジュアライズする
```
$ ./filler_vm -t 3 -p1 john_filler -p2 john_filler -f resources/maps/map00 > log.txt
$ python visualize.py -n 0.1 < log.txt
```

### 2. 新しいバトルをビジュアライズする
```
$ ./filler_vm -t 3 -p1 john_filler -p2 john_filler -f resources/maps/map00 2> /dev/null | python visualize.py -n 0.1
```

## Option
1. `-n [float]`でボードを切り替えるのにかける時間を設定可能（デフォルト0.1秒）
2. `-s True`でボードの最初の状態でストップ可能（デフォルトは`False`になっており、止まらない）

## Others
1. `Ctrl + \`でゲームの一時ストップが可能。もう一度押して、再開
2. rkannoの実況（ボイチャで探してお願いすればしてくれるかも！）

Thanks for ideas rkanno & habe
