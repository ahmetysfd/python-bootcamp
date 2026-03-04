import random

def random_two(card_list):
    deal_cards = []

    deal_cards.append(random.choice(card_list))
    deal_cards.append(random.choice(card_list))

    return deal_cards

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = random_two(cards)
comp_cards = random_two(cards)

def calculate_score(user_cards, comp_cards):

    sum_user = sum(user_cards)
    print(f"sum user is: {sum_user}")
    sum_comp = sum(comp_cards)
    print(f"sum comp is: {sum_comp}")

    if sum_comp == 21 or sum_user == 21:
        print("Black Jack!")
        return 0

    if sum_comp > 21 and 11 in sum_comp:
        sum_comp.remove(11)
        sum_comp.append(1)
    if sum_user > 21 and 11 in sum_user:
        sum_user.remove(11)
        sum_user.append(1)

    if sum_user != 0:
        new_card = input("Do you want another card?")




print(user_cards)
print(comp_cards)
calculate_score(user_cards, comp_cards)


