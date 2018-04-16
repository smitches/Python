
#create global constant for student.txt input file 
STUDENT_INPUT = "students.txt"
#create global constant for courses.txt input file 
COURSE_INPUT = "courses.txt"
#create global constant for students updated output file 
STUDENT_OUTPUT = "students-updated.txt"
#create global constant for courses updated output file 
COURSE_OUTPUT = "courses-updated.txt"
#create global constant to add a class 
ADD_COURSE = 1
#create global constant to drop a class 
DROP_COURSE = 2
#create global constant to print student schedule
PRINT_STUDENT_SCHEDULE = 3
#create global constant to print course schedule
PRINT_COURSE_SCHEDULE = 4
#create global constant as a sentinel 
DONE = 5


#import student class file to create objects 
import student
#import course class file to create objects
import course



#define print menu function
def print_menu():
    #print option 1 using global constant
    print(ADD_COURSE, ".", " Add course", sep="")
    #print option 2 using global constant
    print(DROP_COURSE, ".", " Drop course", sep="")
    #print option 3 using global constant
    print(PRINT_STUDENT_SCHEDULE, ".", " Print student schedule", sep='')
    #print option 4 using global constant
    print(PRINT_COURSE_SCHEDULE, ".", " Print course schedule", sep='')
    #print option 5 using global constant
    print(DONE, ".", " Done", sep='')
    print()


#define user_menu_choice function
def user_menu_choice():   
    #prompt the user for their choice using the specified item numbers
    choice = int(input("Please choose a menu option: "))
    #loop to check for data validity: order can not be less than first choice or greater than last choice
    while choice not in range(ADD_COURSE,DONE+1):
        #print error message telling the user to enter a number between first choice and last choice
        print("You have entered an invalid choice, please input a number between ", ADD_COURSE, "and ", DONE, end="\n")
        #reask the user for their order input
        choice = int(input("Please choose a menu option: "))
        #print blank line
        print("\n")
    #return choice to use in main
    return choice


    
def process_students(infile):
    student_dictionary={}
    for line in infile:
        line=line.rstrip('\n')
        line=line.split(':')
        eid=line[0]
        fname=line[1]
        lname=line[2]
        classes=line[3:]
        student_object=student.Student(eid,fname,lname,classes)
        student_dictionary[eid]=student_object
    return student_dictionary



def process_courses(infile):
    course_dictionary={}
    for line in infile:
        line=line.rstrip('\n')
        line=line.split(';')
        unique_num=line[0]
        title=line[1]
        professor=line[2]
        seats_taken=line[3]
        capacity=line[4]
        course_object=course.Course(seats_taken)
        course_object.set_unique(unique_num)
        course_object.set_title(title)
        course_object.set_prof(professor)
        course_object.set_capacity(int(capacity))
        course_dictionary[unique_num]=course_object
    return course_dictionary



def get_eid(student_dict):
    student_eid = input("Please enter a student ID: ")
    while student_eid not in student_dict:
        student_eid = input("Error. Please enter an existing student ID: ")
    return student_eid



def get_unique_number(course_dict):
    unique_number = input("Please enter the unique number: ")
    while unique_number not in course_dict:
        unique_number = input("Error. Please enter an existing unique number: ")
    return unique_number


#print course schedule of all courses and enrollments
def print_course_schedule(course_dict):
    for unique in course_dict:
        print(course_dict[unique])

#print student information, including a list of courses a student is in
def print_student(student_object,student_dict,course_dict):
    print()
    print(student_object)
    print('Courses:')
    for unique in student_object.get_classes():
        class_object=course_dict[unique]
        class_title=class_object.get_title()
        print(unique, class_title)
    
#write updated object information to an output file
def write_to_file(dictionary,outfile):
    for key in dictionary:
        this_object=dictionary[key]
        line=this_object.line_for_file()
        outfile.write(line)
        
def main():
    student_file=open(STUDENT_INPUT,'r')
    course_file=open(COURSE_INPUT,'r')
    student_dict=process_students(student_file)
    course_dict=process_courses(course_file)
    print_menu()
    choice = user_menu_choice()
    while choice != DONE:
        if choice == ADD_COURSE:
            eid=get_eid(student_dict)
            student_object=student_dict[eid]
            unique=get_unique_number(course_dict)
            course_object=course_dict[unique]
            while course_object.space_available()==False:
                print('Error. Course is full. Please pick a new course')
                unique=get_unique_number(course_dict)
                course_object=course_dict[unique]
            while student_object.add_class(unique)==False:
                unique=get_unique_number(course_dict)
                course_object=course_dict[unique]
                while course_object.space_available()==False:
                    print('Error. Course is full. Please pick a new course')
                    unique=get_unique_number(course_dict)
                    course_object=course_dict[unique]
            course_object.enroll_student()
            print('Student',eid,'enrolled in', unique)
            
            
        elif choice == DROP_COURSE:
            eid=get_eid(student_dict)
            student_object=student_dict[eid]
            unique=get_unique_number(course_dict)
            course_object=course_dict[unique]
            while student_object.drop_class(unique)==False:
                unique=get_unique_number(course_dict)
                course_object=course_dict[unique]
            
            course_object.drop_student()
            print('Student',eid,'dropped from', unique)
            
        elif choice == PRINT_STUDENT_SCHEDULE:
            eid = get_eid(student_dict)
            student_object=student_dict[eid]            
            print_student(student_object,student_dict,course_dict)
        
        elif choice == PRINT_COURSE_SCHEDULE:
            print_course_schedule(course_dict)
        
        print()
        print_menu()
        choice = user_menu_choice()

    updated_student_file=open('students-updated.txt','w')
    updated_course_file=open('courses-updated.txt','w')

    write_to_file(student_dict,updated_student_file)
    write_to_file(course_dict,updated_course_file)
    
    
    updated_student_file.close()
    updated_course_file.close()
    student_file.close()
    course_file.close()


#call main
main()
        
