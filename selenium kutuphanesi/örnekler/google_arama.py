import webbrowser

new=2
tabUrl ="https://www.google.com.tr/?gfe_rd=cr&ei=UFsPWce8NrTY8AfuiJnwBw&gws_rd=ssl#safe=off&q="
term= input("enter search query: ")

webbrowser.open(tabUrl+term,new=new)
