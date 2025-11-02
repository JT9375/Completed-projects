
#the base class which all family members will be created from
class FamilyMember:
    def __init__(self, living, firstname, lastname, birthday, age, ethnicity, gender, father, mother, grandparents, spouse, age_at_death):
        self.living = living
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.age = age
        self.ethnicity = ethnicity
        self.gender = gender
        self.father = father
        self.mother = mother
        self.grandparents = grandparents
        self.spouse = spouse
        self.age_at_death = age_at_death

    #Getters
    def get_living(self):
        return self.living
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_birthday(self):
        return self.birthday
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_ethnicity(self):
        return self.ethnicity
    def get_father(self):
        return self.father
    def get_mother(self):
        return self.mother
    def get_grandparents(self):
        return self.grandparents
    def get_spouse(self):
        return self.spouse
    def get_age_at_death(self):
        return self.age_at_death


    #setters
    def set_living(self, new_living):
        self.living = new_living
    def set_firstname(self, new_firstname):
        self.firstname = new_firstname
    def set_lastname(self, new_lastname):
        self.lastname = new_lastname
    def set_age(self, new_age):
        self.age = new_age
    def set_gender(self, new_gender):
        self.gender = new_gender
    def set_father(self, new_father):
        self.father = new_father
    def set_mother(self, new_mother):
        self.mother = new_mother
    def set_grandparents(self, new_grandparents):
        self.grandparents.append(new_grandparents)
    def set_spouse(self, new_spouse):
        self.spouse = new_spouse
    def set_age_of_death(self, new_age_of_death):
        self.age_at_death = new_age_of_death

    #methods
    def find_parents(self):
        #TESTED
        #f1a.i
        """returns a combined list of both parents"""
        list_of_parents = []
        mother = self.mother
        mother = mother.lower()
        father = self.father
        father = father.lower()
        #checks if both parents are known
        if mother == "unknown":
            mother = "No known mother"
        if father == "unknown":
            father = "No known father"
        #adds both parents to a list
        list_of_parents.append(mother)
        list_of_parents.append(father)
        #returns the list
        return list_of_parents

#subclass for any object which is a biological parent in the family tree
class Parent(FamilyMember):
    def __init__(self, living, firstname, lastname, birthday, age, ethnicity, gender, father, mother, grandparents, spouse, age_at_death,  children):
        super().__init__(living, firstname, lastname, birthday, age, ethnicity, gender, father, mother, grandparents, spouse, age_at_death)
        self.living = living
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.age = age
        self.ethnicity = ethnicity
        self.gender = gender
        self.father = father
        self.mother = mother
        self.grandparents = grandparents
        self.spouse = spouse
        self.age_at_death = age_at_death
        self.children = children

    #getters
    def get_children(self):
        return self.children

    #setters
    def set_children(self, new_children):
        self.children.append(new_children)

def immediate_family(firstname, lastname):
    #TESTED
    #f1b.i
    """Takes a selected person and returns all of their immediate family"""
    list_of_family = []
    got_siblings = True
    selected_person = find_person(firstname, lastname)
    parents = selected_person.find_parents()
    #checks for a known mother
    if parents[0] != "No known mother":
        list_of_family.append([parents[0]])
    #checks for a known father
    if parents[1] != "No known father":
        list_of_family.append([parents[1]])
    #checks for known children
    if type(selected_person).__name__ == "Parent":
        children = selected_person.get_children()
        list_of_family.append(children)
    siblings = find_siblings(firstname, lastname)
    #checks for known siblings
    if siblings == ['Unable to find siblings'] or siblings == ['This Person is an only child or has no known siblings.']:
        got_siblings = False
    if got_siblings == True:
        list_of_family.append(siblings)
    spouse = selected_person.get_spouse()
    #checks for spouse
    if spouse != "None":
        list_of_family.append([spouse])
    if list_of_family == []:
        list_of_family = [["This person has no known immediate family."]]
        return list_of_family
    else:
        return list_of_family

