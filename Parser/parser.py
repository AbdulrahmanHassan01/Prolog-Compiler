from nltk.tree import *
from Scanner.Scanner import *
from Parser.predicates import Predicates

errors = []

def Parse(Tokens):
    j=0
    Children=[]
    # remove comments
    Tokens = [t for t in Tokens if 
              (t.to_dict()['token_type'] != token_type.Comment or
                t.to_dict()['token_type'] != token_type.line_comment or
                t.to_dict()['token_type'] != token_type.mline_comment)]
    
    Predicates_dict=Predicates(j, Tokens)
    Children.append(Predicates_dict["node"])
    '''
    Clauses_dict=Clauses(Predicates_dict["index"], Tokens)
    Children.append(Clauses_dict["node"])
    Goal_dict = Goal(Clauses_dict["index"], Tokens)
    Children.append(Goal_dict["node"])
    if(Goal_dict["index"] != len(Tokens)):
        error = dict()
        error["node"]=["error"]
        error["index"]=Goal_dict["index"]
        Children.append(error["node"])
        errors.append("Logic error : more than one Goal in Goals section")
    '''
    Node=Tree('Program',Children)
    return Node, errors

def Match(a,j, Tokens):
    output=dict()
    if(j<len(Tokens)):
        Temp=Tokens[j].to_dict()
        if(Temp['token_type']==a):
            j+=1
            output["node"]=[Temp['Lex']]
            output["index"]=j
            return output
        else:
            output["node"]=["error"]
            output["index"]=j+1
            errors.append("Syntax error : "+Temp['Lex']+" Expected dot")
            return output
    else:
        output["node"]=["error"]
        output["index"]=j+1
        return output