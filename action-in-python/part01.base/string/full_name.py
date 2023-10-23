
if __name__ == '__main__':
    first_name = "ada"
    last_name = "lovelace"

    # 这种字符串名为f字符串 。f是format（设置格式）的简写，因为Python通过把花括号内的变量替换为其值来设置字符串的格式。
    full_name = f"{first_name} {last_name}"
    # ada lovelace
    print(full_name)
    # Hello, Ada Lovelace!
    print(f"Hello, {full_name.title()}!")

    # 注意：f字符串是Python 3.6引入的。如果你使用的是Python 3.5或更早的版本，需要使用format() 方法，而非这种f语法。
    # 要使用方法format() ，可在圆括号内列出要在字符串中使用的变量。对于每个变量，都通过一对花括号来引用。
    # 这样将按顺序将这些花括号替换为圆括号内列出的变量的值
    full_name_2 = "{} {}".format(first_name, last_name)
    # ada lovelace
    print(full_name_2)

    # 换行和制表符
    print("language: \n\ttC\n\tJava\n\tPython\n\tGolang")

    # 删除空白
    trim = "  Python  "
    # 删除左边的空白
    print(trim.lstrip())
    # 删除右边的空白
    print(trim.rstrip())
    # 删除左右的空白
    print(trim.strip())

    # 重复字符，打印：不允许吃饭！不允许吃饭！不允许吃饭！
    print('不允许吃饭！' * 3)
