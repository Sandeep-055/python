import inflect

def number_to_words(n):
    p = inflect.engine()
    return p.number_to_words(n)

# Example usage
number =int(input(""))
print(number_to_words(number))


from num2words import num2words
def number_to_words(n):
    return num2words(n)
number=int(input(""))
print(number_to_words(number))

word=int(input(""))
currency_name=str(input(""))
amount_words=num2words(word,to='currency', currency=currency_name)
print(amount_words)


words=str(input(""))
#currency1=int(input(""))
money=words.split()[1]
print(money)