def extended_family(firstname, lastname):
    #TESTED
    #f1b.ii
    """Takes an inout from the user and returns their extended family"""
    list_of_ext_family = []
    selected_person = find_person(firstname, lastname)
    cousins = find_cousins(firstname, lastname)
    #Chceks if the person has any cousins from the find_cousins function
    if cousins != ["This person has no known cousins"]:
        #adds cousins to the list of extended family
        list_of_ext_family.append([cousins])
    mother = selected_person.get_mother()
    if mother != "Unknown":
        mother = mother.split()
        mother_firstname = mother[0]
        mother_lastname = mother[1]
        #finds the persons antis and uncles from the mothers side of the family
        sibling_of_mother = find_siblings(firstname=mother_firstname, lastname=mother_lastname)
        if sibling_of_mother != ["Unable to find siblings"]:
            #adds them to the extended family list if they exist
            list_of_ext_family.append([sibling_of_mother])
    father = selected_person.get_father()
    if father != "Unknown":
        father = father.split()
        father_firstname = father[0]
        father_lastname = father[1]
        #finds the antis and uncles of the fathers side of the family
        sibling_of_father = find_siblings(firstname=father_firstname, lastname=father_lastname)
        if sibling_of_father != ["Unable to find siblings"]:
            #adds them to the extended family list if they exist
            list_of_ext_family.append([sibling_of_father])
    #adds their immediate family to the list
    list_of_ext_family.append(immediate_family(firstname, lastname))
    #returns the list
    return flatten_list(list_of_ext_family)

def find_siblings(firstname, lastname):
    #TESTED
    #f2a.i
    """takes a person from the user and returns all of their siblings"""
    list_of_siblings = []
    #take a person as an input
    name_of_person = (firstname + " " + lastname).lower()
    selected_person = find_person(firstname, lastname)
    #finds the selected persons parents and turns them to variable names
    parents = selected_person.find_parents()
    mother = parents[0].replace(" ", "_").lower()
    father = parents[1].replace(" ", "_").lower()
    #checks if the parent is a known member of the tree
    if mother == "no_known_mother" or father == "No_known_father":
        list_of_siblings = ["Unable to find siblings"]
        return list_of_siblings
    else:
        mother = to_variable(mother)
        father = to_variable(father)
        #get the list of children belonging to both parents
        children_of_father = father.get_children()
        children_of_mother = mother.get_children()
        #remove step siblings
        for x in range(len(children_of_father)):
            for y in range(len(children_of_mother)):
                if children_of_father[x] == children_of_mother[y]:
                    #create a new list of siblings
                    list_of_siblings.append(children_of_father[x].lower())
        #remove the searched person from the list
        list_of_siblings.remove(name_of_person)
        #return list of children unless empty
        if list_of_siblings == []:
            list_of_siblings = ["This Person is an only child or has no known siblings."]
            return list_of_siblings
        else:
            return list_of_siblings

def find_grandchildren(firstname, lastname):
    # TESTED
    # f1a.ii
    """Takes a selected person and returns their grandchildren if they have any"""
    list_of_grandchildren = []
    selected_person = find_person(firstname, lastname)
    #checks if the selected person has any children
    if type(selected_person).__name__ == "FamilyMember":
        list_of_grandchildren = [["This person has no Grandchildren"]]
        return list_of_grandchildren
    else:
        children = selected_person.get_children()
        #turns each of the selected persons children into variable names
        for x in range(len(children)):
            child = children[x]
            child = child.replace(" ", "_").lower()
            child = to_variable(child)
            #checks if each of the children of the selected person have children and appends them to the list of grandchildren
            if type(child).__name__ == "Parent":
                grandchildren = child.get_children()
                list_of_grandchildren.append(grandchildren)
        #returns the list of grandchildren
        if list_of_grandchildren == []:
            list_of_grandchildren = ["This person has no Grandchildren"]
            return list_of_grandchildren
        else:
            return list_of_grandchildren

