def partitionString(s):
        counter = 1
        holder = set()
        for i in range(len(s)):
            if s[i] not in holder:
                holder.add(s[i])
            elif s[i] in holder:
                holder.clear()
                holder.add(s[i])
                counter += 1
            print(i, holder)
        
        return counter

print(partitionString("abacaba"))