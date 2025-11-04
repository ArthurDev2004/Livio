# will be used to convert the strings which are recieved from the frontend to the type needed in the backend, so when the is_valid() method is called, it returns true
from genders.models import Gender 
from gradeLevels.models import GradeLevel
from nationalities.models import Nationality

# will receive the data from the post request to create a profile, and will convert the strings which are passed in to the proper type, so that when is_valid is called, it is properly validated and saved 
def convert(post_data):

    new_data = dict() # create a new dictionary since dictionary in python is mutable 

    new_data['firstName'] = post_data['firstName']
    new_data['lastName'] = post_data['lastName']
    new_data['age'] = post_data['age']
    new_data['bio'] = post_data['bio']

    gender = Gender.objects.get(name=post_data['gender'])
    gradeLevel = GradeLevel.objects.get(name=post_data['gradeLevel'])
    nationality = Nationality.objects.get(name=post_data['nationality'])

    new_data['gender'] = gender
    new_data['gradeLevel'] = gradeLevel
    new_data['nationality'] = nationality

    return new_data # will return it, and this will be used for the validation now 

# will receive the data from the post request to create a profile, and will convert the strings which are passed in to the proper type, so that when is_valid is called, it is properly validated and saved 
def convert2(post_data):

    new_data = dict() # create a new dictionary since dictionary in python is mutable 

    new_data['firstName'] = post_data['firstName']
    new_data['lastName'] = post_data['lastName']
    new_data['age'] = post_data['age']
    new_data['bio'] = post_data['bio']

    # get the proper objects for foreign key to make it work for the serializer
    gender = Gender.objects.get(name=post_data['gender']).id
    gradeLevel = GradeLevel.objects.get(name=post_data['gradeLevel']).id
    nationality = Nationality.objects.get(name=post_data['nationality']).id

    new_data['gender'] = gender
    new_data['gradeLevel'] = gradeLevel
    new_data['nationality'] = nationality

    return new_data # will return it, and this will be used for the validation now 