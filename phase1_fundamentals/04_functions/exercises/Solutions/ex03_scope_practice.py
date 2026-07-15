z = 15  # global scope

def main():
    def main_function():
        y = 5  # enclosing scope

        def sub_function():
            nonlocal y          # tells Python: don't create a new local y, use the enclosing one
            x = 1                # local scope
            y = y + 10           # modifies the enclosing y, thanks to nonlocal
            print(f"for local scope: x = {x}")
            print(f"for enclosed scope (inside sub_function): y = {y}")
            print(f"for global scope: z = {z}")
            print(f"for built-in scope: len('hello') = {len('hello')}")

        sub_function()
        print(f"for enclosed scope (back in main_function): y = {y}")  # shows y actually changed

    main_function()

if __name__ == "__main__":
    main()