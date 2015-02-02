"""This program takes an argument -- a single url -- from the command line
   and saves the webpage as file with the same name as the page but with a
   prepended "website-saver-" (E.g., google.com/index.php is saved as 
   website-saver-index.php) in the working directory."""

import sys
import urllib.request

def get_file(url):
    """Takes url, downloads file"""
    if not valid_url(url):
        print("Not a valid url!")
        return
    response = urllib.request.urlopen(url)
    print("Got file!")
    html = response.read()
    filename = get_file_name(url)
    save_file(str(html), "website-saver-" + filename)

def get_file_name(url):
    return url.split("/")[-1]

def valid_url(url):
    """Sees if url looks like a valid url. Full disclosure: really stupid
       function, I'm just writing it for the experience."""
    if (url[:8] == "https://" or url[:7] == "http://" or
        url[-4:] == ".htm" or url[-5:] == ".html" or
        url[-4:] == ".php" or url[-1] != "/"): # so terrible
        return True
    else:
        return False

def save_file(data, filename):
    """File saver helper function"""
    f = open(filename, "w")
    f.write(data)
    print("Saved file!")

if __name__ == "__main__":
    """Why did the ckicekn cross the road?
       To see if she was on __main__ street! :D"""
    args = sys.argv
    if len(args) < 2:
        print("You forgot a URL!\nProper usage: python3 website-saver.py [URL]")
        exit()
    url = args[1] # hopefully a url...
    get_file(url)
    print("Finished program!?")
    