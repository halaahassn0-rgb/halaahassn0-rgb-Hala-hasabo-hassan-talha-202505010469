
def create_ticket():
    print("=== IT Helpdesk Ticket ===")
 
    student_name = input("Student Name : ")
    student_id = input("Student ID : ")
    issue = input("Issue : ")
    location = input("Location : ")
    priority = input("Priority (High/Medium/Low): ")
 
    # Assign technician based on priority level
    if priority.strip().lower() == "high":
        technician = "Ahmad"
    elif priority.strip().lower() == "medium":
        technician = "Siti"
    elif priority.strip().lower() == "low":
        technician = "Ali"
    else:
        technician = "Unassigned"
 
    status = "Pending"
 
    return (
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician,
        status
    )
 
