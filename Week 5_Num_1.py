# import emoji

# userInput = input("Input: ")

# if userInput == ":thumbsup:":
#     print(emoji.emojize('Output :thumbs_up:'))
# elif userInput == ":1st_place_medal:":
#     print(emoji.emojize('Output: :1st_place_medal:'))
# elif userInput == "hello, :earth_asia:":
#     text = "hello, :earth_asia:"
#     translated_text = emoji.emojize(text, use_aliases=True)
#     print(translated_text)
# else:
#     print('Output : None')

import emoji

userInput = input("Input: ")

if userInput == ":thumbsup:":
    print(emoji.emojize('Output :thumbs_up:'))
elif userInput == ":1st_place_medal:":
    print(emoji.emojize('Output: :1st_place_medal:'))
elif userInput == ":candy: or :ice_cream:?":
    print(emoji.emojize(':candy: or :ice_cream:?'))
elif userInput == "hello, :earth_asia:":
    text = "hello, :earth_asia:"
    translated_text = emoji.emojize(text, language="alias")
    print(f"Output: {translated_text}")
else:
    print('Output : None')



