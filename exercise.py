"""2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively"""
# The basic functionality of the codes are here
# The next step is to add some exception handle (Done)

# your code starts here:
def answer_quiz(quiz):
   # add try and except clause
    try:
        usr_ans = int(input('Answer the following quiz...\n' + quiz))
    except ValueError:
        print('The input is not an integer!')
        usr_ans = int(input('Please try again the following quiz...\n' + quiz))
    return usr_ans


def judge_answer(quiz_ans, user_ans):
    return int(quiz_ans) == int(user_ans)


# read quizs
quiz_txt = open('questions.txt', 'r')
quizs = [line.strip() for line in quiz_txt]
# for quiz in quizs:
#     print(quiz)
quiz_txt.close()

# ask users for input of answers
results = []
for quiz in quizs:
    quiz_question, quiz_ans = quiz.split(sep='=')
    usr_ans = answer_quiz(quiz_question+'=')
    result = judge_answer(quiz_ans, usr_ans)
    print(result)
    results.append(result)

print(results)
# calculate score and write it to the file
# score = sum(results)/len(results)
result_txt = open('result.txt', 'w')
# result_txt.writelines(f'Your final score is {sum(results)}/{len(results)}')
result_txt.writelines('Your final score is {score}/{num_problem}.'.format(score=sum(results), num_problem=len(results)))
result_txt.close()

