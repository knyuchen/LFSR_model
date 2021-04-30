def xor (a, b):
   if a == b:
      return 0
   else:
      return 1

def compare_seq(a, b, n):
   for i in range(n):
      if a[i] != b[i]:
         return 0
   print("same")
   return 1

def copy_seq(a, n):
   b = list()
   for i in range(n):
      b.append(a[i])   
   return b

def forward_LFSR_helper(seq, n, cand, nc):
   temp = seq[n-1]
   for i in range(nc):
      temp = xor(temp, seq[n - 1 - cand[i]]) 
   
   for i in range(0, n-1):
      seq[n-i-1] = seq[n-i-2]
   
   seq[0] = temp
   print(seq)
   return seq
   

def forward_LFSR_recur(in_seq, n, cand, nc, loop):

   if loop == 1:
      print(in_seq)
      seq = in_seq
   else:
      seq = forward_LFSR_recur(in_seq, n, cand, nc, loop-1)
   return(forward_LFSR_helper(seq, n, cand, nc))   

def forward_LFSR_iter(in_seq, n, cand, nc, loop):
   print(in_seq)
   seq = in_seq
   for i in range(loop):
      seq = forward_LFSR_helper(seq, n, cand, nc)
   return seq

def forward_LFSR_length(in_seq, n, cand, nc):
   first = copy_seq(in_seq, n)
   seq = in_seq
   count = 0
   while(True):
      seq = forward_LFSR_helper(seq, n, cand, nc)
      count = count + 1
      if compare_seq(seq, first, n) == 1:
         break
   print(count)
   return count


seq = [1, 0, 0]
cand = [1]
n = 3
nc = 1

#forward_LFSR_recur(seq, n, cand, nc, 2)
#forward_LFSR_iter(seq, n, cand, nc, 2)
#forward_LFSR_length(seq, n, cand, nc)

seq = [1, 0, 0, 0]
cand = [1]
n = 4
nc = 1

#forward_LFSR_recur(seq, n, cand, nc, 15)

seq = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
cand = [11, 10, 4]
n = 12
nc = 3

#forward_LFSR_iter(seq, n, cand, nc, 5)
#forward_LFSR_length(seq, n, cand, nc)
seq = [0, 1, 0, 0, 1, 0]
cand = [5, 2]
n = 6
nc = 2
forward_LFSR_length(seq, n, cand, nc)
