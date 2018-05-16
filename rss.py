import json


def load_rs_setup():
    with open('rs_setup.json') as data_file:
        data = json.load(data_file)
        cafeteria_tables = data["cafeteria_tables"]
        return cafeteria_tables


cafeteria_tables = load_rs_setup()
print ("Hi, this is a cafeteria reservation program!")
print ("This cafeteria works from 9:00 to 18:00.")
print ("We have 5 tables with different capacities, which you can order for round number of hours.")


def main(cafeteria_tables):
    order_state = raw_input("Enter 1 If you want to order a table,\nEnter 2 to delete reservations,\nEnter anything else to exit")
    if order_state == "1":
        while True:
            reserver_name = raw_input("What is your name?")
            starting_hour = int(input ("Write your reservation hour ( Example` 13, which is 13:00 ) -> ")) - 9
            num_of_hours = int(input ("For how many hours do you want to reserve the table ?"))
            num_of_people = int(input ("Please enter guests number"))
            if num_of_people > 6 or num_of_people < 1:
                print ("We don't have tables with capacity of " + str(num_of_people))
                print "please select 1 or 2"
                main(cafeteria_tables)
            if starting_hour < 0 or num_of_hours < 1 or (starting_hour + num_of_hours) > 8:
                print ("The order you want to make is out of our working hours")
                print "please select 1 or 2"
                main(cafeteria_tables)
            ordered_table_num = 0
            for index in range(0,5):
                order_hours_acceptable = 1
                for ii in range(0, num_of_hours):
                    if cafeteria_tables[index]["hours"][ii]:
                        order_hours_acceptable = 0
                if order_hours_acceptable == 1 and num_of_people <= cafeteria_tables[index]["number_of_customers"]:
                    ordered_table_num = index+1
                    for ii in range(starting_hour,num_of_hours+starting_hour):
                        cafeteria_tables[index]["hours"][ii] = 1
                        cafeteria_tables[index]["names"]["reserver" + str(starting_hour)] = reserver_name


                    data_json = {"cafeteria_tables" : cafeteria_tables}
                    file = open("rs_setup.json", "w")
                    file.write(json.dumps(data_json))
                    file.close()
                    break
            if ordered_table_num == 0:
                print ("Sorry we don't have tables at that time with that capacity.")
                print "please select 1, 2 or 3"
                main(cafeteria_tables)
            else:
                print ("You have reserved table number " + str(ordered_table_num))
                print "please select 1, 2 or 3"
                main(cafeteria_tables)
    elif order_state == "2":
        new_file = {"cafeteria_tables": [{"hours": [0, 0, 0, 0, 0, 0, 0, 0], "number_of_customers": 3,
                               "names": {}},
                              {"hours": [0, 0, 0, 0, 0, 0, 0, 0], "number_of_customers": 5,
                               "names": {}},
                              {"hours": [0, 0, 0, 0, 0, 0, 0, 0], "number_of_customers": 6,
                               "names": {}},
                              {"hours": [0, 0, 0, 0, 0, 0, 0, 0], "number_of_customers": 3,
                               "names": {}},
                              {"hours": [0, 0, 0, 0, 0, 0, 0, 0], "number_of_customers": 5,
                               "names": {}}]}
        file = open("rs_setup.json", "w")
        file.write(json.dumps(new_file))
        file.close()
        print "Reservations deleted. "
        print "please select 1, 2 or 3"
        main(cafeteria_tables)

    print ("Thank you for using our program!")
    exit()

main(cafeteria_tables)