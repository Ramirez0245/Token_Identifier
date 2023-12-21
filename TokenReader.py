"""
About: A program to read one token at a
time from the given text file and determine whether the token is
i. A number
ii. An identifier (must start with underscore or a letter, followed by
more letters, more digits, or more underscores
iii. A reserved word. List of reserved words: string reserved[5]={“while”, “for”, “switch”, “do”,
“return” };

Sample output for #1
Token   number  identifier  reserved word
K-mart  no      no          no
23andMe no      no          no
456     yes     no          no

Sample output for #2
Token                           number                  identifier              reserved word
Hello!                          no                      no                      no
Welcome                         no                      yes                     no
to                              no                      yes                     no
tokenfile.txt                   no                      no                      no
while                           no                      no                      yes
for                             no                      no                      yes
switch                          no                      no                      yes
do                              no                      no                      yes
return                          no                      no                      yes
This                            no                      yes                     no
file                            no                      yes                     no
is                              no                      yes                     no
for                             no                      no                      yes
tes4516___385ting               no                      yes                     no
purposes.                       no                      no                      no
Good                            no                      yes                     no
Luck!                           no                      no                      no
56479                           yes                     no                      no
K-mart                          no                      no                      no
23andMe                         no                      no                      no
...........
"""

def parsefile():
    tokenfile = open("tokenfile.txt", "r")
    file_string_container = tokenfile.read()
    file_list_container = file_string_container.splitlines()
    reformat_string_container = ""

    for lines in file_list_container:
        reformat_string_container += lines + " "

    reformat_list_container = reformat_string_container.split(" ")
    reformat_list_container.pop(len(reformat_list_container) - 1)

    return reformat_list_container

def token_results(word_container_list):
    result_list = []
    
    for word in word_container_list:
        if word.isnumeric():
            input_format = token_result(word, "yes", "no", "no")
            result_list.append(input_format)
            continue

        match word:
            case "while":
                input_format = token_result(word, "no", "no", "yes")
                result_list.append(input_format)
                continue
            case "for":
                input_format = token_result(word, "no", "no", "yes")
                result_list.append(input_format)
                continue
            case "switch":
                input_format = token_result(word, "no", "no", "yes")
                result_list.append(input_format)
                continue
            case "do":
                input_format = token_result(word, "no", "no", "yes")
                result_list.append(input_format)
                continue
            case "return":
                input_format = token_result(word, "no", "no", "yes")
                result_list.append(input_format)
                continue

        if word[0] == "_" or word[0].isalpha():
            remain_result = word.replace(word[0], "", 1)
            is_not_identifier = False

            for letter in remain_result:
                if not letter.isalpha() and not letter.isnumeric() and not letter == "_":
                    input_format = token_result(word, "no", "no", "no")
                    result_list.append(input_format)
                    is_not_identifier = True
                    break

            if is_not_identifier:
                continue             
            input_format = token_result(word, "no", "yes", "no")
            result_list.append(input_format)
            continue

        input_format = token_result(word, "no", "no", "no")
        result_list.append(input_format)

    return result_list
        
def token_result(word, number, identifier, reserved):
    token_result = {
        "token": word,
        "number": number,
        "identifier": identifier,
        "reserved": reserved
    }
    return token_result

def main():
    list_container = parsefile()
    token_results_list = token_results(list_container)
    print("Token \t\t\t\tnumber\t\t\tidentifier\t\t\treserved word")
    for results in token_results_list:
        if "." in results["token"]:
            print(results["token"] + "\t\t\t" + results["number"] + "\t\t\t" + results["identifier"] + "\t\t\t" + results["reserved"])
            continue
        print(results["token"] + "\t\t\t\t" + results["number"] + "\t\t\t" + results["identifier"] + "\t\t\t" + results["reserved"])
    print(list_container)
    print(type(list_container[len(list_container) - 1]))


if __name__ == "__main__":
    main()