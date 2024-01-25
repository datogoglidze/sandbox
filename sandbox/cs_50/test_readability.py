from dataclasses import dataclass


@dataclass
class Text:
    text: str

    def count_letters(self) -> int:
        return sum([1 for i in range(len(self.text)) if self.text[i].isalpha()])

    def count_words(self) -> int:
        return self.text.count(" ") + 1

    def count_sentences(self) -> int:
        return self.text.count(".") + self.text.count("?") + self.text.count("!")


def main(text: Text) -> str:
    letters = text.count_letters()
    words = text.count_words()
    sentences = text.count_sentences()

    grade = round(
        0.0588 * (letters / words * 100.00)
        - 0.296 * (sentences / words * 100.00)
        - 15.8
    )

    if grade < 2:
        return "Before Grade 1"
    elif grade > 15:
        return "Grade 16+"
    else:
        return f"Grade {grade}"


def test_before_grade_one() -> None:
    text_ = Text("Text: One fish. Two fish. Red fish. Blue fish.")
    assert text_.count_letters() == 33
    assert text_.count_words() == 9
    assert text_.count_sentences() == 4
    assert main(text_) == "Before Grade 1"


def test_grade_three() -> None:
    text_ = Text(
        "Congratulations! Today is your day. "
        "You're off to Great Places! You're off and away!"
    )
    assert main(text_) == "Grade 3"


def test_grade_five() -> None:
    text_ = Text(
        "Harry Potter was a highly unusual boy in many ways. "
        "For one thing, he hated the summer holidays more "
        "than any other time of year. For another, "
        "he really wanted to do his homework, but was forced to do it "
        "in secret, in the dead of the night. "
        "And he also happened to be a wizard."
    )
    assert main(text_) == "Grade 5"


def test_grade_eight() -> None:
    text_ = Text(
        "When he was nearly thirteen, my brother Jem got his "
        "arm badly broken at the elbow. When it healed, "
        "and Jem's fears of never being able to play football were assuaged, "
        "he was seldom self-conscious about "
        "his injury. His left arm was somewhat shorter than his right; "
        "when he stood or walked, the back of his "
        "hand was at right angles to his body, "
        "his thumb parallel to his thigh."
    )
    assert main(text_) == "Grade 8"


def test_grade_max() -> None:
    text_ = Text(
        "A large class of computational problems involve the determination "
        "of properties of graphs, digraphs, "
        "integers, arrays of integers, finite families of finite sets, "
        "boolean formulas and elements of other "
        "countable domains."
    )
    assert main(text_) == "Grade 16+"
