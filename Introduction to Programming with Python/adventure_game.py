import time
import random

weapon = ["dagger", "sword", "axe", "magic staff", "crossbow",
          "spear", "mace", "gun"]
your_weapon = None  # Inizializza globalmente


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere "
                "around here,")
    print_pause("and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty (but not very "
                f"effective) {your_weapon}.")


def where_to():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1 or 2).\n")
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2).\n")
    if choice == '1':
        house()
    elif choice == '2':
        cave()


def lose_fight():
    print_pause(f"You do your best...")
    print_pause(f"but your {your_weapon} is no match for the wicked "
                f"fairie.")
    print_pause("You have been defeated!")
    print_pause("GAME OVER - YOU LOST!")
    play_again()


def win_fight():
    print_pause("The wicked fairie attacks you!")
    print_pause(f"As the wicked fairie moves to attack,")
    print_pause(f"you unsheath your new {your_weapon}.")
    print_pause(f"The {your_weapon} shines brightly in your hand as "
                f"you brace yourself for the attack.")
    print_pause(f"But the wicked fairie takes one look at your shiny "
                f"new toy and runs away!")
    print_pause("You have rid the town of the wicked fairie. You are "
                "victorious!")
    print_pause("VICTORY - YOU WON!")
    play_again()


def play_again():
    choice = input("Would you like to play again? (y/n)\n").lower()
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)\n").lower()
    if choice == 'y':
        print_pause("Excellent! Restarting the game...")
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.")


def cave():
    global your_weapon
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found a new weapon!")
    new_weapon = random.choice(weapon)
    print_pause(f"You discard your silly old {your_weapon} and take "
                f"the {new_weapon} with you.")
    your_weapon = new_weapon
    print_pause("You head back out to the field.")
    where_to()


def field():
    print_pause("You run back into the field. Luckily, you don't seem "
                "to have been followed.")
    print_pause("You are safe for now.")
    print_pause("You decide to head home.")
    play_again()


def house():
    global your_weapon
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out "
                "steps a wicked faerie.")
    print_pause("Eep! This is the wicked faerie's house!")
    print_pause("Enter 1 to fight the wicked faerie.")
    print_pause("Enter 2 to run away.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1 or 2).\n")
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2).\n")
    if choice == '1':
        end_of_fight = random.choice([win_fight, lose_fight])
        end_of_fight()
    elif choice == '2':
        field()


def play_game():
    global your_weapon
    your_weapon = random.choice(weapon)
    intro()
    where_to()


play_game()
