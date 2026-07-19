from monosim.player import Player
from monosim.board import get_board, get_roads, get_properties, get_community_chest_cards, get_bank
import types
import pandas as pd

def roll_dice_temp(self):
    return 1, 1


def buy(self, dict_road_info, road_name):
        """ Buy road

        :param dict_road_info: (dictionary) Road information
        :param road_name: (String) Road name
        :return:
        """
        print(self._bank)
        road_price = dict_road_info['price']
        # enough money?
        if self._cash < road_price:
            raise Exception('Player {} does not have enough money'.format(self._name))
        # pay bank
        self._bank['cash'] += road_price
        self._cash -= road_price
        # exchange ownership
        dict_road_info['belongs_to'] = self._name
        self._list_owned_roads.append(road_name)
        self._dict_owned_houses_hotels[road_name] = (0, 0)
        # mortgage value
        self._properties_total_mortgageable_amount += dict_road_info['mortgage_value']

        color = dict_road_info['color']
        count_roads_of_color = 0
        for road in self._list_owned_roads:
            if color == self._dict_roads[road]['color']:
                count_roads_of_color += 1
        if color == 'brown' and count_roads_of_color == 2:
            self._dict_owned_colors[color] = True
        elif color == 'light_blue' and count_roads_of_color == 3:
            self._dict_owned_colors[color] = True
        elif color == 'purple' and count_roads_of_color == 3:
            self._dict_owned_colors[color] = True
        elif color == 'orange' and count_roads_of_color == 3:
            self._dict_owned_colors[color] = True
        elif color == 'red' and count_roads_of_color == 3:
            self._dict_owned_colors[color] = True
        elif color == 'yellow' and count_roads_of_color == 3:
            self._dict_owned_colors[color] = True
        elif color == 'green' and count_roads_of_color == 3:
            self._dict_owned_colors[color] = True
        elif color == 'blue' and count_roads_of_color == 2:
            self._dict_owned_colors[color] = True

game_data = []

