###solution to exercise 88 from ben stephenson's "the python workbook".
###assumes 3 parameters for the top function.

def is_valid_triangle(x, y, z):
  params = [x, y, z]
  params.sort()

  if (params[2] >= (params[1] + params[0])):
    return False
  else:
    return True


lengths = input('Enter the three sides:' ).split(',')
lengths = [float(i) for i in lengths]

if(is_valid_triangle(lengths[0],lengths[1],lengths[2])):
  print('That is a valid triangle.')
else:
  print('That is an invalid triangle.')
