# There is another alternate way which is an older way of using it.
def main():
    print("Main Method Called")


if __name__ == "__main__":  # This way is similar to Java main method calling. But now people don't use it these days.
    # but via this method, we can "RUN" option in pycharm. In the last Lab_137, we didn't see "RUN" option. We have
    # to select the entire program then we can run but in this case, we can execute the program by run option.

    main()
# if __name__ == "__main__": In this code, this line will be executed it is telling you that if the name is "__main__"
# then run this method: main() and in the output we can see this->   print("Main Method Called") will get printed.
# Some people prefer to use this method and some not.
# you are telling your python interpreter that start your execution from this line: if __name__ == "__main__": and
# execute this function:  --> main()
