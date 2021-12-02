DAY = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

GIFTS = ["and a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "]

def recite(start_verse, end_verse):    
    whole_song = []

    for verse in range(start_verse, end_verse+1):
        song = []
        song.append(f"On the {DAY[verse-1]} day of Christmas my true love gave to me: ")
        
        if verse == 1:
            song.append("a Partridge in a Pear Tree.")
        
        else:
            last_index = verse-1
            gift_list = []

            while last_index >=  0:
                gift_list.append(GIFTS[last_index])
                last_index += -1
            for gift in gift_list: song.append(gift)
        whole_song.append("".join(song))
    
    return whole_song
