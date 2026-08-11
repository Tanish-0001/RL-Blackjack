# Blackjack Reinforcement Learning

A single-deck Blackjack environment in which the dealer stands on 17, with optional five-card Charlie. The project compares two agents that learn when to hit or stand.

## Approaches

- **DQN:** Uses a ~30k parameter NN. Encodes up to five player cards and the dealer's visible card as a six-value vector. A multilayer neural network estimates the Q-values for hit and stand, trained for 200,000 episodes with epsilon-greedy exploration, experience replay, and a periodically updated target network.
- **Tabular Q-learning:** Uses player-card ranks and dealer's upcard as the state, combining all ten-value cards. It trains a dictionary of hit/stand Q-values for 10 million episodes with epsilon-greedy exploration and a per-state-action scheduled learning rate of `1 / visits`.

## Results

Greedy policies were evaluated over 10,000 freshly shuffled games with five-card Charlie enabled.

| Agent | Win rate |
| --- | ---: |
| DQN | **41.52%** |
| Tabular Q-learning | **44.36%** |

Run `play_blackjack.py` to play interactively against the dealer. The training implementations are in `RL_player.ipynb` and `QTable_player.ipynb`.
