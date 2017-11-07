import click

parser_dict={
    '+': '++(*tape);\n',
    '-': '--(*tape);\n',
    '<': '--tape;\n',
    '>': '++tape;\n',
    '.': 'printf("%c",(*tape));\n',
    '[': ' while(*tape) {\n',
    ']': ' }\n',
    ',': 'scanf("%c",&tape);\n'
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
    int main(){
        static char mem[30000], *tape\n;
        tape=mem\n;   
        """
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