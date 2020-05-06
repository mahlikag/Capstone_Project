# Capstone_Project

The following is some instructions on how to best execute the data cleaning and network files. You will need both Python and either R or Rstudio.

You will also need to download the csv file 'Sorted' from myCourses. This file contains some pseduo data of crime incidents for cities within the US. The incidents are listed row by row in the csv, only containing incidents that involved a firearm and organized from the highest populated city to smallest. 

Once that is complete, it will be easier to set the working directory to wherever you have the downloaded files from the repository and the Sorted.csv(submitted on myCourses).
Having all of these things in one place set your working directory to that location before you move any further.
Once the working directory is set, we will be using the Data_Cleaning.R file. Although there is a Rmd file in the repository as well, the R file will run much smoother, without any issues.

Before running the R file, you may need to install the following programs in R or Rstudio:



  Xlsx (by using the command 'install.packages('xlsx')'
  
  *Remember to install that package in the terminal of R or Rstudio
  
To run the program, you could open the R file and run it manually or simply type the command 'source("~/Capstone_Project/Data_Cleaning.R")', in the R or Rstudio terminal. 

This may take a minute or two. Once it's complete, you will notice that there is a new file in your working directory named 'testing.xlsx'. This is perfect!!
That file is needed for the graphing portion of this process.

Before running the python file, you while need to install the following programs if they are not already installed on your computer:


  Read_excel (by using the command 'pip install xlrd')
  
  
  NetworkX (by using the command 'pip install networkx')
  
  
  Matplotlib (by using the command 'pip install matplotlib')
  
  
  Pandas (by using the command 'pip install pandas')
  
  
  
  
You can then open the Networkx.py file and run the program!!

Python should produce a total of two graphs showing the networks described in the paper. 