def find_cousins(firstname, lastname):
    #TESTED
    #f2a.ii
    """takes an input from the user and returns their cousins"""
    cousins = []
    selected_person = find_person(firstname, lastname)
    #finds the siblings of the person's mother
    mother = selected_person.get_mother()
    if mother != "Unknown":
        mother = mother.split()
        mother_firstname = mother[0]
        mother_lastname = mother[1]
        sibling_of_mother = find_siblings(firstname = mother_firstname, lastname = mother_lastname)
        #adds children of mother's siblings to the list of cousins
        if sibling_of_mother != "unable_to_find_siblings":
            for x in range(len(sibling_of_mother)):
                sibling = sibling_of_mother[x]
                sibling = sibling.replace(" ", "_").lower()
                sibling = to_variable(sibling)
                #checks if the sibling has any children
                if type(sibling).__name__ == "Parent":
                    #adds the children to a list of cousins
                    cousins.append(sibling.get_children())
    #finds the siblings of the person's father
    father = selected_person.get_father()
    if father != "Unknown":
        father = father.split()
        father_firstname = father[0]
        father_lastname = father[1]
        sibling_of_father = find_siblings(firstname = father_firstname, lastname = father_lastname)
        #adds children of father's siblings to the list of cousins
        if sibling_of_father != "unable_to_find_siblings":
            for x in range(len(sibling_of_father)):
                sibling = sibling_of_father[x]
                sibling = sibling.replace(" ", "_").lower()
                sibling = to_variable(sibling)
                #Checks if the sibling has any children
                if type(sibling).__name__ == "Parent":
                    #adds the children to a list of cousins
                    cousins.append(sibling.get_children())
        #Checks if the list of cousins is empty amd returns the list
    if cousins == []:
        cousins = ["This person has no known cousins"]
        return cousins
    else:
        cousins = flatten_list(cousins)
        return cousins

def find_birthdays(firstname, lastname):
    #TESTED
    #f2b.i
    """Takes a person from the user and finds the birthdays of everyone on the selected person's branches"""
    list_of_birthdays = []
    #uses the find_siblings() function to get a list of the inputted persons siblings
    list_of_siblings = find_siblings(firstname, lastname)
    #checks if the selected person has any siblings
    if list_of_siblings == ["Unable to find siblings"]:
        list_of_birthdays = [["Unable to branch. This person is an only child or has no known siblings."]]
        return  list_of_birthdays
    else:
        for x in range(len(list_of_siblings)):
            #goes through the list of siblings one by one to get their children
            sibling = to_variable(list_of_siblings[x].replace(" ", "_").lower())
            #adds a sibling's name along with their DOB to the list of birthdays
            list_of_birthdays.append([sibling.get_firstname()+ " " +sibling.get_lastname()+ ": " +sibling.get_birthday()])
            #checks if the sibling is a parent
            if type(sibling).__name__ == "Parent":
                #get a list of the sibling's children
                list_of_children = sibling.get_children()
                for y in range(len(list_of_children)):
                    child = to_variable(list_of_children[y].replace(" ", "_").lower())
                    #adds each child's name and DOB to the list of birthdays
                    list_of_birthdays.append([child.get_firstname()+ " " +child.get_lastname()+ ": " +child.get_birthday()])
        #returns the list of birthdays
        return list_of_birthdays

