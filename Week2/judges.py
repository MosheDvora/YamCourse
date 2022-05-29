def check_position(item_place):
    new_judge_place = 0
    if judges[item_place] > judges[0]:
        new_judge_place += 1
    if judges[item_place] > judges[1]:
        new_judge_place += 1
    if judges[item_place] > judges[2]:
        new_judge_place += 1            
    if judges[item_place] > judges[3]:
        new_judge_place += 1
    if judges[item_place] > judges[4]:
        new_judge_place += 1
    return new_judge_place

judges = ['Esther Hayut', 'Miriam Naor', 'Asher Grunis', 'Dorit Beinisch', 'Aharon Barak']
sorted_judges_list = ["x"] * 5
sorted_judges_list[check_position(0)] = judges[0]
sorted_judges_list[check_position(1)] = judges[1]
sorted_judges_list[check_position(2)] = judges[2]
sorted_judges_list[check_position(3)] = judges[3]
sorted_judges_list[check_position(4)] = judges[4]
print(judges)
print(sorted_judges_list)