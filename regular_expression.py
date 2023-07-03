# import re
# an_word = "3+5+7*7-5-"
# comp = "joseph@gmail.com"
# # result = re.search("@", comp)
# # result2 = re.findall("monday", an_word)
# # result3 = re.split("(\+|-|\*)", an_word)
# # print(result3)
# # result4 = re.sub("Monday", "Wednesday", code)

# # if result3[-2] in ["+", "-", "/", "*"] :
# #     print("Don't do anything")
# # print(result4)

# # Meta Characters
# # . = find any character that is not a new line character
# # + = one or more characters 
# # * = zero or more characters
# # $ = at the end
# # ^ = at the beginning
# # ? = zero or one
# # result = re.findall(".", code)

# # result = re.findall("^Today.+life$", code)

# # # Special Characters
# # \A = any character at the beginning of a word 
# # \b = any character at the beginning or end of a word 
# # \B = any charceter that is not athe the beginning or end 
# # \d = any digit number 
# # \D = any non digit number
# # \s = any whitespace Character
# # \S = any non white space character 

# # Gruoups :
# # [a-zA-Z0-9]
# # (aa)
# # {2}
# code = """
# This is Cain Telephone 08179776605
# This is Abel Telephone +2348179776605

# """

# # result = re.findall(r"\d", code)
# # result = re.findall(r"[^a-zA-z0-9\s]", code)
# result = re.findall(r"[+234][0-9]{13}", code)
# print(result)

import re 
email = "ban@abaz.skgmail.com"
username = "barsore1994"
phone_number = "+2348179776605"
password = "joshuaJoseph1994#"

email_check = re.findall("@.*\.com", email)
username_check = re.findall("[/SA-Z]", username)
phone_number_check = re.findall("^(\+234)", phone_number)
phone_number_check2 = re.findall("(\+[0-9]{13})", phone_number)
password_check = re.findall("[^/S/dA-Za-z0-9]+", password)
password_check2 = re.findall("[A-Za-z0-9]+", password)
print(len(email_check))
print(len(username_check))
print(len(phone_number_check))
print(len(phone_number_check2))
print(len(password_check))
print(len(password_check2))

if len(email_check) >= 1 and len(username_check) == 0 and len(phone_number_check)  >= 1 and len(phone_number_check2) >= 1 and len(password_check) >= 1 and len(password_check2) >= 1:
    print("Your Details meet our requirement, You ca now login")
else :
    print("check carefully your details is incorrect")
