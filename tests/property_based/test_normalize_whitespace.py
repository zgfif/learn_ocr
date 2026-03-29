from hypothesis import given, strategies as st
import re


def normalize_white_space(text: str) -> str:
    """
    Normalize all whitespace characters (spaces, tabs, newlines):
    - replace any whitespace sequence with a single space
    - remove leading and trailing whitespace
    """
    splited = text.strip().split()
    return ' '.join(splited)



@st.composite
def some_text(draw) -> str:
    words = draw(
        st.lists(
            st.text(alphabet='abc', min_size=1), # “Сгенерируй случайную строку длиной ≥ 1, состоящую только из символов a, b, c”
            min_size=1, 
            max_size=5
        )
    )
    spaces = draw(
        st.lists(
            st.integers(min_value=1, max_value=5),
            min_size=len(words),
            max_size=len(words)
        )
    )
    text = ""
    for w, s in zip(words, spaces):
        text += w + (' '* s)
    return ' ' + text + ' '


@given(some_text())
def test_normzalize_white_space(text):
    got = normalize_white_space(text)
    if got:
        assert got[0] != ' '
        assert got[-1] != ' '
    
    assert not re.search(r'\s{2,}', got) # no whitespace sequences > 1
    assert got.split() == text.split()
    assert got == normalize_white_space(got)
