#Keyword Arguments = An argument precedded by an identifier
#                    Helps with readability
#                    Order of Arguments does not matter
#                    1.positional , 2.default , 3.KEYWORDS , 4.arbitrary

def greetings(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

greetings("Hellow", title="Mr.", first="Shrixtacy", last="Dass")
greetings("Hello", last="Shit", first="Bull", title="Mrs.")       #here we applied keyword argument where we set the keywords and what shall they answer


print("1", "2", "3" , sep="-")


#Make a function to generate a phone number

def get_num(Country, area, first4, last4):
    return f"{Country}-{area}-{first4}-{last4}"

phone_num = get_num(Country=91, area=82, last4=6054, first4=2544)

print(phone_num)