def is_eligible_to_vote(age, is_citizen):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age >= 18 and is_citizen:
        return True
    if age <=17: 
        return False
    print("Not eligible to vote")
    return False
