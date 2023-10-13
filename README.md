# Website Broken Link Checker

This Python script allows you to check for broken links on a website. It identifies and reports links that return a status code greater than or equal to 400, indicating a broken or invalid link.

## Prerequisites

- Python 3
- Required Python libraries: `requests`, `beautifulsoup4`

You can install the required libraries using `pip`:

```bash
pip install requests
pip install beautifulsoup4
```

## Usage

1. Save the Python script, `check_broken_links.py`, to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located:

```bash
cd /path/to/script/directory
```

4. Run the script, providing the URL of the website you want to check as a command-line argument:

```bash
python check_broken_links.py <website_url>
```

Replace `<website_url>` with the URL of the website you want to check for broken links.

Example:

```bash
python check_broken_links.py https://example.com
```

5. The script will start checking the website for broken links and display a message for each broken link it finds, showing the URL of the broken link.

## Output

The script will output messages indicating the progress and status of link checking. If it finds any broken links, it will display a message for each one, showing the URL of the broken link.

## Example Output

```bash
Broken link found: https://example.com/non_existent_page
```

## Notes

- The script recursively follows links on the website, so it will check both the main page and linked pages for broken links.
- A broken link is identified when the HTTP status code of the link's response is greater than or equal to 400.

## Troubleshooting

If you encounter any issues or errors while using the script, make sure you have installed the required libraries and that you have provided a valid website URL as a command-line argument.

## Disclaimer

This script provides a basic method for checking broken links on a website. It may not cover all possible scenarios, and the accuracy of the results depends on the website's structure and the availability of linked resources.
```

You can copy and paste this markdown text into your README.md file or any markdown-compatible platform.