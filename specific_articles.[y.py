import re    # give us access to regular expression

article = open('C:\\Users\\sangariej\\Desktop\\projectone1\\readme.txt',encoding="utf-8")  # open flie
read = article.read()   # read the file


result = re.finditer("apple", str(read))    #  find all the occurrences of apple



with open("C:\\Users\\sangariej\\Desktop\\projectone1\\sentimental.txt", 'w', encoding="utf-8") as f:  # open a empty file name sentimental.txt
    for match in result:    # create a for loop for going through every element in the file
        apple = match         # set match variable to apple

        start = apple.start()    # initial  a starting position before before any occurence of apple
        end = apple.end()          # initial a ending position after the word apple in all occurences

        print("________________")


        f.write(read[start - 200:end + 200])      # get 200 characters or indexes before and after the word apple on all ocurrences
    f.close()