# Task management
arr = []

while 1 :
    print("Select the operation : ")
    print("1) Add a task")
    print("2) Update a task")
    print("3) Remove a task")
    print("4) View tasks")
    print("5) Exit")

    opt = int(input("Enter your choice : "))

    if opt == 1 : 
        task = str(input("Enter the task to add in the list : "))
        arr.append(task)
        print("Task added to the list successfully")
    elif opt == 2 :
        print(arr)
        index = int(input("Enter index of the task you want to update : "))
        newTask = str(input("Enter the new task you want to update with : "))
        arr[index] = newTask
        print("Task updated to the list successfully")
    elif opt == 3 :
        # logic
        print("Task removed to the list successfully")
    elif opt == 4 :
        print(arr)
    else : break

# Write a program to manage a voting system where each voter can vote only once. Use sets to track voters and dictionaries to count votes for candidates.

class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates} 
        self.voters = set()

    def vote(self, voter_id, candidate):
        if voter_id in self.voters:
            return f"Error: Voter {voter_id} has already voted."
        
        if candidate not in self.candidates:
            return f"Error: Candidate '{candidate}' is not valid."
        
        self.votes[candidate] += 1
        self.voters.add(voter_id)
        return f"Voter {voter_id} has successfully voted for '{candidate}'."

    def get_results(self):
        return self.votes

    def display_results(self):
        print("\n--- Voting Results ---")
        for candidate, vote_count in self.votes.items():
            print(f"{candidate}: {vote_count} votes")

    def reset_voting(self):
        self.votes = {candidate: 0 for candidate in self.candidates}
        self.voters.clear()


def main():
    
    candidates = ["Alice", "Bob", "Charlie"]

    voting_system = VotingSystem(candidates)

    print(voting_system.vote("voter1", "a"))
    print(voting_system.vote("voter2", "b"))
    print(voting_system.vote("voter3", "c"))
    print(voting_system.vote("voter1", "d")) 
    print(voting_system.vote("voter4", "e")) 

    voting_system.display_results()

    voting_system.reset_voting()
    print("\nVoting system reset for a new election.")
    voting_system.display_results()


if __name__ == "__main__":
    main()

