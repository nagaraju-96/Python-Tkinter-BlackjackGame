#Citations:
# BlackJack game rules and structure: https://en.wikipedia.org/wiki/Blackjack
# Python Official Documentation: https://docs.python.org/3/library/tkinter.html
# Python GUI Programming with Tkinter on GeeksforGeeks: https://www.geeksforgeeks.org/python-gui-tkinter/
# Stack Overflow Community: https://stackoverflow.com/questions/tagged/tkinter
# Real Python Tkinter Tutorial: https://realpython.com/python-gui-tkinter/


import tkinter as tk
from tkinter import messagebox
import random

class BlackjackGame:
    def __init__(self, master):
        """ Initialize the BlackjackGame class"""
        self.master = master
        self.master.title("Blackjack")
        self.master.geometry("800x600")
        self.master.configure(bg="#016236")

        self.deck = []  # Initialize the deck
        self.player_hand = []  # Initialize the player's hand
        self.dealer_hand = []  # Initialize the dealer's hand

        self.start_game_ui()

    def get_deck(self):
        """Create and shuffle a deck of cards"""
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        deck = [{"rank": rank, "suit": suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_cards(self):
        """ Deal two cards from the deck"""
        return [self.deck.pop() for _ in range(2)]

    def calculate_hand_value(self, hand):
        """ Calculate the value of a hand in Blackjack """
        value = 0
        num_aces = 0

        for card in hand:
            rank = card["rank"]
            if rank in ["K", "Q", "J"]:
                value += 10
            elif rank == "A":
                num_aces += 1
                value += 11
            else:
                value += int(rank)

        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1

        return value

    def hit(self):
        """ Handle the player choosing to hit"""
        card = self.deck.pop()
        self.player_hand.append(card)
        self.update_display()

        player_value = self.calculate_hand_value(self.player_hand)
        if player_value > 21:
            self.show_message("Bust! You lose.")
            self.end_game()

    def stand(self):
        """ Handle the player choosing to stand """
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        while dealer_value < 17:
            card = self.deck.pop()
            self.dealer_hand.append(card)
            dealer_value = self.calculate_hand_value(self.dealer_hand)
            self.update_display()

        self.show_result()

    def show_result(self):
        """ Display the result of the game """
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        player_value = self.calculate_hand_value(self.player_hand)

        if dealer_value > 21 or dealer_value < player_value:
            self.show_message("You win!")
        elif dealer_value > player_value:
            self.show_message("You lose.")
        else:
            self.show_message("It's a tie!")
        self.contents()
        self.buttons()
        self.end_game()

    def buttons(self):
        """ Display buttons for the user to interact with """
        line_space_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg="#016236", fg="white")
        line_space_label.pack()

        play_again_button = tk.Button(self.master, text="Play Again", command=self.reset_game, font=("Helvetica", 14), bg="#0000FF", fg="black")
        play_again_button.pack(pady=10)

        quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy, font=("Helvetica", 14), bg="red", fg="white")
        quit_button.pack(pady=10)

    def contents(self):
        """ Display the contents of the game """

        # Clear previous content
        for widget in self.master.winfo_children():
            widget.destroy()

        line_space_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg="#016236", fg="white")
        line_space_label.pack()
        line_space_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg="#016236", fg="white")
        line_space_label.pack()

        # Display dealer hand
        dealer_hand_str = ", ".join(f"{card['rank']} of {card['suit']}" for card in self.dealer_hand)
        dealer_hand_label = tk.Label(self.master, text=f"Dealer Hand: {dealer_hand_str}", font=("Helvetica", 18), bg="#016236", fg="white",pady=20)
        dealer_hand_label.pack()

        # Display dealer score
        dealer_score = self.calculate_hand_value(self.dealer_hand)
        dealer_score_label = tk.Label(self.master, text=f"Dealer Score: {dealer_score}", font=("Helvetica", 18,"bold"), bg="#016236", fg="white")
        dealer_score_label.pack()

        line_space_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg="#016236", fg="white")
        line_space_label.pack()

         # Display player hand
        player_hand_str = ", ".join(f"{card['rank']} of {card['suit']}" for card in self.player_hand)
        player_hand_label = tk.Label(self.master, text=f"Player Hand: {player_hand_str}", font=("Helvetica", 18), bg="#016236", fg="white",pady=20)
        player_hand_label.pack()

        # Display player score
        player_score = self.calculate_hand_value(self.player_hand)
        player_score_label = tk.Label(self.master, text=f"Player Score: {player_score}", font=("Helvetica", 18,"bold"), bg="#016236", fg="white")
        player_score_label.pack()

        return player_score, dealer_score 

    def update_display(self):
        """ Update the display based on game state """
        player_score, dealer_score = self.contents()

        if player_score > 21 or dealer_score > 21:
            self.buttons()
        else:
            hit_button = tk.Button(self.master, text="Hit", command=self.hit, font=("Helvetica", 18), bg="blue", fg="white")
            hit_button.pack(side="left", padx=170)

            stand_button = tk.Button(self.master, text="Stand", command=self.stand, font=("Helvetica", 18), bg="#FF5412", fg="white")
            stand_button.pack(side="right", padx=170)

    def show_message(self, message):
        """ Display a message box with the specified message """
        messagebox.showinfo("Game Over", message)

    def reset_game(self):
        """ Reset the game state """
        self.deck = self.get_deck()
        self.player_hand = self.deal_cards()
        self.dealer_hand = self.deal_cards()
        self.update_display()

    def start_game_ui(self):
        """ Display the initial game UI """
        welcome_label = tk.Label(self.master, text="Welcome to Blackjack!", font=("Helvetica", 24, "bold"), bg="#016236", fg="white")
        welcome_label.pack(pady=40)

        play_button = tk.Button(self.master, text="Play", command=self.start_game, font=("Helvetica", 20, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10)
        play_button.pack(pady=100)

    def start_game(self):
        """ Start the game """
        self.reset_game()

    def end_game(self):
        """ Placeholder for any end-of-game actions """
        pass


def main():
    """ Run the main application """
    root = tk.Tk()
    BlackjackGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
