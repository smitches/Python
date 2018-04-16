#  File: Benford.py

#  Description: This will test a theory of the most common leading number in a set of data

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: 11/28/16

#  Date Last Modified: 11/28/16

def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  # fill the rest
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()
  a=0
  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    pop_num=str(pop_num)[0]
    # make entries in the dictionary
    pop_freq[pop_num]+=1
    a+=1
  # close the file
  in_file.close()

  # write out the result
  print('Digit  ', 'Count', '  %')
  for i in range(1,10):
      print(i, '     ', pop_freq[str(i)], ' '*(6-len(str(pop_freq[str(i)]))), round(100*pop_freq[str(i)]/a,1))
  
main()
