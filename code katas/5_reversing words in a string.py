def reverse(string):
    gnirst = string.split()[::-1]
    new_string = " ".join(gnirst)
    return new_string

string = "Hello World"

rev_st = reverse(string)

print(rev_st)