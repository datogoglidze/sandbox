from cs50 import get_string


def main(card_number):
    # card_number = get_string("Number: ")
    return read_card(card_number)


def read_card(number):
    number_length = len(number)

    if (
        number_length == 15
        and (number[0:2] == "34" or number[0:2] == "37")
        and is_valid(number)
    ):
        return "AMEX\n"
    elif (
        (number_length == 16 or number_length == 13)
        and number[0] == "4"
        and is_valid(number)
    ):
        return "VISA\n"
    elif (
        number_length == 16
        and (
            number[0:2] == "51"
            or number[0:2] == "52"
            or number[0:2] == "53"
            or number[0:2] == "54"
            or number[0:2] == "55"
        )
        and is_valid(number)
    ):
        return "MASTERCARD\n"
    else:
        return "INVALID\n"


def is_valid(number):
    number_length = len(number)
    results = []

    for digit in range(number_length - 2, -1, -2):
        result = str(int(number[digit]) * 2)

        for i in result:
            results.append(int(i))

    total = sum(results)

    for k in range(number_length - 1, -1, -2):
        total += int(number[k])

    if total % 10 == 0:
        return True

    return False


def test_amex():
    assert is_valid("378282246310005") == True
    assert main("378282246310005") == "AMEX\n"


def test_mastercard():
    assert is_valid("5555555555554444") == True
    assert main("5555555555554444") == "MASTERCARD\n"


def test_invalid():
    assert is_valid("1234567890") == False
    assert main("1234567890") == "INVALID\n"
