# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    print(s.replace("!", ""))


remove_exclamation_marks("Hi! Hello!")
remove_exclamation_marks("")
remove_exclamation_marks("Oh, no!!!")

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


def remove_last_em(s):
    print(s[:-1])


remove_last_em("Hi!!!!")

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


def remove_word_with_one_em(s):
    result = []
    ss = s.split(" ")
    for i in ss:
        if i.count("!") == 1:
            pass
        else:
            result.append(i)
    print(" ".join(result))


remove_word_with_one_em("Hi! Hi!! Hi!")
remove_word_with_one_em("Hi! Hi!! Hi")
remove_word_with_one_em("Hi! !Hi! Hi")
remove_word_with_one_em("Hi! Hi!")
