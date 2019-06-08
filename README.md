#help_me_carry
## Overview
  help_me_carryにおける,対話者からのメッセージ処理を行う.


## Description
help.pyは対話者からのメッセージを処理行う。  
resume_sphinx.pyは**PocketSphinx**での音声認識のコード。    

## Usage
```
roslaunch help_me_carry help.launch
```
上記のコマンドを実行し,`help_ctrl`にString型のメッセージを投げると起動する。

## Node
**`name` help**

### Subscribe Topic

* **`help_ctrl`** メインノードの立ち上げ（ std_msgs/String ）

* **`recognition_result`** yes/noの音声認識結果の受け取り（ std_msgs/String ）

* **`recognition_txt`** 対話者の回答の受け取り（ std_msgs/String ）

### Publish Topic

* **`txt_start`** 音声認識開始 ( std_msgs/Bool )

* **`yes_no_start`** yes/noの音声認識開始（ std_msgs/Bool ）

* **`help_me_carry/send_place`** 場所情報の送信（ std_msgs/String ）

## Node
**`name` resume_sphinx**

### Subscribe Topic
* **`txt_start`** 音声認識開始（ std_msgs/Bool ）

### Publish Topic
* **`recognition_txt`** 音声認識結果 ( std_msgs/String )
