class Solution(object):
    def compress(self, chars):
        write = start = 0
        while start < len(chars):
            pointer = start
            while pointer < len(chars) and chars[pointer] == chars[start]:
                pointer += 1
            chars[write] = chars[start]
            write += 1
            length = pointer - start
            if length > 1:
                for i in str(length):
                    chars[write] = i
                    write += 1
            start = pointer

        return write