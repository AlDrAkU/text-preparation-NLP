from prep_text import PrepareText






if __name__ ==  "__main__":
    text = """His exquisite sincerity education shameless ten earnestly breakfast add. So we me unknown as improve hastily sitting forming. 
Especially favourable compliment but thoroughly unreserved saw she themselves. Sufficient impossible him may ten insensible put continuing. 
Oppose exeter income simple few joy cousin but twenty.
Scale began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can.
On projection apartments unsatiable so if he entreaties appearance. Rose you wife how set lady half wish. Hard sing an in true felt. 
Welcomed stronger if steepest ecstatic an suitable finished of oh. Entered at excited at forming between so produce. 
Chicken unknown besides attacks gay compact out you. Continuing no simplicity no favourable on reasonably melancholy estimating.
Own hence views two ask right whole ten seems. What near kept met call old west dine. Our announcing sufficient why pianoforte."""


    prep = PrepareText(text)
    print(prep.tokenizeToWords())
    print(prep.removeNumbers())
    print(prep.lowercaseText())
    print(prep.removeWhitespaces())
    print(prep.removeStopWords())
    print(prep.removePunctuation())


 