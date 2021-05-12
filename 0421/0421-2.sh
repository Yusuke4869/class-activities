#!/bin/bash
echo -e ".cファイルコンパイル\n"

echo -n "ファイル名を入力してください: "
read file_name

if [ -e $file_name.c ]; then
    echo -e "\n$file_name.c をコンパイルします"
    gcc -fexec-charset=CP932 -o $file_name $file_name.c

    if [ $? = 0 ]; then
        echo -e "\nコンパイル完了"
    else
        echo -e "\nエラー\nコンパイルに失敗しました"
    fi

else
    echo -e "\n$file_name.c が存在しません\n$file_name.c が存在することを確認し、同一デ
ィレクトリで再度実行してください"
fi

echo -e "\n10秒後に終了します\n「Ctrl+C」で強制終了できます"

sleep 10