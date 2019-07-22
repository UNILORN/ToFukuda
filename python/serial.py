############################## 
#
# シリアル通信
# データ受信 -> データ送信 -> （以下ループ) 
#
##############################


import serial

if __name__ == '__main__':

    # シリアルポートのPath
    path = '/dev/tty.******'
    ser = serial.Serial(path)

    while True: # 常に動作させる

        #
        # 受信時
        #
        line = ser.readline()   # データの受信待ちを行う データが来るまではここで待機される
        text = line.decode('utf-8') # データ取得後テキストエンコードを行う

        print(text)     # 受信データの表示

        if text == "起動":    # データに"起動"という文字列があれば実行
            print("起動プログラム")
        elif text == "終了":
            print("終了プログラム")
        else:
            print("意図されないデータの受信")

        #
        # 送信時
        #
        data = "送信用ダミーデータ"             # 送信するテキストデータ
        ser.write(bytes(data, 'UTF-8'))      # データを送信する
