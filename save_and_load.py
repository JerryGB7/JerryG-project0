import pickle

def load_data():
    with open(f'p_data.pickle', 'rb') as f2:
        saved_player = pickle.load(f2)
    return saved_player

def save_data(player):
    with open(f'p_data.pickle', 'wb') as f:
        pickle.dump(player, f)