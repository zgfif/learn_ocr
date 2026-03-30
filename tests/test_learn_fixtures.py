import pytest

# @pytest.fixture
# def data(request):
#     return request.param * 2



@pytest.mark.parametrize("data", [1, 2, 3], indirect=True)
def test_data(data) -> None:
    assert data in [2, 4, 6]

