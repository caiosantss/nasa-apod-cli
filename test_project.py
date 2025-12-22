import datetime
from project import get_date_from_user, display_image_info


def test_get_date_from_user_today():
    """If user inputs empty string, should return today's date."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    assert get_date_from_user("") == today


def test_get_date_from_user_valid_date():
    """Valid date should be returned unchanged."""
    assert get_date_from_user("2023-08-15") == "2023-08-15"


def test_get_date_from_user_invalid_date():
    """Invalid date format should raise ValueError."""
    try:
        get_date_from_user("15-08-2023")
    except ValueError:
        assert True
    else:
        assert False


def test_display_image_info_runs_without_error(capsys):
    """display_image_info should print expected fields without crashing."""
    fake_data = {
        "date": "2023-08-15",
        "title": "Test Image",
        "media_type": "image",
        "explanation": "This is a test explanation.",
        "url": "https://example.com/image.jpg"
    }

    display_image_info(fake_data)
    captured = capsys.readouterr()

    assert "Test Image" in captured.out
    assert "2023-08-15" in captured.out
    assert "This is a test explanation." in captured.out
