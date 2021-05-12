#!/bin/bash
clear

today=$(date "+%Y年%m月%d日")

string_today="今日は $today です。"

display () {
    string_today=$1
    for ((i = 0; i < ${#string_today}; i++))
    do
        now=$(date "+%p%I時%M分%S秒")
        string_now="今は $now です。"
        clear
        display_string_today=${string_today:$i:${#string_today}-$i}${string_today:0:$i}
        display_string_now=${string_now:$i:${#string_now}-$i}${string_now:0:$i}
        echo $display_string_today
        echo $display_string_now
        sleep 0.1
    done
}

while :
do
    display "$string_today"
done
