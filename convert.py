import re
import pyperclip

## Get the copied content from the clipboard
#copied_content = pyperclip.paste()
#
##link=input('Enter the link')
#
#
## Use a regular expression to check if the content matches the link format
#match = re.search(r'https://item\.taobao\.com/item\.htm\?spm=.+?&id=(\d+)', copied_content)
##match = re.search(r'https://item\.taobao\.com/item\.htm\?spm=.+?&id=(\d+)', link)
#
## If there's a match, extract the ID and create the new link
#if match:
#    id = match.group(1)
#    new_link = f'https://item.taobao.com/item.htm?id={id}'
#
#    # Replace the old link with the new link in the clipboard
#    pyperclip.copy(new_link)
#    #print(new_link)

#regex for Taobao link
taobao_regex = r'https://item.taobao.com/item.htm\?spm=.+&id=(\d+).*'

#regex for Tmall link
tmall_regex = r'https://detail.tmall.com/item.htm\?.+&id=(\d+).*'

#regex for Taobao shop link
shop_regex = r"https://[a-zA-Z0-9-]+\.(taobao\.com)/\?.*"

clipboard_content = pyperclip.paste()

#if the clipboard contains a Taobao link
match = re.match(taobao_regex, clipboard_content)
if match:
    item_id = match.group(1)
    new_link = f"https://item.taobao.com/item.htm?id={item_id}"
    pyperclip.copy(new_link)

#if the clipboard contains a Tmall link
match = re.match(tmall_regex, clipboard_content)
if match:
    item_id = match.group(1)
    new_link = f"https://detail.tmall.com/item.htm?id={item_id}"
    pyperclip.copy(new_link)

match = re.match(shop_regex, clipboard_content)
if match:
    new_url = re.sub(r'\?.*$', '', clipboard_content)
    pyperclip.copy(new_url)
