class Game:
    def __init__(self, title, genre, platform, rating):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.rating = rating

class Library:
    def __init__(self):
        self.games = []  # Lista para armazenar os jogos
        self.reservations = {}  # Dicionário para armazenar reservas (usuário: jogo)

    def add_game(self, game):
        self.games.append(game)

    def search_game(self, title):
        for game in self.games:
            if game.title.lower() == title.lower():
                return game
        return None

    def reserve_game(self, user, game):
        if user in self.reservations:
            print(f"{user} already has a reservation.")
        else:
            self.reservations[user] = game
            print(f"{user} reserved {game.title}.")

    def list_all_games(self):
        for game in self.games:
            print(f"{game.title} ({game.genre}) - Platform: {game.platform} - Rating: {game.rating:.1f}")

# Example usage
library = Library()

game1 = Game("The Witcher 3", "RPG", "PC", 9.5)
game2 = Game("Super Mario Odyssey", "Platformer", "Nintendo Switch", 9.0)

library.add_game(game1)
library.add_game(game2)

search_title = "The Witcher 3"
found_game = library.search_game(search_title)
if found_game:
    print(f"Game found: {found_game.title} ({found_game.genre})")
else:
    print(f"Game '{search_title}' not found in the library")

print("\nAll games in the library:")
library.list_all_games()

# Simulate reservations
user1 = "Alice"
user2 = "Bob"
library.reserve_game(user1, game1)
library.reserve_game(user2, game2)
