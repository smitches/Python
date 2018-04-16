#  File: DNA.py

#  Description: This program finds longest similar strand

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867   

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: October 26, 2016

#  Date Last Modified: October 26, 2016

def main():
    in_file=open("./dna.txt","r")
    num_pairs=in_file.readline()
    num_pairs=num_pairs.strip()
    num_pairs=int(num_pairs)
    for i in range(num_pairs):
        print('Pair', i+1, end='')
        print(":", end=' ')
        st1=in_file.readline()
        st2=in_file.readline()
        st1=st1.strip()
        st2=st2.strip()
        st1=st1.upper()
        st2=st2.upper()
        if len(st1)>len(st2):
            dna1=st1
            dna2=st2
        else:
            dna1=st2
            dna2=st1
        maxlen=0
        wnd=len(dna2)
        flag=False
        while wnd>1:
            start_idx=0
            while start_idx+wnd<=len(dna2):
                sub_strand=dna2[start_idx:start_idx+wnd]
                if dna1.count(sub_strand)>0:
                    maxlen=len(sub_strand)
                    print(sub_strand)
                    print('        ', end='')
                    flag=True
                start_idx+=1
            if maxlen>0:
                break
            wnd-=1
        if not flag:
            print('No Common Sequence Found')
        print()
    in_file.close()
main()
