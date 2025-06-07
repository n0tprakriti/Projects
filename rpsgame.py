import tkinter as tk
import random

# Global scores
player_score = 0
computer_score = 0
high_score = 0
auto_playing = False

# Choices
choices = ['Rock', 'Paper', 'Scissors']
emojis = {'Rock': '🪨', 'Paper': '📄', 'Scissors': '✂️'}

# Game logic
def play(player_choice=None):
    global player_score, computer_score, high_score

    if player_choice is None:
        player_choice = random.choice(choices)

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        player_score += 1
        result = "You Win! 🎉"
    else:
        computer_score += 1
        result = "Computer Wins! 🤖"

    # Update high score
    if player_score > high_score:
        high_score = player_score

    # Update UI
    user_label.config(text=f"You: {player_choice} {emojis[player_choice]}")
    computer_label.config(text=f"Computer: {computer_choice} {emojis[computer_choice]}")
    result_label.config(text=result)
    score_label.config(text=f"You: {player_score} | Computer: {computer_score}")
    high_score_label.config(text=f"🏆 Best Score: {high_score}")

    # Repeat if autoplay is on
    if auto_playing:
        root.after(3000, play)

def toggle_auto_play():
    global auto_playing
    auto_playing = not auto_playing
    auto_btn.config(text="Stop Auto-Play" if auto_playing else "Start Auto-Play")
    if auto_playing:
        play()

def reset_game():
    global player_score, computer_score, auto_playing
    player_score = 0
    computer_score = 0
    auto_playing = False
    user_label.config(text="You: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Result: ")
    score_label.config(text="You: 0 | Computer: 0")
    auto_btn.config(text="Start Auto-Play")

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game 🎮")
root.geometry("420x500")
root.config(bg="#f0f8ff")
root.resizable(False, False)

tk.Label(root, text="🪨 Rock - 📄 Paper - ✂️ Scissors", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#444").pack(pady=10)

# Game buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

style = {'width': 10, 'font': ("Arial", 12, "bold")}

tk.Button(button_frame, text="Rock", **style, bg="#aad4f5", command=lambda: play('Rock')).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", **style, bg="#bffcc6", command=lambda: play('Paper')).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", **style, bg="#ffdfba", command=lambda: play('Scissors')).grid(row=0, column=2, padx=5)

# Labels
user_label = tk.Label(root, text="You: ", font=("Arial", 13), bg="#f0f8ff")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 13), bg="#f0f8ff")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), fg="blue", bg="#f0f8ff")
result_label.pack(pady=10)

score_label = tk.Label(root, text="You: 0 | Computer: 0", font=("Arial", 13), bg="#f0f8ff")
score_label.pack(pady=5)

high_score_label = tk.Label(root, text="🏆 Best Score: 0", font=("Arial", 12), bg="#f0f8ff", fg="#008000")
high_score_label.pack(pady=5)

# Control buttons
tk.Button(root, text="Reset Game", command=reset_game, bg="#ff4d4d", fg="white", font=("Arial", 12)).pack(pady=8)

auto_btn = tk.Button(root, text="Start Auto-Play", command=toggle_auto_play, bg="#6c6cff", fg="white", font=("Arial", 12))
auto_btn.pack(pady=8)

tk.Label(root, text="Enjoy and Beat the Bot! 😄", font=("Arial", 10, "italic"), bg="#f0f8ff").pack(pady=10)

root.mainloop()
