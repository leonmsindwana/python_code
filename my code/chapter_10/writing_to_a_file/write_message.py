from pathlib import Path


# contents = "I love programming.\n"
# contents += "I love creating new games.\n"
# contents += "I also love working with data.\n"

# path = Path('programming.txt')
# path.write_text(contents)

random_text = "hello i'm random...."

path = Path("random.txt")

path.write_text(random_text)