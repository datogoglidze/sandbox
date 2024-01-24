# from cs50 import get_string


def main(card_number):
    # card_number = get_string("Number: ")
    length = len(card_number)
    return read_card(card_number, length)


def read_card(number, length):
    if (
        length_check([15], length)
        and start_check(["34", "37"], number)
        and validity_check(number, length)
    ):
        return "AMEX\n"
    elif (
        length_check([13, 16], length)
        and start_check(["4"], number)
        and validity_check(number, length)
    ):
        return "VISA\n"
    elif (
        length_check([16], length)
        and start_check(["51", "52", "53", "54", "55"], number)
        and validity_check(number, length)
    ):
        return "MASTERCARD\n"
    else:
        return "INVALID\n"


def validity_check(number, length):
    results = []

    for digit in range(length - 2, -1, -2):
        calculated = str(int(number[digit]) * 2)

        for i in calculated:
            results.append(int(i))

    for k in range(length - 1, -1, -2):
        results.append(int(number[k]))

    if sum(results) % 10 == 0:
        return True

    return False


def length_check(expected_length, actual_length):
    if actual_length in expected_length:
        return True

    return False


def start_check(digits, number):
    if number[: len(digits[0])] in digits:
        return True

    return False


def test_amex():
    assert validity_check("378282246310005", len("378282246310005"))
    assert main("378282246310005") == "AMEX\n"


def test_mastercard():
    assert validity_check("5555555555554444", len("5555555555554444"))
    assert main("5555555555554444") == "MASTERCARD\n"


def test_invalid():
    assert not validity_check("1234567890", len("1234567890"))
    assert main("1234567890") == "INVALID\n"
