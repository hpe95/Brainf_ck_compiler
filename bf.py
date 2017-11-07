import click

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
    cprog="""#include<stdio.h>
#include<stdlib.h>\n
    int main(){
        char *tape = malloc(sizeof(char) * 3000);\n"""
 #to initialize the brainf*** environment
    lines = source.read()
    for i in lines:
      if i in parser_dict:
        cprog += parser_dict[i] 
    
    cprog += "\n return 0; \n} "
    o.write(cprog)
    o.flush()

#main program
if __name__=="__main__":
    parse()