import requests
import re



if __name__ == '__main__':

# match 方法是从字符串的开头就匹配才能返回结果
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
    print(result)
    print(result.group())
    print(result.span())

# search 方法，是在一段文本中，提取出第一个符合正则表达式要求的内容

# findall 方法，在一段文本中，提取出所有符合正则表达式要求的内容
