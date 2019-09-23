

response = input("What is your question?:")
def ask_question():
    return response


import random
def add_questions(response):
    answer=["It is certain","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good","Very doubtful."]
    result=random.choice(answer)
    print(result)
    return result




def check_questions(response):
    suffix="?"
    ending=response.endswith(suffix)
    if ending == True:
        add_questions(response)
    else:
        print("“I’m sorry, I can only answer questions.")
    return ending


check_questions(response)
