import os
import sys

try:
    import cv2
    import pygame
except ImportError as e:
    print(f"\nHATA: Gerekli kütüphaneler eksik! -> {e}")
    print("Lütfen terminale şu komutu yazarak kütüphaneleri kurun:")
    print("py -3.11 -m pip install opencv-python pygame")
    input("\nKapatmak için Enter'a basın...")
    sys.exit()

def play_bad_apple(video_path, audio_path):
    if not os.path.exists(video_path) or not os.path.exists(audio_path):
        print("\nHATA: 'bad_apple.mp4' veya 'bad_apple.mp3' dosyası bu klasörde bulunamadı!")
        print("Lütfen video ve ses dosyalarının bu kodla aynı klasörde olduğundan emin olun.")
        input("\nKapatmak için Enter'a basın...")
        return

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(audio_path)
    except Exception as e:
        print(f"Ses dosyası yüklenemedi: {e}")
        input()
        return
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Hata: Video açılmadı.")
        input()
        return

    cv2.namedWindow("Bad Apple!!", cv2.WINDOW_NORMAL)
    pygame.mixer.music.play()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, threshold_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

        cv2.imshow("Bad Apple!!", threshold_frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    pygame.mixer.music.stop()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"\nŞu anki klasör: {current_dir}")
    print(f"Klasör içindeki dosyalar: {os.listdir(current_dir)}")
    
    video_dosyasi = os.path.join(current_dir, "bad_apple.mp4")
    ses_dosyasi = os.path.join(current_dir, "bad_apple.mp3")
    play_bad_apple(video_dosyasi, ses_dosyasi)
