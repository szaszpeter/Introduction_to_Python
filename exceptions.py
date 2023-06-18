while True:
    try:
        number = int(input("what's your fav number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Zero is invalid")
    except:
        print("Some generic error occured")
        break
    finally:
        print("finally block called")




