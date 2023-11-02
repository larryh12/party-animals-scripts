import pyautogui
import time
import random

if __name__ == "__main__":
    start_time = time.time()
    game_count = 0

    try:
        while True:
            start = pyautogui.locateCenterOnScreen("res/btn-start.png", confidence=0.9)

            if start:
                pyautogui.click(start)
                print("Start button found. Starting new game...")
                game_count += 1
                print(f"Total games played: {game_count}")

            pyautogui.press("space")

            sleep_time = random.randint(5, 10)
            print(f"Sleeping for {sleep_time} seconds...")
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        end_time = time.time()
        elapsed_time = end_time - start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        print("Script terminated by user.")
        print(
            f"Total time running: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        )
        print(f"Total games played: {game_count}")
