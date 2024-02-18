import pyttsx3
import PyPDF2

book = open("short-stories-for-children.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)
total_pages = len(pdfReader.pages)
print(f"Total number of pages: {total_pages}")

speaker = pyttsx3.init()

# Adjust the speech speed (rate)
speed = 300  # You can adjust this value as needed
speaker.setProperty('rate', speed)

speaker = pyttsx3.init()
start_page = 5
end_page = 6

speaker.say(f"Let's begin reading from page {start_page} to {end_page}.")

for page_number in range(start_page, end_page + 1):
    page = pdfReader.pages[page_number - 1]  # Adjusting to 0-based index
    text = page.extract_text()
    speaker.say(text)

speaker.runAndWait()
book.close()  # Close the PDF file after use
