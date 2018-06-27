def extract_url(some_text):
    splitted_text = some_text.split(" ")
    for url in splitted_text:
        if url.startswith("http://"):
            print(url)


extract_url("http://www.google.com ")
extract_url("this is a test http://www.facebook.com ")
extract_url("this is a test http://www.something-cool.com for other text")
extract_url("this is a test www.something-Not-cool.com.http:// for other text")
