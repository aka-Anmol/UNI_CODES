#input student records

#get details
name = input("Enter student name: ")
id = input("Enter student ID: ")
english_mark = float(input("Enter mark for English: "))
maths_mark = float(input("Enter mark for Maths: "))
science_mark = float(input("Enter mark for Science: "))

#calculate average
average = (english_mark + maths_mark + science_mark) / 3

#print average
print(f"{name} (ID: {id}) has an average of {average}%")
