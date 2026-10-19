#Participation Activity 2
from pyscript import display, document

# Initial member lists
grade_7 = ['Hernan Cortes', 'Juan Sebastian', 'Henry Stickman']
grade_8 = ['Justin Case', 'Anita Bath', 'Paul E. Tician', 'Ray Poe', 'Edgar Allan Poe', 'Mano Poe']
grade_9 = ['Jose Rizal', 'Karylle Oval']
grade_10 = ['Marc Cortez', 'St. Francis of Assisi', 'St. Nicholas', 'El Filiboosterismo', 'Gerard Gamboa', 'Joe Kerr']

# Master list declared outside the function so additions persist
all_members = grade_7 + grade_8 + grade_9 + grade_10

def add_member(e):
    # Clear previous results
    document.getElementById('results').innerHTML = ''
    
    # Retrieve user input
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    
    # Combine inputs into a single string
    new_member = f"{first_name} {last_name}".strip()
    
    # Add new entry to list
    all_members.append(new_member)
    
    # Display the updated list of members
    display(all_members, target='results')
    
    # Display total count
    total_count = f"Total Members: {len(all_members)}"
    display(total_count, target='results')