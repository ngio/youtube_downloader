# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

import yt_dlp
import os

def download_youtube_video():
    """사용자 입력 URL을 기반으로 YouTube 영상을 다운로드하는 함수"""
    
    url = input("다운로드할 YouTube 영상 URL을 입력하세요: ").strip()
    
    if not url:
        print("경고: 유효한 URL을 입력해야 합니다.")
        return

    # 📌 수정 1: 다운로드 폴더 경로 설정 
    current_dir = os.getcwd() # 현재 스크립트가 실행되는 디렉토리
    download_dir = os.path.join(current_dir, 'downloads') # 'downloads' 하위 폴더 경로 생성
    
    # 📌 수정 2: 'downloads' 폴더가 없으면 생성
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print(f"[알림] 'downloads' 폴더를 생성했습니다: {download_dir}")

    # 2. 다운로드 옵션 설정
    ydl_opts = {
        #'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 
        'format': 'bestvideo+bestaudio/best',
        
        # 📌 수정 3: outtmpl 옵션에 'download_dir' 경로 추가
        # outtmpl 옵션: 저장될 파일의 템플릿 (경로 포함)
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'), 
        
        'postprocessors': [{
            'key': 'FFmpegMetadata',
            'add_metadata': True,
        }],
    }

    # 3. 다운로드 실행
    try:
        print(f"\n[알림] 다운로드를 시작합니다: {url}")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print("\n🎉 다운로드가 성공적으로 완료되었습니다!")
        print(f"저장된 위치: {download_dir}")
        
    except yt_dlp.utils.DownloadError as e:
        print(f"\n[오류] 다운로드 중 오류가 발생했습니다: {e}")
    except Exception as e:
        print(f"\n[오류] 예상치 못한 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    download_youtube_video()
