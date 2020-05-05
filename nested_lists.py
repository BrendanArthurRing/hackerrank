# https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen


students = []
scores = []
"""
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
"""
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
scores = [37.21, 37.21, 37.2, 41, 39]

def find_2nd_lowest_score(arr):
    return sorted(set(arr))[1]

def get_names(arr):
    names = []
    for i in arr:
        if find_2nd_lowest_score(scores) in arr:
            


"""
Given the names and grades for each student in a Physics class of n students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the same grade, 
rder their names alphabetically and print each name on a new line.
"""

"""
Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry
"""

