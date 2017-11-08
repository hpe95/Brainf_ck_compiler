import click

#Dict that represents the parser between brainf_ck-code and c-code
parser_dict={
    '+': '\t++(*tape);\n',
    '-': '\t--(*tape);\n',
    '<': '\t--tape;\n',
    '>': '\t++tape;\n',
    '.': '\tprintf("%c",(*tape));\n',
    '[': '\twhile(*tape) {\n',
    ']': '\t}\n',
    ',': '\tscanf("%c",&tape);\n'
    }

"""
click commands are used to get arguments on command line
first argument is the source file in brainfuck
second argument "-o file_name" is the file in c that will receive
the translation
"""
@click.command()
@click.argument('source', type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))

def parse(source, o):
  """
    source: An input file with .bf extension
    o: An output file with .c extension
    Reads the lines from the input file,
    and parsers the code using parser_dict,
    then writes to the output file
  """

  cprog="""#include<stdio.h>
#include<stdlib.h>\n
    int main(){
        char *tape = malloc(sizeof(char) * 3000);\n"""
 
  code = source.read()
  for i in code:
    if i in parser_dict:
      cprog += parser_dict[i] 
    
  cprog += "\n return 0; \n} "
  o.write(cprog)
  o.flush()

#main program
if __name__=="__main__":
  parse()