if __name__ == '__main__':
    import random
    for seed in range(1000, 5000):
    # for seed in [313880]:
    #     print(seed)
        random.seed(seed)
        # bank = dict_bank  # TODO bank needs to be a copy, otherwise the values are accumulated game after game
        bank = get_bank()
        list_board = get_board()
        dict_roads = get_roads()
        dict_properties = get_properties()
        dict_community_chest_cards = get_community_chest_cards()
        community_cards_deck = list(dict_community_chest_cards.keys())
        player1 = Player('player1', 1, bank, list_board, dict_roads, dict_properties, community_cards_deck)
        player2 = Player('player2', 2, bank, list_board, dict_roads, dict_properties, community_cards_deck)

        # player1.roll_dice = roll_dice_temp
        # player1.roll_dice = types.MethodType(roll_dice_temp, player1)

        # player1.buy = types.MethodType(buy, player1)

        player1.meet_other_players([player2])
        player2.meet_other_players([player1])

        list_players = [player1, player2]
        idx_count = 0
        while not player1.has_lost() and not player2.has_lost() and idx_count < 2000:
            for player in list_players:
                player.play()
                state = player.get_state()
                state["game_id"] = seed
                state["turn"] = idx_count
                game_data.append({
                    "game_id": seed,
                    "turn": idx_count,
                    "player": state["name"],
                    "player_number": state["number"],
                    "position": state["position"],
                    "dice_value": state["dice_value"],
                    "cash": state["cash"],
                    "mortgageable_amount": state["mortgageable_amount"],
                    "jail_count": state["jail_count"],
                    "exit_jail": state["exit_jail"],
                    "free_visit": state["free_visit"],

                    "owned_roads": len(state["owned_roads"]),
                    "owned_stations": len(state["owned_stations"]),
                    "owned_utilities": len(state["owned_utilities"]),
                    "total_properties":
                        len(state["owned_roads"])
                        + len(state["owned_stations"])
                        + len(state["owned_utilities"]),

                    "mortgaged_roads": len(state["mortgaged_roads"]),
                    "mortgaged_stations": len(state["mortgaged_stations"]),
                    "mortgaged_utilities": len(state["mortgaged_utilities"]),

                    "monopolies": sum(state["owned_colors"].values()),

                    "houses": sum(v[0] for v in state["owned_houses_hotels"].values()),
                    "hotels": sum(v[1] for v in state["owned_houses_hotels"].values()),

                    "bank_cash": state["bank_cash"],
                    "net_worth": state["cash"] + state["mortgageable_amount"],
                    "has_lost": state["has_lost"]
                })
            idx_count += 1
            # print('--------- ' + str(idx_count) + ' -------------')
            dict_state_p1 = player1.get_state()
            dict_state_p2 = player2.get_state()
            dict_houses_hotels_p1 = player1.get_state()['owned_houses_hotels']
            dict_houses_hotels_p2 = player2.get_state()['owned_houses_hotels']
            list_houses_p1 = [i[0] for i in dict_houses_hotels_p1.values()]
            list_houses_p2 = [i[0] for i in dict_houses_hotels_p2.values()]
            list_hotels_p1 = [i[1] for i in dict_houses_hotels_p1.values()]
            list_hotels_p2 = [i[1] for i in dict_houses_hotels_p2.values()]

            # if seed == 1005 and idx_count == 109:
            if seed == 1006:
                print('-------- ' + str(idx_count) + ' -------------')
                print('{} is in position {} ({}), dice value {}, cash {}, '
                      'mortgageable amount {}, mortgaged_roads {}, bank-cash {}, owned_roads {}, owned_utilities {}, '
                      'owned_stations {}, owned_houses {}, owned_hotels {}, owned_colors {}'.format(dict_state_p1['name'],
                                                                                                    dict_state_p1['position'],
                                                                                                    list_board[dict_state_p1['position']]['name'],
                                                                                                    dict_state_p1['dice_value'],
                                                                                                     dict_state_p1['cash'],
                                                                                                    dict_state_p1['mortgageable_amount'],
                                                                                                     len(dict_state_p1['mortgaged_roads']),
                                                                                                     dict_state_p1['bank_cash'],
                                                                                                    len(dict_state_p1['owned_roads']),
                                                                                                     player1.get_owned_utilities_count(),
                                                                                                    player1.get_owned_stations_count(),
                                                                                                     sum(list_houses_p1), sum(list_hotels_p1),
                                                                                                     sum(dict_state_p1['owned_colors'].values())))
                print('{} is in position {} ({}), dice rolled {}, cash {}, '
                      'mortgageable amount {}, mortgaged_roads {}, bank-cash {}, owned_roads {}, owned_utilities {}, '
                      'owned_stations {}, owned_houses {}, owned_hotels {}, owned_colors {}'.format(dict_state_p2['name'],
                                                                                                    dict_state_p2['position'],
                                                                                                    list_board[dict_state_p2['position']]['name'],
                                                                                                    dict_state_p2['dice_value'],
                                                                                                    dict_state_p2['cash'],
                                                                                                    dict_state_p2['mortgageable_amount'],
                                                                                                    len(dict_state_p2['mortgaged_roads']),
                                                                                                    dict_state_p1['bank_cash'],
                                                                                                    len(dict_state_p2['owned_roads']),
                                                                                                    player2.get_owned_utilities_count(),
                                                                                                    player2.get_owned_stations_count(),
                                                                                                    sum(list_houses_p2), sum(list_hotels_p2),
                                                                                                    sum(dict_state_p2['owned_colors'].values())))
                # print(dict_state_p2['owned_colors'])

        # if player1.has_lost():
        #     # print('Player 1 has lost')
        #     pass
        # elif player2.has_lost():
        #     # print('Player 2 has lost')
        #     pass
        # else:
        #     print(seed)
        #     print('nobody lost')
    
    print(f"Collected {len(game_data)} game states.")
    df = pd.DataFrame(game_data)
    df.to_csv("monopoly_dataset.csv", index=False)
    print("Dataset saved!")