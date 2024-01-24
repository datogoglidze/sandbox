from dataclasses import dataclass


@dataclass
class Card:
    number: str

    @property
    def length(self) -> int:
        return len(self.number)

    def read_card(self) -> str:
        if (
            self.length_check([15])
            and self.start_check(["34", "37"])
            and self.validity_check()
        ):
            return "AMEX\n"
        elif (
            self.length_check([13, 16])
            and self.start_check(["4"])
            and self.validity_check()
        ):
            return "VISA\n"
        elif (
            self.length_check([16])
            and self.start_check(["51", "52", "53", "54", "55"])
            and self.validity_check()
        ):
            return "MASTERCARD\n"
        else:
            return "INVALID\n"

    def validity_check(self) -> bool:
        results = []

        for digit in range(self.length - 2, -1, -2):
            calculated = str(int(self.number[digit]) * 2)

            for i in calculated:
                results.append(int(i))

        for k in range(self.length - 1, -1, -2):
            results.append(int(self.number[k]))

        if sum(results) % 10 == 0:
            return True

        return False

    def length_check(self, expected_length: list[int]) -> bool:
        if self.length in expected_length:
            return True

        return False

    def start_check(self, digits: list[str]) -> bool:
        if self.number[: len(digits[0])] in digits:
            return True

        return False


def test_amex() -> None:
    card = Card("378282246310005")
    assert card.validity_check()
    assert card.read_card() == "AMEX\n"


def test_mastercard() -> None:
    card = Card("5555555555554444")
    assert card.validity_check()
    assert card.read_card() == "MASTERCARD\n"


def test_invalid() -> None:
    card = Card("1234567890")
    assert not card.validity_check()
    assert card.read_card() == "INVALID\n"
