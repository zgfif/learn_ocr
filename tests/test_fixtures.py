from pytest import fixture



@fixture
def var1() -> int:
    var1: int = 5
    assert isinstance(var1, int)
    return var1


@fixture
def var2() -> float:
    var2: float = 3.2
    assert isinstance(var2, float)
    return var2


def test_fixtures(var1, var2):
    result = var1 + var2
    assert isinstance(result, float)
    assert result == 8.2
