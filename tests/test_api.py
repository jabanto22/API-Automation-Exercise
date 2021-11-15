import requests

from json import dumps
from uuid import uuid4

BASE_URL = "http://216.10.245.166"


def test_solution():
    # Add a new book using /Library/Addbook.php endpoint and POST as request method
    unique_name = f"Learn Appium Automation with Python {str(uuid4())}"
    unique_isbn = f"ISBN {str(uuid4())}"
    unique_aisle = "227"
    unique_author = f"Author {str(uuid4())}"

    payload = dumps(
        {
            "name": unique_name,
            "isbn": unique_isbn,
            "aisle": unique_aisle,
            "author": unique_author,
        }
    )
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    addbook_url = BASE_URL + "/Library/Addbook.php"
    post_response = requests.post(url=addbook_url, data=payload, headers=headers)

    # Verify the status code of the request
    assert post_response.status_code == 200

    # Verify the success mesage on the response JSON
    post_response_json = post_response.json()
    assert post_response_json["Msg"] == "successfully added"
    assert post_response_json["ID"] == unique_isbn + unique_aisle

    # GET the book details using /Library/Getbook.php?AuthorName=<author_name> endpoint
    # and GET as request method
    getbook_url = BASE_URL + f"/Library/GetBook.php?AuthorName={unique_author}"
    get_response = requests.get(getbook_url)

    # Verify the status code of the response
    assert get_response.status_code == 200

    # Verify the details on the JSON response
    get_response_json = get_response.json()[0]
    assert get_response_json["book_name"] == unique_name
    assert get_response_json["isbn"] == unique_isbn
    assert get_response_json["aisle"] == unique_aisle
