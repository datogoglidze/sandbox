from dataclasses import dataclass


@dataclass
class Card:
    card_number: str

    @property
    def length(self) -> int:
        return len(self.card_number)

    def read_card(self) -> str:
        if self.length_is([15]) and self.starts_with(["34", "37"]) and self.is_valid():
            return "AMEX\n"
        elif self.length_is([13, 16]) and self.starts_with(["4"]) and self.is_valid():
            return "VISA\n"
        elif (
            self.length_is([16])
            and self.starts_with(["51", "52", "53", "54", "55"])
            and self.is_valid()
        ):
            return "MASTERCARD\n"
        else:
            return "INVALID\n"

    def is_valid(self) -> bool:
        results = []

        for digit in range(self.length - 2, -1, -2):
            calculated = str(int(self.card_number[digit]) * 2)

            for i in calculated:
                results.append(int(i))

        for k in range(self.length - 1, -1, -2):
            results.append(int(self.card_number[k]))

        if sum(results) % 10 == 0:
            return True

        return False

    def length_is(self, expected_length: list[int]) -> bool:
        if self.length in expected_length:
            return True

        return False

    def starts_with(self, digits: list[str]) -> bool:
        if self.card_number[: len(digits[0])] in digits:
            return True

        return False


def test_amex() -> None:
    card = Card("378282246310005")
    assert card.is_valid()
    assert card.read_card() == "AMEX\n"


def test_mastercard() -> None:
    card = Card("5555555555554444")
    assert card.is_valid()
    assert card.read_card() == "MASTERCARD\n"


def test_invalid() -> None:
    card = Card("1234567890")
    assert not card.is_valid()
    assert card.read_card() == "INVALID\n"
