# Electoral-roll-OCR
INTRO
Last year Election Commision of India made sure that electoral roll cannot be converted to editable format easily by making electoral data into an image format. But image data is not safe now when OCR technology is improving day by day. In this project I have used Tesseract 3(stable) and 4(latest) to fetch data of electoral roll and use strengths of both version to get maximum accuracy.

Tesseract 3, which is stable version till date can be used to whitelist characters, which tesseract 4, which is latest version till date, lacks. Tesseract 4 on other hand have high accuracy on text data.

To fetch data I have used tesseract 3 for numerical and categorical values and tesseract 4 for names.

There were many ways to extract data from electoral roll. One of them would be to extract text of complete image at once and clean the data later. This method, although fast, it is very tedious to clean afterwords. Then I used the fact that in electoral roll all the information have set pattern and are uniformly divided to my advantage.

There were 2 types of pattern in Electoral data in a ward, I'm considering only the first one:

1)Front Page
2)Electoral voters data
1. Front Page
Extracting data from front page was simple as all the data needed to be extracted were in one place. Information we extracted were

Vidhan Sabha
Part Number
Main Town
Polling Station name
Male count
Female count
Total
