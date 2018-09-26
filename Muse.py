from parse import chart_parse,video_parse
from video_downloader import video
from time import sleep
from sys import exit
import os

def art():
    art = """
    ▄▄▄▄███▄▄▄▄   ███    █▄     ▄████████    ▄████████ 
 ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███   ███    ███ 
 ███   ███   ███ ███    ███   ███    █▀    ███    █▀  
 ███   ███   ███ ███    ███   ███         ▄███▄▄▄     
 ███   ███   ███ ███    ███ ▀███████████ ▀▀███▀▀▀     
 ███   ███   ███ ███    ███          ███   ███    █▄  
 ███   ███   ███ ███    ███    ▄█    ███   ███    ███ 
  ▀█   ███   █▀  ████████▀   ▄████████▀    ██████████ 
                                                      """
    print(art)

def chart_50():
    chart_list = chart_parse()

    os.system('cls')
    print("실시간 TOP50\n")
    ct = 1
    for key in chart_list:
        print(str(ct)+". ",key," - ", chart_list[key])
        ct+=1

    print("\n아무키나 누르면 메인화면으로 돌아갑니다.")
    input()

def yt_search(search):
    yt_list = video_parse(search)

    os.system('cls')
    print("검색어 리스트\n")
    ct = 1
    for key in yt_list:
        print(str(ct)+". ",key,"\n")
        ct+=1

    return yt_list

def yt_down(idx,yt_list):
    ct = 1
    for key in yt_list:
        if ct == idx:
            yt_url = yt_list[key]
            break
        ct+=1

    print("다운중...")
    if not video(yt_url):
        print("제대로 다운되지 않았습니다.")
        sleep(1)
        return 0

    print("성공적으로 다운되었습니다.")
    sleep(1)
    return 1

if __name__ == '__main__':
    while True:
        os.system('cls')
        art()
        print("\n\n\n")
        print("Default Download Folder ./Music\n")
        print("1. 실시간 차트 확인\n")
        print("2. 음악 다운받기\n")
        print("3. 프로그램 종료\n")
        try:
            ch = int(input(">> "))
        except:
            print("숫자를 입력해주세요.")
            sleep(1)
            continue

        if ch == 1:
            chart_50()

        elif ch == 2:
            print("검색어를 입력해주세요.")
            search = input(">> ")

            print("검색중...")
            yt_list = yt_search(search)

            print("\n번호를 선택해주세요.")

            try:
                idx = int(input(">> "))
            except:
                print("숫자를 입력해주세요.")
                sleep(1)
                continue

            if 0 < idx < len(yt_list):
                yt_down(idx,yt_list)
            else:
                print("잘못 입력하셨습니다.")
                sleep(1)
                continue

        elif ch == 3:
            exit()

        else:
            print("잘못 입력하셨습니다.")
            sleep(1)
            continue
