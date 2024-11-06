def filtered_input(values=None, casting_func=str, prompt="> "):
    while True:
        try:
            raw_input = input(prompt)
            choice = casting_func(raw_input)
            if choice in values:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Try again.")
            continue

