import pandas as pd

file = pd.read_excel("Assignment one submission.xlsx")

# set of problems
problems = set(file["problem"])

users_with_multiple_submissions = set()
names_problems = {}

# Create map of username and his submissions
for index, row in file.iterrows():
    if row["username"] not in names_problems:
        names_problems[row["username"]] = []

    if row["problem"]  in  names_problems[row["username"]]:
        users_with_multiple_submissions.add(row["username"])

    names_problems[row["username"]].append(row["problem"])

output_map = {}
output_map["username"] = []

for problem in problems:
    output_map[problem] = []

for user in users_with_multiple_submissions:
    output_map["username"].append(user)
    for problem in problems:
        output_map[problem].append(names_problems[user].count(problem))

output_df = pd.DataFrame(output_map)
writer = pd.ExcelWriter('multible submissions.xlsx', engine='xlsxwriter')
output_df.to_excel(writer,index=False)
