from survey import AnonymousSurvey
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)
# 调用类里面的函数时需要用句点法指出实例的名称
language_survey.show_question()
print("Enter 'q' at any time to quit.")

while True:
    response = input("Language:")
    if response == 'q':
        break
    else:
        language_survey.store_response(response.title())

print("Thank you to everyone who participated in the survey!")
language_survey.show_results()