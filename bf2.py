import sys
import getch

numOfTabs = 0

def startWhile():
  global numOfTabs
  numOfTabs += 1
  return 'while(tape[index] != 0):\n'

def endWhile():
  global numOfTabs
  numOfTabs -= 1
  return 'pass\n'

parser_dict={
    '+': lambda : 'tape[index] += 1\n',
    '-': lambda : 'tape[index] -= 1\n',
    '<': lambda : 'index -= 1\n',
    '>': lambda : 'index += 1\n',
    '.': lambda : 'print(chr(tape[index]), end="")\n',
    '[': startWhile,
    ']': endWhile,
    ',': lambda : 'tape[index] = ord(getch())\n'
    }

def parse(source, o):
  pythonProg = """from getch import getch\ntape = [0] * 5000\nindex = 0\n"""

  f = open(o, 'w')
  f2 = open(source, 'r')

  code = f2.read()
  for i in code:
    if i in parser_dict:
      pythonProg += '\t'*numOfTabs
      pythonProg += parser_dict[i]()

  f.write(pythonProg)
  f.flush()

  f.close()
  f2.close()

if __name__=="__main__":
  parse(sys.argv[1], sys.argv[3])
