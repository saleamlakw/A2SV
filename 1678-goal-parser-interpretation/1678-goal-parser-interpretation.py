class Solution:
    def interpret(self, command: str) -> str:
        re=""
        i=0
        while i<len(command):
            if command[i]=="G":
                re+="G"
                i+=1
            elif command[i]=="(":
                if command[i+1]==")":
                    re+="o"
                    i+=2
                elif command[i+1]=="a":
                    re+="al"
                    i+=4
            
        return re
                
            
        