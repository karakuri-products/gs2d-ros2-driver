# gs2d-ros2-driver

ROS2 driver for gs2d (汎用シリアルバス RC サーボドライバ・ライブラリ)

----

<img src="https://user-images.githubusercontent.com/15685007/91433150-c886ac00-e89d-11ea-9695-45ce390ce97e.png" width="200">

ROS2で [gs2d](https://github.com/karakuri-products/gs2d) のシリアルサーボドライバを利用できるようにするためのパッケージです。 

ROS 2 Foxy Fitzroy でのみ動作確認済みです。

### ビルド

```
$ cd ~/foxy_ws/src
$ git clone git@github.com:karakuri-products/gs2d-ros2-driver.git
$ cd ..
$ colcon build
```

### 実行サンプル

gs2dノードを起動

```
ros2 run gs2d_ros2_driver gs2d
```

サーボID: 1のトルクをON

```
ros2 topic pub -1 /gs2d_ros2_driver/torque_enable gs2d_ros2_driver_msg/TorqueEnable '{servo_id: 1, data: true}'
```

サーボID: 1のポジションを110度に設定

```
ros2 topic pub -1 /gs2d_ros2_driver/target_position gs2d_ros2_driver_msg/TargetPosition '{servo_id: 1, data: 110}'
```


### メッセージ

#### TorqueEnable
- servo_id (int): サーボID
- data (bool): True (トルクON), False (トルクOFF)

#### TargetPosition
- servo_id (int): サーボID
- data (float): -180〜+180度

その他メッセージやsubscriber/publisherは後日対応予定！