def birthdays_in_common(firstname, lastname):
    #TESTED
    #f2b.ii
    """Takes an input from the user and returns the birthdays of everyone in their branch in an ordered calendar"""
    month_converter = [["1", "January"], ["2", "February"], ["3", "March"], ["4", "April"], ["5", "May"], ["6", "June"], ["7", "July"], ["8", "August"],
                       ["9", "September"], ["10", "October"], ["11", "November"], ["12", "December"]]
    list_to_sort = []
    to_delete = []
    #get the birthdays of a branch
    list_of_birthdays = find_birthdays(firstname, lastname)
    if list_of_birthdays == [['Unable to branch. This person is an only child or has no known siblings.']]:
        list_of_birthdays = ["Unable to create the calendar. It is not possible to create a branch off this person."]
        return list_of_birthdays
    else:
        #split the birthdays into day, month and year
        for x in range(len(list_of_birthdays)):
            one_value = list_of_birthdays[x]
            one_value = one_value[0].split(":")
            list_to_sort.append(one_value)
            birthday = list_to_sort[x][1].split(".")
            day = int(birthday[0])
            month = int(birthday[1])
            list_to_sort[x][1] = day
            list_to_sort[x].append(month)
        for x in range(len(list_to_sort)):
            for y in range(len(list_to_sort) - 1):
                # sort birthdays by day
                if list_to_sort[y][1] > list_to_sort[y + 1][1]:
                    temp = list_to_sort[y]
                    list_to_sort[y] = list_to_sort[y+1]
                    list_to_sort[y + 1] = temp
                #sort birthdays by month
                if list_to_sort[y][2] > list_to_sort[y + 1][2]:
                    temp = list_to_sort[y]
                    list_to_sort[y] = list_to_sort[y+1]
                    list_to_sort[y + 1] = temp
        #chacks for matching birthdays
        for x in range(len(list_to_sort)):
            for y in range(len(list_to_sort)):
            #combines people with matching birthdays into the same position
                if list_to_sort[x][1] == list_to_sort[y][1] and list_to_sort[x][2] == list_to_sort[y][2] and list_to_sort[x] != list_to_sort[y]:
                    list_to_sort[x][0] = list_to_sort[x][0] + " and " + list_to_sort[y][0]
                    list_to_sort[y] = list_to_sort[x]
                    #add the position of irreverent data to a new list to be deleted
                    to_delete.append(y)
        #remove the data in list_to_sort using the indexes stored in to_delete
        for x in range(len(to_delete)):
            delete = to_delete[x]
            del list_to_sort[delete]
        #combine the data in multiple positions into one to be returned
        for x in range(len(list_to_sort)):
            list_to_sort[x][1] = str(list_to_sort[x][1])
            list_to_sort[x][2] = str(list_to_sort[x][2])
            for y in range(len(month_converter)):
                if list_to_sort[x][2] == month_converter[y][0]:
                    list_to_sort[x][2] = month_converter[y][1]
            list_to_sort[x][1] = list_to_sort[x][1]+ " " + list_to_sort[x][2]
            del list_to_sort[x][2]
            list_to_sort[x][0] = list_to_sort[x][0]+ " was/were born on: " + list_to_sort[x][1]
            del list_to_sort[x][1]
        #flatten and return the list
        list_to_sort = flatten_list(list_to_sort)
        return list_to_sort

def average_age_at_death():
    #TESTED
    #f3a.iii
    """Checks everyone in the family tree to see if they're deceased and returns the average age of which they all died"""
    sum_of_ages = 0
    num_of_dead = 0
    for x in range(len(list_of_tree)):
        #turn each person in the list into a variable
        person = to_variable(list_of_tree[x])
        #check if they're dead
        if person.get_living() == False:
            #add their age at death to the sum_of_ages
            sum_of_ages += person.get_age_at_death()
            #increment the num_of_dead counter
            num_of_dead += 1
    #return the average
    return "the average age at death for this family is: " + str(sum_of_ages/num_of_dead)

def number_of_children():
    #TESETD
    #f3b.i
    """Returns a list of every person in the family tree who is a parent along with their children """
    list_of_children = []
    for x in range(len(list_of_tree)):
        #turn each person into a variable
        person = list_of_tree[x]
        person_variable = to_variable(person)
        #check if the person is a variable
        if type(person_variable).__name__ == "Parent":
            #combines the parent and number of children into a list to be flattened
            if len(person_variable.get_children()) == 1:
                list_of_children.append([person+" has:", len(person_variable.get_children()), "child"])
            else:
                list_of_children.append([person+" has:", len(person_variable.get_children()), "children"])
    #return the list
    return list_of_children

def average_number_of_children():
    #TESTED
    #f3b.ii
    """Take the list: number_of_children and calculated the average number of children per family member in the tree"""
    list_of_children = number_of_children()
    sum_of_children = 0
    for x in range(len(list_of_children)):
        #add the number of children together
        sum_of_children += list_of_children[x][1]
    #halfes the number of children to take into consideration each child has one mother and one father, doubling the amount of children in the list of children
    sum_of_children /= 2
    #calculate the average
    average = len(list_of_tree)/sum_of_children
    #return the average
    return "the average number of children in the family tree is: "+ str(average) +" children per person"

def find_person(firstname, lastname):
    #TESTED
    """takes an input and turns it into the formating of all the objects created by our classes for family members while also checking if the searched person is part of the family tree"""
    firstname = firstname.lower()
    lastname = lastname.lower()
    fullname = (firstname+"_"+lastname)
    #ensures the name of the person entered is within the family tree
    in_list = fullname in list_of_tree
    while in_list != True:
        print("This person is not in the family tree")
        print("please enter a different name")
        firstname = input("Enter the firstname of the person you are searching for:")
        firstname = firstname.lower()
        lastname = input("Enter the lastname of the person you are searching for:")
        lastname = lastname.lower()
        fullname = (firstname + "_" + lastname)
        in_list = fullname in list_of_tree
    return to_variable(fullname)

