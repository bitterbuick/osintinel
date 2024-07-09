# src/username_generator.py

class UsernameGenerator:
    @staticmethod
    def generate_usernames(first_name, last_name):
        usernames = [
            f"{first_name}{last_name}",
            f"{first_name}.{last_name}",
            f"{first_name}_{last_name}",
            f"{first_name[0]}{last_name}",
            f"{first_name}{last_name[0]}"
        ]
        return usernames

# Example usage
if __name__ == "__main__":
    usernames = UsernameGenerator.generate_usernames("john", "doe")
    print(usernames)

