# Global constants
NUM_DAYS = 7
FILE_NAME = "runners.txt"

def getRunnerData(filename):
  runners = {}   # Create an empty dictionary
  try:
    with open(filename, 'r') as inFile:
      for line in inFile:        
        items = line.split()    # Extract the tokens
        name = items[0]    # Extract the key field
        miles = []    # List for the scores
        for i in range(1, NUM_DAYS+1):   # Start with index 1
          miles.append(float(items[i]))   # Convert to float
        weekly = sum(miles)
        average = weekly / len(miles)
        runners[name] = {'miles': miles, 'weekly': weekly, 'average': average} # Put a record in the dictionary
  except FileNotFoundError:
    print(f'The file {filename} does not exist')
  return runners

def report(runners):
  print("Name         Su  Mo  Tu  Wd  Th  Fr  Sa  Total   Average")
  for name in runners:
    daystr = ""
    milesRun = runners[name]["miles"]
    for day in range(NUM_DAYS):
      m = f'{milesRun[day]:4.0f}'
      daystr = daystr + m
    print(f'{name:10} {daystr:20} {runners[name]["weekly"]:5.0f}    {runners[name]["average"]:.2f}')

def main():
  runners = getRunnerData(FILE_NAME)
  report(runners)
  

# Call the main function
if __name__ == '__main__':
  main()