import string
hashtag = input("Enter the hashtag ")

if len(hashtag) > 139:
    hashtag = hashtag[:139]
    print("Are u kidding me, more than 140?")

hashtag = hashtag.title()
hashtag = hashtag.replace(" ", "")

for char in string.punctuation:
    hashtag = hashtag.replace(char, "")
hashtag = "#" + hashtag
print(hashtag)
