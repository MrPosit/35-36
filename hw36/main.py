import random

class Game:
    def __init__(self):
        self.player_hp = 100
        self.computer_hp = 100
        self.player_mana = 50
        self.round_counter = 0

    def play_round(self):
        self.round_counter += 1
        print(f"Round {self.round_counter}:")

        player_move = input("Your move (attack/defend): ")
        computer_move = random.choice(["attack", "defend"])

        if player_move == "attack" and computer_move == "defend":
            print("You attack, computer defends.")
            self.computer_hp -= 10
        elif player_move == "defend" and computer_move == "attack":
            print("You defend, computer attacks.")
            self.player_hp -= 10
        elif player_move == "attack" and computer_move == "attack":
            print("Both attack.")
            self.player_hp -= 10
            self.computer_hp -= 10
        elif player_move == "defend" and computer_move == "defend":
            print("Both defend.")

        print(f"Player HP: {self.player_hp}")
        print(f"Computer HP: {self.computer_hp}")

    def game_over(self):
        if self.player_hp <= 0 or self.computer_hp <= 0 or self.round_counter >= 10:
            return True
        else:
            return False

    def display_game_status(self):
        print(f"\n--- Game Status ---")
        print(f"Player HP: {self.player_hp}")
        print(f"Computer HP: {self.computer_hp}")
        print(f"Player Mana: {self.player_mana}")
        print(f"Round: {self.round_counter}\n")

    def play_game(self):
        print("==== Welcome to the Game ====")
        while not self.game_over():
            self.display_game_status()
            self.play_round()

        if self.player_hp <= 0 and self.computer_hp <= 0:
            print("It's a tie!")
        elif self.player_hp <= 0:
            print("You lost the game!")
        elif self.computer_hp <= 0:
            print("Congratulations! You won the game!")
        else:
            print("Game over.")

game = Game()
game.play_game()
