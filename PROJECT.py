# RITA AFRICA BOOTCAMP PROJECT 
# STUDENT NAME: DOGUNRO HONESTY 
# COUNTRY: NIGERIA
# PROJECT: CUSTOMER FEEDBACK MANAGEMENT SYSTEM 


import pandas as pd
import csv

# Collecting customer feedback data using input function
customer_name1 = input("Enter the first customer's name: ")
customer_rating1 = int(input("Enter the first customer's rating (1-5): "))
customer_feedback1 = input("Enter the first customer's feedback: ")

customer_name2 = input("Enter the second customer's name: ")
customer_rating2 = int(input("Enter the second customer's rating (1-5): "))
customer_feedback2 = input("Enter the second customer's feedback: ")

customer_name3 = input("Enter the third customer's name: ")
customer_rating3 = int(input("Enter the third customer's rating (1-5): "))
customer_feedback3 = input("Enter the third customer's feedback: ")

customer_name4 = input("Enter the fourth customer's name: ")
customer_rating4 = int(input("Enter the fourth customer's rating (1-5): "))
customer_feedback4 = input("Enter the fourth customer's feedback: ")

customer_name5 = input("Enter the fifth customer's name: ")
customer_rating5 = int(input("Enter the fifth customer's rating (1-5): "))
customer_feedback5 = input("Enter the fifth customer's feedback: ")

# Saving the data to a CSV file
with open('customer_feedback.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Rating', 'Feedback'])
    writer.writerow([customer_name1, customer_rating1, customer_feedback1])
    writer.writerow([customer_name2, customer_rating2, customer_feedback2])
    writer.writerow([customer_name3, customer_rating3, customer_feedback3])
    writer.writerow([customer_name4, customer_rating4, customer_feedback4])
    writer.writerow([customer_name5, customer_rating5, customer_feedback5])

# Reading the data from the CSV file
df = pd.read_csv('customer_feedback.csv')

# Displaying the collected feedback
print(df)

# Display the first few rows of the dataset
print(df.head())

# Display the info of the dataset
print(df.info())

# Calculating total and average ratings
total_ratings = df['Rating'].sum()
average_rating = total_ratings / len(df)
print("Average Rating:", average_rating)

# Categorizing feedback for the first customer
feedback_category1 = ''
if customer_rating1 >= 4 and "excellent" in customer_feedback1.lower():
    feedback_category1 = "Very Positive"
elif customer_rating1 >= 4:
    feedback_category1 = "Positive"
elif customer_rating1 >= 3:
    feedback_category1 = "Neutral"
else:
    feedback_category1 = "Negative"

# Repeat for other customers
feedback_category2 = "Positive" if customer_rating2 >= 4 else "Neutral" if customer_rating2 >= 3 else "Negative"
feedback_category3 = "Positive" if customer_rating3 >= 4 else "Neutral" if customer_rating3 >= 3 else "Negative"
feedback_category4 = "Positive" if customer_rating4 >= 4 else "Neutral" if customer_rating4 >= 3 else "Negative"
feedback_category5 = "Positive" if customer_rating5 >= 4 else "Neutral" if customer_rating5 >= 3 else "Negative"

feedback_categories = [feedback_category1, feedback_category2, feedback_category3, feedback_category4, feedback_category5]
print("Feedback Categories:", feedback_categories)

# Analyzing feedback comments
feedback_words1 = customer_feedback1.lower().split()
feedback_words2 = customer_feedback2.lower().split()
feedback_words3 = customer_feedback3.lower().split()
feedback_words4 = customer_feedback4.lower().split()
feedback_words5 = customer_feedback5.lower().split()

# Counting occurrences of a specific word
word_to_count = "service"
word_count1 = feedback_words1.count(word_to_count)
word_count2 = feedback_words2.count(word_to_count)
word_count3 = feedback_words3.count(word_to_count)
word_count4 = feedback_words4.count(word_to_count)
word_count5 = feedback_words5.count(word_to_count)

print(f"Count of '{word_to_count}' in first feedback:", word_count1)
print(f"Count of '{word_to_count}' in second feedback:", word_count2)
print(f"Count of '{word_to_count}' in third feedback:", word_count3)
print(f"Count of '{word_to_count}' in fourth feedback:", word_count4)
print(f"Count of '{word_to_count}' in fifth feedback:", word_count5)
