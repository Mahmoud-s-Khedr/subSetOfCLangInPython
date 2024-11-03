from lexer import lex

#the code is hard coded for now till the implementation of the interface
code = '''
#include<stdio.h>

int main(){
    int x = 10;
    for (int i = 0; i < x; i++){
        printf("%d", i);//this is a comment
    }
    //this is another comment
    int y = 20;
    for (int i = 0; i < y; i++){
        printf("%d", x*i);
    }
    return 0;
}
    '''
tokens = lex(code)
for token in tokens:
    print("tokenType: ",token[0]," ,tokenValue: " ,token[1])
