# For eg: We will ask user which browser you want?
# Then we can use match browser condition.
browser = input("Enter the browser name: \n")
browser=browser.lower()
match browser:

    case "chrome":
        print("Chrome code executed")
    case "firefox":
        print("ff code executed")
    case "IE":
        print("IE code executed")
    case "Microsoft Edge":
        print("ME code executed")
    case _: # Default case
        print("No browser found!")
