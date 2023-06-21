def wrap(string, max_width):
    from math import ceil
    inti=0
    fin=max_width
    result=""
    for i in range(ceil(len(string)/4)):
        try:
            result +=(string[inti:fin] + "\n")
            inti+=max_width
            fin += max_width
        except:
            result+=(string[inti:])
    return(result)

if __name__ == '__main__':
