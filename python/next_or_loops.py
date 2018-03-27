def for_loops():
  for i in range(100):
    if i == 9:
      break;
      
def using_next():
  next((x for x in range(100) if x == 9), None)
  

if __name__ == '__main__':
  import timeit
  print(timeit.Timer("for_loops()", setup="from __main__ import for_loops").repeat())
  print(timeit.Timer("using_next()", setup="from __main__ import using_next").repeat())