def to_variable(fullname):
    """Takes the string of a family member part of the tree and uses a dictionary to turn the name into a variable"""
    #TESTED
    object_name = {}
    if fullname == "otto_emmersohn":
        object_name["object_name"] = otto_emmersohn
    elif fullname == "rob_emmersohn":
        object_name["object_name"] = rob_emmersohn
    elif fullname == "anna_emmersohn":
        object_name["object_name"] = anna_emmersohn
    elif fullname == "leon_emmersohn":
        object_name["object_name"] = leon_emmersohn
    elif fullname == "ava_emmersohn":
        object_name["object_name"] = ava_emmersohn
    elif fullname == "alejandro_emmersohn":
        object_name["object_name"] = alejandro_emmersohn
    elif fullname == "mia_emmersohn":
        object_name["object_name"] = mia_emmersohn
    elif fullname == "alice_nowak":
        object_name["object_name"] = alice_nowak
    elif fullname == "armand_nowak":
        object_name["object_name"] = armand_nowak
    elif fullname == "isabelle_nowak":
        object_name["object_name"] = isabelle_nowak
    elif fullname == "jayce_emmersohn":
        object_name["object_name"] = jayce_emmersohn
    elif fullname == "viola_emmersohn":
        object_name["object_name"] = viola_emmersohn
    elif fullname == "cornelia_emmersohn":
        object_name["object_name"] = cornelia_emmersohn
    elif fullname == "tahar_kumar":
        object_name["object_name"] = tahar_kumar
    elif fullname == "shreya_kumar":
        object_name["object_name"] = shreya_kumar
    elif fullname == "maya_hassan":
        object_name["object_name"] = maya_hassan
    elif fullname == "abdul_hassan":
        object_name["object_name"] = abdul_hassan
    elif fullname == "tania_hassan":
        object_name["object_name"] = tania_hassan
    elif fullname == "sadia_hassan":
        object_name["object_name"] = sadia_hassan
    elif fullname == "zahir_kumar":
        object_name["object_name"] = zahir_kumar
    elif fullname == "amir_kumar":
        object_name["object_name"] = amir_kumar
    else:
        object_name["object_name"] = niya_kumar
    return object_name["object_name"]

def flatten_list(list_to_flatten):
    """flattens a multi-dimensional list into a 1-dimensional list of data"""
    flat_list = []
    for x in list_to_flatten:
        for y in x:
            flat_list.append(y)
    return flat_list

