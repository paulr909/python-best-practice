from faker import Faker

fake = Faker()

# data_employee
data_employee1 = (
    fake.first_name_male(),
    fake.last_name(),
    fake.date(),
    "M",
    fake.date(),
)
data_employee2 = (
    fake.first_name_female(),
    fake.last_name(),
    fake.date(),
    "F",
    fake.date(),
)
data_employee3 = (
    fake.first_name_male(),
    fake.last_name(),
    fake.date(),
    "M",
    fake.date(),
)
data_employee4 = (
    fake.first_name_female(),
    fake.last_name(),
    fake.date(),
    "F",
    fake.date(),
)
data_employee5 = (
    fake.first_name_male(),
    fake.last_name(),
    fake.date(),
    "M",
    fake.date(),
)
data_employee6 = (
    fake.first_name_female(),
    fake.last_name(),
    fake.date(),
    "F",
    fake.date(),
)
data_employee7 = (
    fake.first_name_female(),
    fake.last_name(),
    fake.date(),
    "F",
    fake.date(),
)
data_employee8 = (
    fake.first_name_female(),
    fake.last_name(),
    fake.date(),
    "F",
    fake.date(),
)
data_employee9 = (
    fake.first_name_male(),
    fake.last_name(),
    fake.date(),
    "M",
    fake.date(),
)
data_employee10 = (
    fake.first_name_male(),
    fake.last_name(),
    fake.date(),
    "M",
    fake.date(),
)
# data_salary
data_salary1 = {
    "emp_no": 1,
    "salary": 50000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary2 = {
    "emp_no": 2,
    "salary": 45000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary3 = {
    "emp_no": 3,
    "salary": 56000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary4 = {
    "emp_no": 4,
    "salary": 68000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary5 = {
    "emp_no": 5,
    "salary": 57000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary6 = {
    "emp_no": 6,
    "salary": 65000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary7 = {
    "emp_no": 7,
    "salary": 56000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary8 = {
    "emp_no": 8,
    "salary": 67000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary9 = {
    "emp_no": 9,
    "salary": 60000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_salary10 = {
    "emp_no": 10,
    "salary": 85000,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
# data_dept
data_dept1 = {
    "dept_no": 1,
    "dept_name": "Data Analytics",
}
data_dept2 = {
    "dept_no": 2,
    "dept_name": "Finance",
}
data_dept3 = {
    "dept_no": 3,
    "dept_name": "DevOps",
}
data_dept4 = {
    "dept_no": 4,
    "dept_name": "Business",
}
data_dept5 = {
    "dept_no": 5,
    "dept_name": "HR",
}
data_dept6 = {
    "dept_no": 6,
    "dept_name": "Media",
}
# data_manager
data_manager1 = {
    "emp_no": 1,
    "dept_no": 3,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager2 = {
    "emp_no": 2,
    "dept_no": 6,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager3 = {
    "emp_no": 3,
    "dept_no": 1,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager4 = {
    "emp_no": 4,
    "dept_no": 3,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager5 = {
    "emp_no": 5,
    "dept_no": 2,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager6 = {
    "emp_no": 6,
    "dept_no": 3,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager7 = {
    "emp_no": 7,
    "dept_no": 4,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager8 = {
    "emp_no": 8,
    "dept_no": 6,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager9 = {
    "emp_no": 9,
    "dept_no": 5,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_manager10 = {
    "emp_no": 10,
    "dept_no": 4,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
# data_title
data_title1 = {
    "emp_no": 1,
    "title": "Data Analyst",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title2 = {
    "emp_no": 2,
    "title": "Project Lead",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title3 = {
    "emp_no": 3,
    "title": "Software Developer",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title4 = {
    "emp_no": 4,
    "title": "Marketing Executive",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title5 = {
    "emp_no": 5,
    "title": "Line Manager",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title6 = {
    "emp_no": 6,
    "title": "HR Executive",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title7 = {
    "emp_no": 7,
    "title": "Finance Executive",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title8 = {
    "emp_no": 8,
    "title": "Media Executive",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title9 = {
    "emp_no": 9,
    "title": "HR Executive",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_title10 = {
    "emp_no": 10,
    "title": "Full Stack Developer",
    "from_date": fake.date(),
    "to_date": fake.date(),
}
# data_dept_emp
data_dept_emp1 = {
    "emp_no": 1,
    "dept_no": 5,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp2 = {
    "emp_no": 2,
    "dept_no": 1,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp3 = {
    "emp_no": 3,
    "dept_no": 2,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp4 = {
    "emp_no": 4,
    "dept_no": 5,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp5 = {
    "emp_no": 5,
    "dept_no": 6,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp6 = {
    "emp_no": 6,
    "dept_no": 4,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp7 = {
    "emp_no": 7,
    "dept_no": 2,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp8 = {
    "emp_no": 8,
    "dept_no": 5,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp9 = {
    "emp_no": 9,
    "dept_no": 6,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
data_dept_emp10 = {
    "emp_no": 10,
    "dept_no": 3,
    "from_date": fake.date(),
    "to_date": fake.date(),
}
