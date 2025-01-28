# import re
# import sys


# def main():
#     print(parse(input("HTML: ")))


# def parse(s):
#     similaire = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
#     if similaire:
#         lien = "https://www.youtube.be/" + similaire.group(1)
#         return lien
#     else:
#         return False




# if __name__ == "__main__":
#     main()




import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search (r"<iframe(.)*><\/iframe>", s):
#         utiliser regex101
        lien = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if lien:
            lien_url = lien.groups()
            return "https://youtu.be/" + lien_url[3]


if __name__ == "__main__":
    main()