def menu():
    """A centralised way to decide what functions you wish to execute"""
    print("Welcome to the family tree! Please enter the corresponding number for the function you wish to execute")
    print("1: Find a family member's parents (f1a.i)")
    print("2: Find a family member's grandchildren (f1a.ii)")
    print("3: Find a family member's immediate family (f1b.i)")
    print("4: Find a family member's extended family (f1b.ii)")
    print("5: Find a family member's siblings (f2a.i)")
    print("6: Find a family member's cousins (f2a.ii)")
    print("7: find the birthdays of a family member's branch (f2b.i)")
    print("8: find the ordered list of birthdays of a family member's branch (f2b.ii)")
    print("9: find the average age of death of family members in the tree (f3a.iii)")
    print("10: find the number of children each family member has (f3b.i)")
    print("11: find the average number of children per person in the tree (f3b.ii)")
    print("OR enter 'END' to exit")
    print("Alternatively, enter 'TREE' to display the list of everyone in the family tree")
    available_choices = ["TREE", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    choice = input("Please enter your input here: ")

    while choice != "END":
        while choice not in available_choices:
            choice = input("Invalid input. Please enter a number from 1-11 or 'TREE' to see a list of family members: ")

        if choice == "TREE":
            print(", ".join(list_of_tree))

        elif choice == "1":
            person = find_person(input("Enter the firstname you wish to find the parents off:"), input("Enter the lastname of the person you wish to find the parents of:"))
            print("This person's parents are: ")
            print(", ".join(person.find_parents()))

        elif choice == "2":
            grandchildren = find_grandchildren(input("Enter the firstname of the person you wish to find the grandchildren of:"), input("Enter the lastname of the person you wish to find the grandchildren of:"))
            grandchildren = flatten_list(grandchildren)
            print("This person's grandchildren is:")
            print(", ".join(grandchildren))

        elif choice == "3":
            family = immediate_family(input("Enter the firstname of the person you wish to find the immediate family of:"), input("Enter the lastname of the person you wish to find the immediate family of:"))
            family = flatten_list(family)
            print("the immediate family o this person are:")
            print(", ".join(family))

        elif choice == "4":
            ext_family = extended_family(input("Enter the firstname of the person you wish to find the extended family of:"), input("Enter the lastname of the person you wish to find the extended family of:"))
            ext_family = flatten_list(ext_family)
            print("the immediate family of this person are:")
            print(", ".join(ext_family))

        elif choice == "5":
            siblings = find_siblings(input("Enter the firstname of the person you wish to find the siblings of:"), input("Enter the lastname of the person you wish to find the siblings of:"))
            print("the siblings of this person are:")
            print(", ".join(siblings))

        elif choice == "6":
            cousins = find_cousins(input("Enter the firstname of the person you wish to find the cousins of:"), input("Enter the lastname of the person you wish to find the cousins of:"))
            print("the cousins of this person are:")
            print(", ".join(cousins))

        elif choice == "7":
            birthdays = flatten_list(find_birthdays(input("Enter the firstname of the person you wish to find the list of birthdays for their branches"), input("Enter the lastname of the person you wish to find the list of birthdays for their branches")))
            print("The birthdays of this branch are:")
            print(", ".join(birthdays))

        elif choice == "8":
            calendar =  birthdays_in_common(input("enter the firstname of the person you wish to find the calendar of birthdays for their branches"), input("enter the lastname of the person you wish to find the calendar of birthdays for their branches"))
            print("The calendar for this branch is:")
            print(", ".join(calendar))

        elif choice == "9":
            print(average_age_at_death())

        elif choice == "10":
            list_of_children = number_of_children()
            for x in range(len(list_of_children)):
                list_of_children[x] = [list_of_children[x][0]+" "+str(list_of_children[x][1])+" "+list_of_children[x][2]]
            list_of_children = flatten_list(list_of_children)
            print("the list of parents and their children is:")
            print(", ".join(list_of_children))

        elif choice == "11":
            print(average_number_of_children())

        choice = input("please neter a new input or 'END' to exit: ")

    print("EXITING FAMILY TREE")
    exit()

#All the members of the tree as classes
otto_emmersohn = Parent(True, "Otto", "Emmersohn", "17.6.1991", "39", "Swedish", "Male", "Rob Emmersohn", "Anna Emmersohn",[], "Cornelia Emmersohn", 0, ["Jayce Emmersohn", "Viola Emmersohn"])
rob_emmersohn = Parent(False, "Rob", "Emmersohn", "4.12.1951", "72", "Swedish", "Male", "Unknown", "Unknown",[], "Anna Emmersohn",68, ["Otto Emmersohn", "Leon Emmersohn", "Alice Nowak"])
anna_emmersohn = Parent(True, "Anna", "Emmersohn", "8.7.1953", "71", "Swedish", "Female", "Unknown", "Unknown",[], "Rob Emmersohn", 0,["Otto Emmersohn", "Leon Emmersohn", "Alice Nowak"])
leon_emmersohn = Parent(True, "Leon", "Emmersohn", "17.6.1990", "34", "Swedish", "Male", "Rob Emmersohn", "Anna Emmersohn",[], "Ava Emmersohn",0, ["Mia Emmersohn", "Alejandro Emmersohn"])
ava_emmersohn = Parent(True, "Ava", "Emmersohn", "25.8.1994", "30", "Spanish", "Female", "Unknown", "Unknown",[], "Leon Emmersohn", 0,["Mia Emmersohn", "Alejandro Emmersohn"])
alejandro_emmersohn = FamilyMember(True, "Alejandro", "Emmersohn", "12.11.2019", "5", "Swedish/Spanish", "Male", "Leon Emmersohn", "Anna Emmersohn",[], "None", 0)
mia_emmersohn = FamilyMember(True, "Mia", "Emmersohn", "14.8.2022", "2", "Swedish/Spanish", "Female", "Leon Emmersohn", "Ava Emmersohn",[], "None", 0)
alice_nowak = Parent(True, "Alice", "Nowak", "17.6.1990", "34", "Swedish", "Female", "Otto Emmersohn", "Anna Emmersohn",[], "Armand Nowak", 0, ["Isabelle Nowak"])
armand_nowak = Parent(True, "Armand", "Nowak", "22.10.1992", "32", "Polish", "Male", "Unknown", "Unknown",[], "Alice Nowak", 0, ["Isabelle Nowak"])
isabelle_nowak = FamilyMember(True, "Isabelle", "Nowak", "5.4.2016", "8", "Polish/Swedish", "Female", "Armand Nowak", "Alice Nowak",["Rob Emmersohn", "Anna Emmersohn"], "None", 0)
jayce_emmersohn = FamilyMember(True, "Jayce", "Emmersohn", "17.6.15", "9", "Swedish", "Male", "Otto Emmersohn", "Cornelia Emmersohn",["Rob Emmersohn", "Anna Emmersohn"], "None", 0)
viola_emmersohn = FamilyMember(True, "Viola", "Emmersohn", "3.12.2021", "11", "Swedish", "Female", "Otto Emmersohn", "Cornelia Emmersohn",["Rob Emmersohn", "Anna Emmersohn"], "None", 0)
cornelia_emmersohn = Parent(True, "Cornelia", "Emmersohn", "27.11.1985", "38", "Indian", "Female", "Tahar Kumar", "Shreya Kumar", [], "Otto Emmersohn", 0, ["Jayce Emmersohn", "Viola Emmersohn"])
tahar_kumar = Parent(True, "Tahar", "Kumar", "19.4.1955", "69", "Indian", "Male", "Unknown", "Unknown", [], "Shreya Kumar", 0, ["Cornelia Emmersohn", "Maya Hassan", "Zahir Kumar", "Amir Kumar"])
shreya_kumar = Parent(False, "Shreya", "Kumar", "24.3.1960", "64", "Indian", "Female", "Unknown", "Unknown", ["Tahar"], "Tahar Kumar", 64, ["Cornelia Emmersohn", "Maya Hassan", "Zahir Kumar", "Amir Kumar"])
maya_hassan = Parent(True, "Maya", "Hassan", "29.5.1984", "40", "Indian", "Female", "Tahar Kumar", "Shreya Kumar", [], "Abdul Hassan", 0, ["Tania Hassan", "Sadia Hassan"])
abdul_hassan = Parent(True, "Abdul", "Hassan", "8.9.1981", "43", "Sri Lankan", "Male", "Unknown", "Unknown", [], "Maya Hassan", 0, ["Tania Hassan", "Sadia Hassan"])
tania_hassan = FamilyMember(True, "Tania", "Hassan", "1.2.2006", "18", "Indian/Sri Lankan", "Female", "Abdul Hassan", "Maya Hassan", ["Shreya Kumar", "Tahar Kumar"], "None", 0)
sadia_hassan = FamilyMember(True, "Sadia", "Hassan", "30.10.2004.", "20", "Indian/Sri Lankan", "Female", "Abdul Hassan", "Maya Hassan", ["Shreya Kumar", "Tahar Kumar"], "None", 0)
zahir_kumar = FamilyMember(False, "Zahir", "Kumar", "1.4.1991", "33", "Indian", "Male", "Tahar Kumar", "Shreya Kumar", [], "None", 18)
amir_kumar = FamilyMember(True, "Amir", "Kumar", "6.8.1989", "35", "Indian", "Male", "Tahar Kumar", "Shreya Kumar", [], "Niya Kumar", 0)
niya_kumar =  FamilyMember(True, "Niya", "Kumar", "27.12.1988", "35", "Nepalese", "Female", "Unknown", "Unknown", [], "Amir Kumar", 0)

#list of all members in the family tree
list_of_tree = ["otto_emmersohn", "rob_emmersohn", "anna_emmersohn", "leon_emmersohn", "ava_emmersohn", "alejandro_emmersohn", "mia_emmersohn", "alice_nowak",
                    "armand_nowak", "isabelle_nowak", "jayce_emmersohn", "viola_emmersohn", "cornelia_emmersohn", "tahar_kumar", "shreya_kumar", "maya_hassan",
                    "abdul_hassan", "tania_hassan", "sadia_hassan", "zahir_kumar", "amir_kumar", "niya_kumar"]

#enter the User interface
menu()
