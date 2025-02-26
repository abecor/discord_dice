import roll_dice



def test_roll(test_strings):
    for n in test_strings:
        print("===========================")
        print("Testing: " + n)
        print(roll_dice.roll(n))


file = open("test.txt", "r")
test_strings = file.read().split(",")
print(test_strings)
file.close()

usr_input = input("Roll ")

if usr_input == "test":
    test_roll(test_strings)
else:
    print(roll_dice.roll(usr_input))


