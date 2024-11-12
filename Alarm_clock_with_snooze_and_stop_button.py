from playsound import playsound
import time

# Constants for terminal control sequences
CLEAR_SCREEN = "\033[2J"
RETURN_TO_START = "\033[H"

def alarm(duration_seconds):
    """Sets an alarm to go off after the specified duration in seconds, with options to snooze or stop."""
    print(CLEAR_SCREEN)
    elapsed_time = 0

    # Countdown loop
    while elapsed_time < duration_seconds:
        time.sleep(1)
        elapsed_time += 1

        # Calculate time left in minutes and seconds
        time_left = duration_seconds - elapsed_time
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Display time left, updating in-place
        print(f"{RETURN_TO_START}Time left: {minutes_left:02d}:{seconds_left:02d}")
    
    # Alarm goes off when time is up
    playsound("alarm.mp3")
    print("Alarm! Time is up.")

    # Offer options to snooze or stop
    while True:
        user_input = input("Enter 's' to snooze or 'x' to stop: ").strip().lower()
        if user_input == 's':
            try:
                snooze_minutes = int(input("Enter snooze time in minutes: "))
                snooze_seconds = snooze_minutes * 60
                print(f"Snoozing for {snooze_minutes} minutes...")
                alarm(snooze_seconds)  # Call alarm again with snooze time
                break
            except ValueError:
                print("Invalid input. Please enter a valid number of minutes.")
        elif user_input == 'x':
            print("Alarm stopped.")
            break
        else:
            print("Invalid choice. Please enter 's' for snooze or 'x' for stop.")

if __name__ == "__main__":
    # Get user input in minutes and convert to seconds
    try:
        time_input = int(input("Enter the time to sleep in minutes: "))
        total_seconds = time_input * 60
        alarm(total_seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number of minutes.")
