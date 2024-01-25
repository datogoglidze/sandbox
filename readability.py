def main(text: str) -> str:
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

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


def count_letters(text: str) -> int:
    return sum([1 for i in range(len(text)) if text[i].isalpha()])


def count_words(text: str) -> int:
    return text.count(" ") + 1


def count_sentences(text: str) -> int:
    return text.count(".") + text.count("?") + text.count("!")


def test_before_grade_one():
    text_ = "Text: One fish. Two fish. Red fish. Blue fish."
    assert count_letters(text_) == 33
    assert count_words(text_) == 9
    assert count_sentences(text_) == 4
    assert main(text_) == "Before Grade 1"


def test_grade_three():
    text_ = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
    assert main(text_) == "Grade 3"


def test_grade_five():
    text_ = (
        "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more "
        "than any other time of year. For another, he really wanted to do his homework, but was forced to do it "
        "in secret, in the dead of the night. And he also happened to be a wizard."
    )
    assert main(text_) == "Grade 5"


def test_grade_eight():
    text_ = (
        "When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, "
        "and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about "
        "his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his "
        "hand was at right angles to his body, his thumb parallel to his thigh."
    )
    assert main(text_) == "Grade 8"


def test_grade_max():
    text_ = (
        "A large class of computational problems involve the determination of properties of graphs, digraphs, "
        "integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other "
        "countable domains."
    )
    assert main(text_) == "Grade 16+"
