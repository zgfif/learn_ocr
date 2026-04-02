import pytest

import app.has_template as module
from app.has_template import has_template


@pytest.mark.parametrize(
        'coordinates, expected', 
        [
            ([], False),
            (None, False),
            ([(10, 20)], True),
            ([(10, 20), (30, 40)], True),
        ]
)
def test_has_template(
    mocker, 
    coordinates, 
    expected
) -> None:
    fake_image = object()
    fake_template = object()

    mock = mocker.patch.object(
        module,
        "find_template_coordinates", 
        return_value=coordinates
    )
    result = has_template(fake_image, fake_template)  # type: ignore[arg-type]
    assert result == expected
    mock.assert_called_once_with(image=fake_image, template=fake_template)

