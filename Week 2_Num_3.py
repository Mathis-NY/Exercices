name = input("File name: ").lower().strip()

if ".gif" in name:
    print("image/gif")
elif ".jpg" in name:
    print("image/jpeg")
elif ".jpeg" in name:
    print("image/jpeg")
elif ".png" in name:
    print("image/png")
elif ".pdf" in name:
    print("application/pdf")
elif ".zip" in name:
    print("application/zip")
elif ".txt" in name:
    print("text/plain")
else:
    print("application/octet-stream")
