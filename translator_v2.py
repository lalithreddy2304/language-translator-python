from deep_translator import GoogleTranslator

def menu():
    print("  ---  LANGUAGE TRANSLATOR ---  ")
    print("1. Translate Text")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")

def chooseLanguage(message):
    print(message)
    print("1. English")
    print("2. Hindi")
    print("3. Telugu")

    try:
        num = int(input("Enter your choice: "))
    except:
        return None

    if num == 1:
        return "en"
    elif num == 2:
        return "hi"
    elif num == 3:
        return "te"
    else:
        return None


while True:

    menu()

    try:
        opt = int(input("Enter your option: "))
    except:
        print("Invalid input")
        continue

    if opt == 1:

        text = input("Enter the text: ")

        lang_sorurce = chooseLanguage("Choose source Language")
        lang_chose = chooseLanguage("Choose Target Language")

        if lang_sorurce is None or lang_chose is None:
            print("Invalid language selected!")
            continue

        translator = GoogleTranslator(
            source=lang_sorurce,
            target=lang_chose
        )

        try:
            result = translator.translate(text)

            print(f"\nTranslated Text: {result}")

            with open("history.txt", "a") as file:
                file.write(f"{text} ---> {result}\n")

            print("Translation saved")

        except:
            print("Translation failed")

    elif opt == 2:

        with open("history.txt", "r") as file:
            content = file.read()

            if content == "":
                print("No history found.")
            else:
                print("HISTORY\n")
                print(content)

    elif opt == 3:

        with open("history.txt", "w"):
            pass

        print("History cleared")

    elif opt == 4:

        print("exiting")
        break

    else:

        print("Invalid option")