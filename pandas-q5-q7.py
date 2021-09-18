#this is the pandas part made by Nhi, and the rest is made by Dan
board = pd.DataFrame(sid, columns = ['StudentID'])
board['Grading'] = score
board['Final Result'] = pf
board.to_csv(os.getcwd() + '\\Output\\grading.csv', index = False, header = True)
print("""5. Generating grading.csv (StudentID, Grading).
7. Generating the final result (pass/fail) of the class.""")
board.index += 1
board