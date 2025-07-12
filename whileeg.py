corrected_pin="12345"
attempt=1
while(attempt<3):
    num=input("ENTER YOUR PIN:")
    if num==corrected_pin:
        print("access granted")

    else:
        print("not granted")

if attempt>3:
    print("card is blocked")
