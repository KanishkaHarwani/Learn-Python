from collections import deque, Counter, defaultdict
def main():
    my_text = """there are 15 people on the road that work 
    for the mafia in front of me but I am the only one on this side.
    the 'capo' is out for my blood but what can I do when I asked
    chief to give me the simple burglary case I was happy thinking
    I got an easy case but its been a long journey since. I found 
    some truths, some things no one should know and also got 
    betrayed in the middle. I am still standing here knowing this 
    day might be my last and the world is too harsh for me.    
    """
    words = my_text.split()
    text_d = deque(words)
    print(Counter(text_d).most_common(10))

    expenses = [('poha', 60), ('Pepsi', 40), ('coke', 20), ('poha', 180),
                ('pepsi', 20), ('eggs', 48), ('dabeli', 35), ('poha', 120),
                ('eggs', 51), ('laundry', 350), ('pepsi', 20), ('coke', 20), ('dabeli', 65)]
    d = defaultdict(list)
    for k, v in expenses:
        d[k].append(v)

    sorted(d.items())
    print(d.items())
    pass


if __name__ == "__main__":
    main()
