# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///
import requests
from bs4 import BeautifulSoup
from typing import Literal
import re
import json

BASE_URL = "https://www.beybxdb.com"


def clean_name(text):
    """
    Ensure that the text 'GearPoint(GP)' contains a space between 'GearPoint' and '(GP)'.

    Args:
    text (str): The input text to be formatted.

    Returns:
    str: The formatted text with a space between 'GearPoint' and '(GP)'.
    """
    # Use regex to find the pattern 'GearPoint(GP)' and add a space
    formatted_text = re.sub(r"(\w+)\s*\((\w+)\)", r"\1 (\2)", text)
    return formatted_text


def url_template(part: Literal["blade", "ratchet", "bit"]):
    return f"/parts-system-guide/parts/{part}/"


def scape_for(part) -> str:
    template = url_template(part)
    url = f"{BASE_URL}{template}"  # Replace with the actual URL
    result = set()

    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

    # Check if the request was successful
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <a> elements where href starts with `/parts-system-guide/parts/bit/`
    a_elements = soup.find_all("a", href=True)

    filtered_elements = [
        a for a in a_elements if a["href"].startswith(template) and a.find("span")
    ]

    # Print the href and the span text of each filtered <a> element
    seen_urls = []
    for a in filtered_elements:
        href = a["href"]

        if href in seen_urls:
            continue

        div_parent_text = a.parent.parent.parent.get_text(strip=True)
        result.add(clean_name(div_parent_text))

    return result


def main():
    blades = sorted(scape_for("blade"))
    ratchets = sorted(scape_for("ratchet"))
    bits = sorted(scape_for("bit"))

    formatted_blades = [{"name": p, "points": 0} for p in blades]
    formatted_ratchets = [{"name": p, "points": 0} for p in ratchets]
    formatted_bits = [{"name": p, "points": 0} for p in bits]

    data = {
        "blades": formatted_blades,
        "ratchets": formatted_ratchets,
        "bits": formatted_bits,
    }

    js_content = (
        "const parts = " + json.dumps(data, indent=2, separators=(",", ": ")) + ";"
    )
    print(js_content)

    with open("javascrip_parts.txt", "w") as f:
        f.write(js_content)

    # for part in scrape_list:
    #     with open(f"{part}s.txt", "w") as f:
    #         f.writelines("\n".join(perform_scrape(part)))


if __name__ == "__main__":
    main()
