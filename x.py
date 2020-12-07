import pandas as pd

f = pd.read_csv("hospital_directory.csv",usecols=["Sr_No","Hospital_Name","Location","Address_Original_First_Line","Mobile_Number","Number_Doctor"])
print(f)