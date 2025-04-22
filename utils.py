import torch
from blackjack import Game


def get_game_state_sparse(game: Game) -> torch.Tensor:
    """
    Returns the featurized game state.

    Returns:
        torch.Tensor: A 104 dimensional vector representing the featurized game state where the first 52 elements
        encode the player's hand and the next 52 encode the dealer's face-up card.

    """
    features = torch.zeros(size=(104,), dtype=torch.float32)
    for card in game.player_hand:
        features[card.index] = 1.

    dealer_face_up = game.dealer_hand[0]
    features[52 + dealer_face_up.index] = 1.

    return features


def get_game_state(game: Game) -> torch.Tensor:

    features = ([(card.index / 52) for card in game.player_hand] +
                [0.] * (5 - len(game.player_hand)) +
                [(game.dealer_hand[0].index / 52)])

    return torch.tensor(features, dtype=torch.float32)


if __name__ == "__main__":
    game = Game()
    print(get_game_state_sparse(game))
    print(get_game_state(game))
