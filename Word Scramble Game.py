import random
import tkinter as tk
from tkinter import messagebox

# List of words
words = ["apple", "banana", "orange", "grape", "kiwi", "peach", "pear", "watermelon"]

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def check_guess(word, guess):
    return guess.lower() == word

class WordScrambleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Scramble Game")

        self.word_label = tk.Label(root, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.guess_entry = tk.Entry(root, font=("Arial", 18))
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

        self.current_word = ""
        self.scrambled_word = ""
        self.score = 0

        self.new_word()

    def new_word(self):
        self.current_word = random.choice(words)
        self.scrambled_word = scramble_word(self.current_word)
        self.word_label.config(text=self.scrambled_word)
        self.submit_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def check_guess(self):
        guess = self.guess_entry.get()
        if check_guess(self.current_word, guess):
            messagebox.showinfo("Result", "Correct! You unscrambled the word!")
            self.score += 1
        else:
            messagebox.showinfo("Result", f"Sorry, the correct word was: {self.current_word}")

        self.submit_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        self.new_word()

def main():
    root = tk.Tk()
    game = WordScrambleGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()