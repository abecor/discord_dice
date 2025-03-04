import random as rnd

def get_lategif():
    
    file = open("giflinks.txt")
    gif_links = file.readlines()
    file.close()
    link = rnd.choice(gif_links)
    return(link)
