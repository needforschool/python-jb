from quote import Quote

quotes = [
    "Clic baw, ah les b**** ils ont fumé Pop Simoké.",
    "Frère si j'sors la AK, j'sais qu'ils feront tous caca.",
    "I am not the danger skyler, I am the danger.",
    "A quoi sert ton million si tu prends perpet' ?",
    "T'as un crampté ? Apagnan ! Quoicoubeh, quoicoubeh, quoicoubeh, quoicoubeh !",
    "J'ai le cigare au bord des lèvres.",
    "C'est pas parce que voilà que t'as capté et au final c'est toujours la même chose donc bon c'est tout."
]

# Create an instance of the class
quote = Quote(quotes)

# Get a random quote
random_quote = quote.get_random_quote()

# Print the random quote
print(random_quote)