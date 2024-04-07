browser = str(input("Enter browser name:\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed!")
    case "firefox":
        print("Firefox code executed!")
    case "google":
        print("Google code executed!")
    case browser if browser == "fb":
        print("You are entered into fb")
    case browser if browser == "insta":
        print("You are entered into insta")
    case _:
        print("Default browser!")
